import os
import ast
import json
from core.llm import ask_llm
from core.tool_manager import get_tool_list
from core.tool_selector import select_tool
from core.tool_executor import execute_tool
from core.memory_selector import select_memory
from knowledge_base.service import KnowledgeBase

from memory.memory import (
    load_facts,
    load_memory,
    save_memory,
    save_fact,
    delete_fact,
    search_memory,
    search_tool_logs,
    search_tool_logs_by_keywords,
    remember_fact,
    load_development_history,
    search_development_history,
    add_development_history,
    update_development_history
)

def process(question):

    print("DEBUG process() received question:", repr(question))

    remember_fact(question)

    # =========================
    # Development History 登録依頼
    # =========================

    if question.startswith("開発履歴を登録："):

        history_json = question.split(
            "開発履歴を登録：",
            1
        )[1].strip()

        try:
            entry = json.loads(history_json)

        except json.JSONDecodeError as e:
            return f"開発履歴のJSON形式が正しくありません：{e}"

        required_fields = (
            "id",
            "date",
            "file",
            "feature",
            "changes",
            "purpose",
            "syntax_check",
            "execution_test",
            "status"
        )

        if not isinstance(entry, dict):
            return "登録データはJSONオブジェクトで指定してください。"

        if not all(field in entry for field in required_fields):
            return "登録に必要な項目が不足しています。"

        history = load_development_history()

        if any(item.get("id") == entry["id"] for item in history):
            return f"ID {entry['id']} は既に登録されています。"

        add_development_history(entry)

        return f"開発履歴 ID {entry['id']} を登録しました。"

    # =========================
    # Development History 更新依頼
    # =========================

    if question.startswith("開発履歴を更新："):

        history_json = question.split(
            "開発履歴を更新：",
            1
        )[1].strip()

        try:
            update_data = json.loads(history_json)

        except json.JSONDecodeError as e:
            return f"更新データのJSON形式が正しくありません：{e}"

        if not isinstance(update_data, dict):
            return "更新データはJSONオブジェクトで指定してください。"

        if "id" not in update_data:
            return "更新対象のIDが指定されていません。"

        allowed_fields = (
            "syntax_check",
            "execution_test",
            "status"
        )

        if not any(
            field in update_data
            for field in allowed_fields
        ):
            return "更新する項目が指定されていません。"

        result = update_development_history(
            history_id=update_data["id"],
            syntax_check=update_data.get("syntax_check"),
            execution_test=update_data.get("execution_test"),
            status=update_data.get("status")
        )

        if result:
            return f"開発履歴 ID {update_data['id']} を更新しました。"

        return f"開発履歴 ID {update_data['id']} が見つかりません。"
    
    # =========================
    # Facts Memoryの変更依頼
    # =========================

    change_markers = (
        "を",
        "に変更してください",
    )

    if (
        change_markers[0] in question
        and change_markers[1] in question
    ):
        key, value = question.split("を", 1)
        value = value.split("に変更してください", 1)[0].strip()

        key = key.replace("私の", "").strip()

        if key and value:
            facts = load_facts()

            # 登録済みの項目だけ変更する
            if key not in facts:
                answer = f"「{key}」はMemoryに登録されていません。変更は行いませんでした。"
            else:
                save_fact(key, value)
                facts_after_save = load_facts()

                if facts_after_save.get(key) == value:
                    answer = f"{key}を「{value}」に変更し、保存しました。"
                else:
                    answer = f"{key}の変更を保存できませんでした。"

            messages = load_memory()
            messages.append({
                "role": "user",
                "content": question
            })
            messages.append({
                "role": "assistant",
                "content": answer
            })
            save_memory(messages)

            return answer

    # =========================
    # Facts Memoryの削除依頼
    # =========================

    delete_markers = (
        "の記憶を削除してください",
        "の記憶を削除して",
        "を削除してください",
        "を削除して"
    )

    for marker in delete_markers:

        if marker in question:

            key = question.split(marker, 1)[0]
            key = key.replace("私の", "").strip()

            if key:

                facts = load_facts()

                if key not in facts:
                    answer = f"「{key}」はMemoryに登録されていません。削除は行いませんでした。"

                else:
                    deleted = delete_fact(key)

                    if deleted:
                        answer = f"「{key}」をFacts Memoryから削除しました。"
                    else:
                        answer = f"「{key}」の削除を確認できませんでした。"

                messages = load_memory()

                messages.append({
                    "role": "user",
                    "content": question
                })

                messages.append({
                    "role": "assistant",
                    "content": answer
                })

                save_memory(messages)

                return answer

    # =========================
    # 元の依頼文を取り出す
    # =========================

    intent_question = question

    if "【今回の依頼】" in question:
        intent_question = question.split(
            "【今回の依頼】", 1
        )[1]

        for marker in (
            "【前のTaskの実行結果】",
            "【前回の回答検証エラー：修正必須】",
        ):
            intent_question = intent_question.split(
                marker, 1
            )[0]

        intent_question = intent_question.strip()

    question_lower = intent_question.lower()

    # =========================
    # 過去の結果を要求しているか
    # =========================

    asking_previous_result = (
        "以前" in intent_question
        or "過去" in intent_question
        or "前回" in intent_question
        or "前に" in intent_question
    )
    print(
        "過去結果要求：",
        asking_previous_result
    )

    # =========================
    # Memory Selector
    # =========================

    memory_selection = select_memory(question)

    selected_memories = memory_selection.get(
        "memories",
        []
    )

    relevant_tool_logs = []

    # =========================
    # Knowledge Base
    # =========================

    relevant_knowledge = []
    knowledge_base = None

    if "knowledge_base" in selected_memories:

        try:
            knowledge_base = KnowledgeBase()

            relevant_knowledge = knowledge_base.search(
                intent_question,
                limit=5
            )

            print(
                "Knowledge Base検索結果：",
                relevant_knowledge
            )

            print("===== Knowledge Base 出典情報 =====")

            for item in relevant_knowledge:
                print(
                    "文書名:", item.get("filename"),
                    "| チャンク:", item.get("chunk_index"),
                    "| 類似度:", round(item.get("score", 0), 4),
                    "| 保存場所:", item.get("source")
                )

            print("===================================")

        except Exception as e:
            print("Knowledge Base検索エラー：", e)

        finally:
            if knowledge_base is not None:
                knowledge_base.close()

    print(
        "Memory選択結果：",
        memory_selection
    )

    facts = load_facts()
    messages = load_memory()

    # =========================
    # Conversation Memory
    # =========================

    relevant_memory = []

    conversation_keyword = question

    if "conversation" in selected_memories:

        conversation_keyword = question


    elif "初回案内メール" in question:
            conversation_keyword = "初回案内メール"

    print("DEBUG conversation_keyword:", repr(conversation_keyword))

    print("===== DEBUG 最近の会話 =====")

    for message in messages[-15:]:
            print(
                message.get("role"),
                repr(message.get("content", "")[:200])
            )

    print("============================")

    if "conversation" in selected_memories:

        relevant_memory = search_memory(
            messages,
            conversation_keyword
        )

    else:

        relevant_memory = []

    print(
            "Conversation検索結果：",
            relevant_memory
        )

    # =========================
    # Development History
    # =========================

    relevant_development_history = []

    if "development_history" in selected_memories:

        development_keyword = ""

        development_history = load_development_history()

        # 登録されているファイル名を長い順に確認
        filenames = sorted(
            {
                entry.get("file", "")
                for entry in development_history
                if entry.get("file", "")
            },
            key=len,
            reverse=True
        )

        # 質問文に含まれるファイル名を特定
        for filename in filenames:

            if filename.lower() in question.lower():

                development_keyword = filename
                break

        # ファイル名が指定された場合は完全一致で取得
        if development_keyword:

            relevant_development_history = [
                entry
                for entry in development_history
                if entry.get("file", "").lower()
                == development_keyword.lower()
            ]

            relevant_development_history = (
                relevant_development_history[-10:]
            )

        # ファイル名がなければ直近10件を取得
        else:

            relevant_development_history = search_development_history(
                "",
                limit=10
            )

        print(
            "Development History検索結果：",
            relevant_development_history
        )  

    # =========================
    # Tool Logs
    # =========================

    if "tool_logs" in selected_memories:

        tool_keywords = []

         # Tool履歴全体の表示要求
        show_all_tool_logs = any(
            word in question_lower
            for word in (
                "toolの実行履歴",
                "tool履歴",
                "toolの履歴",             # 今回追加
                "tool実行履歴",
                "これまでのtool実行履歴",
                "過去のtool実行履歴",           
                "過去のtool実行履歴",
                "ツールの実行履歴",
                "ツール履歴",
                "実行ログを見せて",
                "実行履歴を見せて",
            )
        )       

        recent_tool_question = any(
            word in question
            for word in (
                "直前に実行したTool",
                "直近のTool",
                "直前のTool",
                "直近に実行したTool",
            )
        )

        relevant_tool_logs = []

        # =========================
        # Random
        # =========================

        if (
            "random" in question_lower
            or "ランダム" in question
            or "generate_random_number" in question
        ):

            tool_keywords.extend([
                "random",
                "generate_random_number"
            ])

        # =========================
        # Calculate
        # =========================

        if (
            "計算" in question
            or "掛け算" in question
            or "足し算" in question
            or "引き算" in question
            or "割り算" in question
            or "calculate" in question_lower
        ):

            tool_keywords.append(
                "calculate"
            )

        # =========================
        # Current Time
        # =========================

        if (
            "時刻" in question
            or "時間" in question
            or "現在時刻" in question
            or "get_current_time" in question
        ):

            tool_keywords.append(
                "get_current_time"
            )

        # =========================
        # Current Date
        # =========================

        if (
            "日付" in question
            or "何日" in question
            or "今日" in question
            or "get_current_date" in question
        ):

            tool_keywords.append(
                "get_current_date"
            )

        # =========================
        # System Info
        # =========================

        if (
            "pc" in question_lower
            or "システム情報" in question
            or "get_system_info" in question
        ):

            tool_keywords.append(
                "get_system_info"
            )

        # =========================
        # 重複削除
        # =========================

        tool_keywords = list(
            dict.fromkeys(tool_keywords)
        )

        print(
            "Tool検索キーワード：",
            tool_keywords
        )


        # =========================
        # Tool履歴検索
        # =========================

        if recent_tool_question:
            relevant_tool_logs = search_tool_logs("", limit=1)

        elif show_all_tool_logs and not tool_keywords:
            relevant_tool_logs = search_tool_logs("", limit=10)

        elif tool_keywords:
            relevant_tool_logs = search_tool_logs_by_keywords(
                tool_keywords,
                limit=10
            )

        print("Tool Logs件数：", len(relevant_tool_logs))

        # =========================
        # 過去結果
        # =========================

        print(
            "過去結果としてLLMへ渡すTool Logs：",
            relevant_tool_logs
        )

    # =========================
    # Facts
    # =========================

    context = ""

    if "facts" in selected_memories:

        for key, value in facts.items():

            context += f"{key}: {value}\n"

    # =========================
    # Tool選択
    # =========================

    tool = "none"
    arguments = {}
    new_tool_result = None

    # 新しいTool実行を明示的に要求している質問

    # Tool履歴を取得する質問かどうか
    tool_logs_request = (
        "実行履歴" in intent_question
        or "Tool履歴" in intent_question
        or "ツール履歴" in intent_question
    )

    tool_execution_request = (
        not tool_logs_request
        and (
           "生成して" in intent_question
            or "生成してください" in intent_question
            or "計算して" in intent_question
            or "計算してください" in intent_question
            or "掛け算" in intent_question
            or "掛けて" in intent_question
            or "足し算" in intent_question
            or "足して" in intent_question
            or "引き算" in intent_question
            or "引いて" in intent_question
            or "割り算" in intent_question
            or "割って" in intent_question
            or "実行して" in intent_question
            or "実行してください" in intent_question
            or "調べて" in intent_question
            or "取得して" in intent_question
            or "検索して" in intent_question
            or "検索してください" in intent_question
            or "要約して" in intent_question
            or "要約してください" in intent_question
            or "もう一度" in intent_question
            or "今日" in intent_question
            or "現在" in intent_question
            or "今何時" in intent_question
        )
    )

    print("DEBUG selected_memories:", selected_memories)
    print("DEBUG asking_previous_result:", asking_previous_result)
    print("DEBUG tool_logs_request:", tool_logs_request)
    print("DEBUG tool_execution_request:", tool_execution_request)

  
    # =========================
    # Tool Selector
    # =========================

    if (
        not asking_previous_result
        and tool_execution_request
    ):

        tools = get_tool_list()


        # Tool履歴の取得件数が明示されている場合
        if "get_tool_logs" in question and "limit=1" in question:

            selection = {
                "tool": "get_tool_logs",
                "arguments": {"limit": 1}
            }

        # 日付取得が明確な質問は、LLMを介さずToolを指定する
        elif (
            "今日" in question
            or "今日の日付" in question
            or "何日" in question
            or "get_current_date" in question
        ):
            selection = {
                "tool": "get_current_date",
                "arguments": {}
            }

        else:
            selection = select_tool(
                question,
                tools
            )


        tool = selection.get(
            "tool",
            "none"
        )

        arguments = selection.get(
            "arguments",
            {}
        )

        
        # Tool履歴の検索対象を質問から指定する
        if tool == "get_tool_logs":
            if "calculate" in question.lower():
                arguments["tool_name"] = "calculate"
            elif "generate_random_number" in question.lower():
                arguments["tool_name"] = "generate_random_number"
            elif "get_current_time" in question.lower():
                arguments["tool_name"] = "get_current_time"
            elif "get_current_date" in question.lower():
                arguments["tool_name"] = "get_current_date"
            elif "get_system_info" in question.lower():
                arguments["tool_name"] = "get_system_info"


    print(
        "Tool実行前の過去Tool Logs：",
        relevant_tool_logs
    )


    # =========================
    # Tool Execution
    # =========================

    if tool != "none":

        result = execute_tool(
            tool,
            arguments
        )

        new_tool_result = result

        print(
            "今回新しく実行したTool：",
            tool
        )

        print(
            "今回のTool実行結果：",
            new_tool_result
        )

        # =========================
        # Tool + MemoryをLLMへ送る
        # =========================

        prompt = f"""
あなたはAI COREです。

ユーザーの質問：
{question}

=========================
Memory情報
=========================

【Conversation Memory】
{relevant_memory}

【Facts Memory】
{context}

【Tool Logs Memory】
{relevant_tool_logs}

【Knowledge Base】
{relevant_knowledge}

【Development History】
{relevant_development_history}
=========================
今回新しく実行したTool
=========================

Tool：
{tool}

実行結果：
{new_tool_result}

=========================
回答ルール
=========================

1. Memory情報に存在する情報は正確に使用してください。

2. 今回新しく実行したToolの結果も正確に使用してください。

3. Toolの実行結果に複数のデータが含まれている場合は、
   すべてのデータを漏れなく確認して回答してください。
   特に複数のメールが含まれている場合は、
   メールごとに番号を付けて個別に要約してください。
   一部のメールだけを選んで回答してはいけません。
   取得件数と回答件数が一致していることを確認してください。

4. 今回のTool結果を、
   過去のTool Logsの結果と混同しないでください。

5. Toolの実行結果を変更、推測、再計算しないでください。

6. calculateの結果についても、
   LLM自身で再計算せず、
   「実行結果」に記載された値をそのまま使用してください。

7. 新しいToolを実行した場合は、
   今回新しく実行したToolの実行結果を優先して回答してください。
   Tool Logs Memoryの過去の結果は、
   ユーザーが過去の結果を尋ねている場合にのみ使用してください。

8. Memoryごとに別々の回答を生成しないでください。

9. 「回答：」を複数回出力しないでください。

10. 自然で簡潔な日本語で回答してください。

11. 「今回新しく実行したTool」の実行結果は、
    Tool Logs Memoryにある過去のTool履歴とは別のものとして扱ってください。

12. ユーザーが以前の結果、過去の結果、以前の計算結果、
    過去の計算結果、前回の結果などを尋ねている場合は、
    Tool Logs Memoryに記録されている過去の結果だけを回答してください。
    今回新しく実行したToolの結果は、
    過去の結果として扱わないでください。

13. 過去結果を利用する場合は、
    Toolを新しく実行せず、
    Tool Logs Memoryに記録された結果を
    そのまま使用してください。

=========================
"""

        print(
            "===== TOOL + MEMORY LLM PROMPT ====="
        )
        print(prompt)

        print(
            "===================================="
        )

        print(
            "PROMPT LENGTH =",
            len(prompt)
        )

    # =========================
    # 通常のLLM
    # =========================

    else:

        print(
            "Tool履歴：",
            relevant_tool_logs
        )

        print(
            "Conversation：",
            relevant_memory
        )

        prompt = f"""
あなたはAI COREです。

ユーザーの質問：
{question}

=========================
Memory情報
=========================

【Conversation Memory】
{relevant_memory}

【Facts Memory】
{context}

【Tool Logs Memory】
{relevant_tool_logs}

【Knowledge Base】
{relevant_knowledge}

【Development History】
{relevant_development_history}

=========================
回答ルール
=========================

1. Memory情報に存在する情報は正確に使用してください。

2. Conversation Memory、Facts Memory、
   Tool Logs Memoryに関連情報がある場合は、
   それらを1つの自然な回答に統合してください。

3. Memoryごとに別々の回答を生成しないでください。

4. Tool Logs Memoryに複数の関連する結果がある場合は、
   その結果をすべて正確に回答してください。

5. Tool Logs Memoryに記録された数値や結果を、
   推測、再計算、変更しないでください。

6. 提示されたMemoryに存在しない過去の情報を、
   推測して使用しないでください。

7. ユーザーが過去のTool実行結果だけを尋ねている場合は、
   Tool Logs Memoryに記録されている結果を正確に回答してください。
   Conversation Memoryなど、他のMemory情報も尋ねている場合は、
   それらの関連情報も含めて1つの回答に統合してください。

8. Memory情報が空の場合は、
   Memoryを使用せず、通常のLLMとして回答してください。

9. 「回答：」を複数回出力しないでください。

10. 回答は1つのまとまった文章として生成してください。

11. 自然で簡潔な日本語で回答してください。

12. Knowledge Baseの情報を回答に使用した場合は、
    検索結果に含まれるfilenameを参照資料として
    回答の末尾に記載してください。

13. Knowledge Baseの検索結果が空の場合や、
    回答に使用していない場合は、
    参照資料を記載しないでください。
    検索結果に存在しないファイル名を
    推測して記載してはいけません。

14. Development Historyを使用する場合は、
    各履歴のstatusとexecution_testを個別に確認してください。

15. statusが"completed"の履歴だけを
    完了済みとして説明してください。

16. statusが"test"の履歴はテスト段階として説明し、
    execution_testが"pending"の場合は
    実行テスト未完了として扱ってください。

17. 複数の履歴がある場合、
    一部の履歴の状態を他の履歴に適用せず、
    それぞれの状態を区別して回答してください。    

=========================
"""


    # =========================
    # 過去の計算結果を直接取得
    # =========================

    previous_result_answer = None
    previous_calculation_request = False
    requested_operation = None

    calculation_terms = (
        "計算", "掛け算", "掛けて", "乗算",
        "足し算", "足して", "加算",
        "引き算", "引いて", "減算",
        "割り算", "割って", "除算"
    )

    if asking_previous_result and not tool_logs_request:

        print(
            "DEBUG calculation term matches:",
            [term for term in calculation_terms if term in intent_question]
        )

        if any(term in intent_question for term in calculation_terms):

            previous_calculation_request = True

            # 質問から計算の種類を判定
            if any(
                term in intent_question
                for term in ("掛け算", "掛けて", "乗算")
            ):
                requested_operation = "multiply"
                operation_label = "掛け算"

            elif any(
                term in intent_question
                for term in ("足し算", "足して", "加算")
            ):
                requested_operation = "add"
                operation_label = "足し算"

            elif any(
                term in intent_question
                for term in ("引き算", "引いて", "減算")
            ):
                requested_operation = "subtract"
                operation_label = "引き算"

            elif any(
                term in intent_question
                for term in ("割り算", "割って", "除算")
            ):
                requested_operation = "divide"
                operation_label = "割り算"

            else:
                # 計算種類の指定がなければ、全種類を対象にする
                requested_operation = None
                operation_label = "計算"

            # 全履歴の要求か判定
            asking_all_calculation_history = any(
                term in intent_question
                for term in ("すべて", "全て", "全部", "全件", "一覧")
            )

            log_file = "logs/tool.log"
            matching_logs = []

            if os.path.exists(log_file):

                with open(log_file, "r", encoding="utf-8") as f:
                    log_lines = f.readlines()

                # 新しいログから順番に調べる
                for line in reversed(log_lines):

                    parts = line.strip().split(" | ", 3)

                    if len(parts) != 4:
                        continue

                    timestamp, tool_name, arguments_text, result = parts

                    if tool_name != "calculate":
                        continue

                    try:
                        arguments = ast.literal_eval(arguments_text)
                    except (ValueError, SyntaxError):
                        continue

                    if not isinstance(arguments, dict):
                        continue

                    # 計算種類が指定されていれば一致させる
                    if (
                        requested_operation is not None
                        and arguments.get("operation") != requested_operation
                    ):
                        continue

                    # エラーや異常値を除外する
                    result_text = result.strip()

                    if result_text.lower() in ("inf", "-inf", "nan"):
                        continue

                    if "計算Toolに必要な引数が正しくありません" in result_text:
                        continue

                    # 正常な履歴を記録日時ごとに保持する
                    matching_logs.append((timestamp, result_text))

                    # 「すべて」の要求でなければ最新の1件で終了
                    if not asking_all_calculation_history:
                        break

            if matching_logs:

                if asking_all_calculation_history:

                    answer_lines = [
                        f"- {result}（記録日時：{timestamp}）"
                        for timestamp, result in matching_logs
                    ]

                    previous_result_answer = (
                        f"過去の{operation_label}の結果は、"
                        f"以下の{len(matching_logs)}件です。\n"
                        + "\n".join(answer_lines)
                    )

                else:

                    timestamp, result = matching_logs[0]

                    previous_result_answer = (
                        f"前回の{operation_label}の結果は、"
                        f"{result}です。"
                        f"（記録日時：{timestamp}）"
                    )

            else:

                previous_result_answer = (
                    f"該当する過去の{operation_label}の履歴は"
                    "見つかりませんでした。"
                )

            print(
                "過去の計算結果を直接取得：",
                previous_result_answer
            )

            print(
                "DEBUG previous_calculation_request:",
                previous_calculation_request
            )

            print(
                "DEBUG previous_result_answer:",
                previous_result_answer
            )

    # =========================
    # LLM Prompt Check
    # =========================

    print(
        "===== LLM PROMPT ====="
    )

    print(prompt)

    print(
        "======================"
    )

    print(
        "===== PROMPT CHECK ====="
    )

    print(
        "Prompt文字数：",
        len(prompt)
    )



    print(
        "Question：",
        question
    )

    print(
        "========================"
    )

 
    # =========================
    # calculate結果は直接回答する
    # =========================

    
    # =========================
    # 回答方法の選択
    # =========================

    if previous_calculation_request and (
        "conversation" in selected_memories
        or "facts" in selected_memories
    ):
        if "conversation" in selected_memories:
            # 会話履歴と過去の計算結果をLLMで統合
            answer = ask_llm([
                {
                    "role": "user",
                    "content": prompt
                }
            ])

        else:
            # Facts Memoryの項目を取得
            answer_parts = []

            for key, value in facts.items():
                if key in question:
                    answer_parts.append(f"{key}は{value}です。")

            # 過去の計算結果を追加
            if previous_result_answer:
                answer_parts.append(previous_result_answer)

            if answer_parts:
                answer = "".join(answer_parts)
            else:
                answer = ask_llm([
                    {
                        "role": "user",
                        "content": prompt
                    }
                ])

        print("複数Memoryの統合回答：", answer)

    elif previous_calculation_request:
        answer = previous_result_answer
        print("過去の計算結果を直接回答：", answer)

    elif tool == "calculate":
        answer = str(new_tool_result)
        print("計算結果を直接回答：", answer)

    elif tool == "get_tool_logs":
        answer = str(new_tool_result)
        print("Tool履歴を直接回答：", answer)

    else:

        if (
            tool == "search_and_get_gmail_messages"
            and isinstance(new_tool_result, dict)
            and new_tool_result.get("status") == "success"
        ):

            email_messages = new_tool_result.get("messages", [])
            answer_parts = []

            for index, email in enumerate(email_messages, 1):

                headers = email.get("headers", {})

                subject = headers.get("subject", "件名なし")
                date = headers.get("date", "日付なし")
                body = email.get("body", "")

                email_prompt = f"""
あなたはAI COREです。

以下のメール1件だけを簡潔に要約してください。

【メール番号】
{index} / {len(email_messages)}

【日付】
{date}

【件名】
{subject}

【本文】
{body}

【回答ルール】
1. このメールの内容だけを要約してください。
2. 重要な情報を省略しないでください。
3. 本文にない情報を推測しないでください。
4. 日本語で簡潔に回答してください。
5. メールの件名と日付も含めてください。
"""

                summary = ask_llm([
                    {
                        "role": "user",
                        "content": email_prompt
                    }
                ])

                answer_parts.append(
                    f"【メール {index}】\n{summary}"
                )

            answer = "\n\n".join(answer_parts)

            print(
                "Gmail個別要約完了：",
                len(answer_parts),
                "/",
                len(email_messages)
            )

        else:

            llm_messages = [
                {
                    "role": "user",
                    "content": prompt
                }
            ]

            print("===== LLMへ送信するmessages =====")
            print(llm_messages)
            print("================================")

            answer = ask_llm(llm_messages)




    # =========================
    # 会話保存
    # =========================

    messages.append({
        "role": "user",
        "content": question
    })

    messages.append({
        "role": "assistant",
        "content": answer
    })

    save_memory(
        messages
    )

    return answer