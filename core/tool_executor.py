import os

from core.tool_manager import run_tool
from datetime import datetime
from tools.gmail_tool import (
    search_gmail,
    get_gmail_message,
    search_and_get_gmail_messages
)


def save_tool_log(tool, arguments, result):

    os.makedirs("logs", exist_ok=True)

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    log_line = (
        f"{timestamp} | "
        f"{tool} | "
        f"{arguments} | "
        f"{result}\n"
    )

    with open(
        "logs/tool.log",
        "a",
        encoding="utf-8"
    ) as f:

        f.write(log_line)

def log_tool(tool, arguments, result):

    print()
    print("[TOOL EXECUTION]")
    print(f"Tool   : {tool}")
    print(f"Args   : {arguments}")
    print(f"Result : {result}")
    print()

    save_tool_log(
        tool,
        arguments,
        result
    )


def execute_tool(tool, arguments):

    if tool == "get_current_time":

        result = run_tool("get_current_time")

        log_tool(
            tool,
            arguments,
            result
        )

        return result


    if tool == "get_current_date":

        result = run_tool("get_current_date")

        log_tool(
            tool,
            arguments,
            result
        )

        return result


    if tool == "get_system_info":

        result = run_tool("get_system_info")

        log_tool(
            tool,
            arguments,
            result
        )

        return result

    if tool == "count_tool_logs":

        result = run_tool("count_tool_logs")

        # ログ件数取得Tool自身はログに記録しない
        return result


    if tool == "get_tool_logs":

        limit = arguments.get("limit", 10)
        tool_name = arguments.get("tool_name")

        print("get_tool_logs に渡す limit:", limit)
        print("get_tool_logs に渡す tool_name:", tool_name)

        result = run_tool(
            "get_tool_logs",
            limit,
            tool_name=tool_name
        )

        # ログ閲覧Tool自身はログに記録しない
        return result




    if tool == "generate_random_number":

        try:
            min_value = int(arguments["min_value"])
            max_value = int(arguments["max_value"])

        except (KeyError, TypeError, ValueError):

            result = "ランダム数生成Toolの引数が正しくありません。"

            log_tool(
                tool,
                arguments,
                result
            )

            return result

        if min_value > max_value:

            result = "最小値は最大値以下にしてください。"

            log_tool(
                tool,
                arguments,
                result
            )

            return result

        result = run_tool(
            "generate_random_number",
            min_value,
            max_value
        )

        log_tool(
            tool,
            arguments,
            result
        )

        return result


    if tool == "calculate":

        try:
            a = float(arguments["a"])
            b = float(arguments["b"])
            operation = arguments["operation"]

        except (KeyError, TypeError, ValueError):

            result = "計算Toolに必要な引数が正しくありません。"

            log_tool(
                tool,
                arguments,
                result
            )

            return result

        allowed_operations = {
            "add",
            "subtract",
            "multiply",
            "divide"
        }

        if operation not in allowed_operations:

            result = "許可されていない計算方法です。"

            log_tool(
                tool,
                arguments,
                result
            )

            return result

        result = run_tool(
            "calculate",
            a,
            b,
            operation
        )

        if isinstance(result, float) and result.is_integer():

            result = f"{int(result):,}"

        else:

            result = str(result)

        log_tool(
            tool,
            arguments,
            result
        )

        return result


    if tool == "search_gmail":

        query = arguments.get("query", "")
        max_results = arguments.get("max_results", 5)

        if not isinstance(query, str) or not query.strip():
            result = "Gmail検索キーワードを指定してください。"

        else:
            try:
                max_results = int(max_results)

                if not 1 <= max_results <= 20:
                    raise ValueError

                result = search_gmail(
                    query,
                    max_results
                )

            except (TypeError, ValueError):
                result = "検索件数は1〜20の整数で指定してください。"

        log_result = {
            "status": result.get("status", "error"),
            "count": result.get("count", 0)
        } if isinstance(result, dict) else "検索エラーまたは入力エラー"

        log_tool(
            tool,
            {"max_results": max_results},
            log_result
        )

        return result


    if tool == "get_gmail_message":

        message_id = arguments.get("message_id", "")

        if not isinstance(message_id, str) or not message_id.strip():
            result = "メールIDを指定してください。"

        else:
            result = get_gmail_message(message_id)

        log_result = {
            "status": result.get("status", "error")
        } if isinstance(result, dict) else "取得エラーまたは入力エラー"

        log_tool(
            tool,
            {"message_id": message_id},
            log_result
        )

        return result

    if tool == "search_and_get_gmail_messages":

        query = arguments.get("query", "")
        max_results = arguments.get("max_results", 2)

        if not isinstance(query, str) or not query.strip():
            result = {
                "status": "error",
                "message": "Gmail検索キーワードを指定してください。"
            }

        else:
            try:
                max_results = int(max_results)

                if not 1 <= max_results <= 5:
                    raise ValueError

                result = search_and_get_gmail_messages(
                    query,
                    max_results
                )

            except (TypeError, ValueError):
                result = {
                    "status": "error",
                    "message": "取得件数は1〜5の整数で指定してください。"
                }

        log_result = {
            "status": result.get("status", "error"),
            "count": result.get("count", 0)
        }

        log_tool(
            tool,
            {"max_results": max_results},
            log_result
        )

        return result

    result = "未登録のToolです。"

    log_tool(
        tool,
        arguments,
        result
    )

    return result