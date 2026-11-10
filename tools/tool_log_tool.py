
def get_tool_logs(limit=10, tool_name=None):
    """AI COREのTool実行履歴を取得します。"""

    try:
        with open(
            "logs/tool.log",
            "r",
            encoding="utf-8"
        ) as f:
            logs = f.readlines()

    except FileNotFoundError:
        return "Tool実行ログはまだありません。"

    if not logs:
        return "Tool実行ログはまだありません。"

    # 指定されたToolだけに絞り込む
    if tool_name:
        filtered_logs = []

        for line in logs:
            parts = line.strip().split(" | ", 3)

            if len(parts) != 4:
                continue

            if parts[1] == tool_name:
                filtered_logs.append(line)

        logs = filtered_logs

    if not logs:
        return f"{tool_name}の実行履歴はありません。"

    # 取得件数を指定する
    limit = max(1, int(limit))

    return "".join(logs[-limit:])

def count_tool_logs():
    """保存されているTool実行ログの総件数を取得します。"""

    try:
        with open(
            "logs/tool.log",
            "r",
            encoding="utf-8"
        ) as f:
            logs = f.readlines()

    except FileNotFoundError:
        return 0

    return sum(1 for line in logs if line.strip())

