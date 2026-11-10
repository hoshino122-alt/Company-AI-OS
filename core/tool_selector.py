import json

from core.llm import ask_llm
from core.tool_manager import get_tool_descriptions


def select_tool(question, tools):

    descriptions = get_tool_descriptions()

    tool_information = {}

    for tool in tools:
        tool_information[tool] = descriptions.get(
            tool,
            "説明なし"
        )

    prompt = f"""
あなたはAI COREのTool選択担当です。

利用可能なToolと説明：
{json.dumps(tool_information, ensure_ascii=False, indent=2)}

ユーザーの質問：
{question}

必要なToolを選択してください。

Toolが必要ない場合：
{{
    "tool": "none",
    "arguments": {{}}
}}

Toolを使用する場合は、
必ず上記の利用可能なToolから1つ選んでください。

Gmailのメールを検索する場合：

{{
    "tool": "search_gmail",
    "arguments": {{
        "query": "subject:請求書",
        "max_results": 5
    }}
}}

特定のメールの本文を取得する場合：

{{
    "tool": "get_gmail_message",
    "arguments": {{
        "message_id": "メールID"
    }}
}}

複数のメールを検索して本文を取得する場合：

{{
    "tool": "search_and_get_gmail_messages",
    "arguments": {{
        "query": "subject:請求書",
        "max_results": 2
    }}
}}

Gmail検索条件の設定ルール：

1. ユーザーが「最近のメール」「直近のメール」
   と依頼し、具体的な検索キーワードがない場合は、
   queryに "newer_than:7d" を設定してください。

2. ユーザーが検索対象の期間を指定した場合は、
   その期間に対応するGmail検索演算子を使用してください。

3. Gmail検索を実行する場合、
   queryを空文字にしてはいけません。

4. 検索条件が特定できない場合は、
   無理に空のqueryでToolを実行せず、
   toolを "none" にしてください。

Gmailの検索条件には、Gmail検索演算子を使用できます。

例：
from:example@gmail.com
subject:請求書
after:2026/10/01

現在時刻や日時が必要な場合：
{{
    "tool": "get_current_time",
    "arguments": {{}}
}}

日付だけが必要な場合：
{{
    "tool": "get_current_date",
    "arguments": {{}}
}}

PCのシステム情報が必要な場合：
{{
    "tool": "get_system_info",
    "arguments": {{}}
}}

Tool実行履歴が必要な場合：
{{
    "tool": "get_tool_logs",
    "arguments": {{}}
}}

Tool Logsの総件数が必要な場合：
{{
    "tool": "count_tool_logs",
    "arguments": {{}}
}}

ランダムな数値が必要な場合：
{{
    "tool": "generate_random_number",
    "arguments": {{
        "min_value": 1,
        "max_value": 100
    }}
}}

計算が必要な場合：
{{
    "tool": "calculate",
    "arguments": {{
        "a": 123,
        "b": 456,
        "operation": "multiply"
    }}
}}

calculateのoperationは以下だけを使用してください。

add
subtract
multiply
divide

必ずJSONだけを返してください。
"""

    answer = ask_llm([
        {
            "role": "user",
            "content": prompt
        }
    ])

    answer = answer.strip()

    # Markdownの ```json ... ``` を除去
    if answer.startswith("```"):

        lines = answer.splitlines()

        if lines[0].startswith("```"):
            lines = lines[1:]

        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        answer = "\n".join(lines)

    try:

        result = json.loads(answer)

        if not isinstance(result, dict):
            return {
                "tool": "none",
                "arguments": {}
            }

        tool = result.get("tool")

        if not isinstance(tool, str):
            return {
                "tool": "none",
                "arguments": {}
            }

        if tool != "none" and tool not in tools:
            return {
                "tool": "none",
                "arguments": {}
            }

        if "arguments" in result and not isinstance(result["arguments"], dict):
            return {
                "tool": "none",
                "arguments": {}
            }

        if "tool" not in result:

            return {
                "tool": "none",
                "arguments": {}
            }

        if "arguments" not in result:

            result["arguments"] = {}

        return result

    except json.JSONDecodeError:

        return {
            "tool": "none",
            "arguments": {}
        }