import json

from core.llm import ask_llm


def select_memory(question):

    question_lower = question.lower()

    memories = []

    # =========================
    # Tool履歴
    # =========================

    tool_keywords = [
    "tool_logs",
    "tool履歴",
    "ツール履歴",
    "実行履歴",
    "直前に実行したtool",
    "直近のtool",
    "直前のtool",
    "直近に実行したtool",
    "ランダムな数字",
    "ランダムの結果",
    "生成された数字",
    "generate_random_number",

    # 計算
    "計算",
    "以前の計算結果",
    "過去の計算結果",
    "以前の計算",
    "過去の計算",
    "計算してください",
    "掛け算",
    "足し算",
    "引き算",
    "割り算",
    "calculate",

    # 時刻・日付
    "時刻",
    "現在時刻",
    "時間",
    "日付",
    "今日の日付",

    # システム情報
    "pc",
    "システム情報",
    "get_system_info"
]

    for keyword in tool_keywords:

        if keyword in question_lower:

            if "tool_logs" not in memories:
                memories.append("tool_logs")

            break

    # =========================
    # Conversation
    # =========================

    conversation_keywords = [
        "さっき",
        "先ほど",
        "直前",
        "直近",
        "今の",
        "今さっき",
        "何を話した",
        "何をテスト",
        "話していた",
        "言っていた"
    ]

    for keyword in conversation_keywords:

        if keyword in question_lower:

            if "conversation" not in memories:
                memories.append("conversation")

            break

    # =========================
    # Development History
    # =========================

    development_keywords = [
        "開発履歴",
        "development history",
        "development_history",
        "開発変更",
        "コード変更",
        "何を変更した",
        "何を変更しました",
        "何を修正しました",
        "何を実装しました",
        "何を修正した",
        "何を実装した",
        "いつ変更した",
        "変更内容",
        "開発で変更",
        "実装履歴"
    ]

    for keyword in development_keywords:

        if keyword in question_lower:

            if "development_history" not in memories:
                memories.append("development_history")

            if "conversation" in memories:
                memories.remove("conversation")

            break

    # =========================
    # Facts
    # =========================

    fact_keywords = [
        "私の名前",
        "名前",
        "好きな色",
        "好きな食べ物",
        "会社名",
        "覚えている",

        # Company AI OS
        "company ai os",
        "company ai",
        "ai os",
        "ai core",
        "目的",
        "主要機能",
        "役割",
        "ai社員",
        "ai社長",
        "ai秘書",
        "部門管理",
        "タスク管理",
        "workflow",
        "ローカルllm",
        "rag"
    ]

    for keyword in fact_keywords:

        if keyword in question_lower:

            if "facts" not in memories:
                memories.append("facts")

            break

    # =========================
    # Knowledge Base
    # =========================

    knowledge_keywords = [
        "社内文書",
        "社内資料",
        "社内規程",
        "業務マニュアル",
        "会社の資料",
        "登録文書",
        "保存文書",
        "文書を検索",
        "資料を検索",
        "文書に書かれている",
        "資料に書かれている",
        "ナレッジベース",
        "knowledge base",
        "社内ナレッジ",

        # Company AI OSの構成要素
        "taskstore",
        "workflowengine",
        "corerunner",
        "planner",
        "executor",
        "task"      
    ]

    for keyword in knowledge_keywords:

        if keyword in question_lower:

            if "knowledge_base" not in memories:
                memories.append("knowledge_base")

            break


    # =========================
    # キーワードでMemoryが決まった場合
    # =========================

    if memories:

        return {
            "memories": memories
        }

    # =========================
    # LLMによるMemory選択
    # =========================

    prompt = f"""
あなたはAI COREのMemory選択担当です。

ユーザーの質問：
{question}

利用可能なMemory：

- conversation
  過去の会話を検索する

- facts
  保存された重要情報を使用する

- tool_logs
  過去に実行したToolの履歴を検索する

- knowledge_base
  社内文書・業務マニュアル・登録資料を検索する 

ルール：

1つの質問の中に複数の要求が含まれている場合は、
それぞれの要求に必要なMemoryをすべて選択してください。

例えば、

「私がさっきテストしていた内容と、
以前のランダムな数字の結果を教えてください」

の場合は、

{{
    "memories": ["conversation", "tool_logs"]
}}

を返してください。

必要なMemoryが1つだけの場合は、
そのMemoryだけを選択してください。

必要なMemoryがない場合は、

{{
    "memories": []
}}

を返してください。

必ずJSONだけを返してください。
"""

    answer = ask_llm([
        {
            "role": "user",
            "content": prompt
        }
    ])

    answer = answer.strip()

    if answer.startswith("```"):

        lines = answer.splitlines()

        if lines[0].startswith("```"):
            lines = lines[1:]

        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        answer = "\n".join(lines)

    try:

        result = json.loads(answer)

        if "memories" not in result:
            return {
                "memories": []
            }

        if not isinstance(result["memories"], list):
            return {
                "memories": []
            }

        return result

    except json.JSONDecodeError:

        return {
            "memories": []
        }