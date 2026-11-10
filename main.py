
from core.core import process
from workflow.application import WorkflowApplication


def run_conversation():
    print("\n=== 通常会話モード ===")
    print("終了する場合は exit と入力してください。")
    print("複数行入力の場合は、最後に空行を入力してください。")

    while True:

        lines = []

        first_line = input("\n質問：")

        if first_line.strip().lower() == "exit":
            break

        if not first_line.strip():
            continue

        lines.append(first_line)

        while True:
            line = input()

            if not line.strip():
                break

            lines.append(line)

        question = "\n".join(lines).strip()

        answer = process(question)
        print(answer)


def run_business_workflow():
    print("\n=== 業務実行モード ===")

    request = input("\n業務依頼：").strip()

    mode = input(
        "\n処理モードを選択してください。\n"
        "1. 通常業務\n"
        "2. Knowledge Base資料調査\n"
        "選択："
    ).strip()

    if mode not in ("1", "2"):
        print("1または2を選択してください。")
        return

    is_research = mode == "2"

    if not request:
        print("業務依頼が入力されていません。")
        return

    tasks = [
        {
            "name": "Planner：企画・方針の整理",
            "description": "業務依頼の目的、課題、実現方針、優先順位を整理する。資料調査の場合は、資料に明記された事実と資料に記載されていない情報を区別する",
            "input_data": {
                "employee_id": "planner",

                "instructions": (
                    (
                        "Knowledge Baseに登録された資料だけを根拠にしてください。\n"
                        "資料に明確に記載された事実と、資料に記載されていない情報を区別してください。\n"
                        "資料に記載されていない情報は推測で補わず、「資料に記載なし」としてください。\n"
                        "一般知識による補足や、資料にない処理手順・内部動作の創作は禁止します。\n"
                        "前提や関係性を推測で確定しないでください。"
                    ) if is_research else ""
                ),

                "question": (
                    "次の業務依頼について、目的・課題・実現方針・"
                    "優先順位を整理してください。\n\n"
                    f"【業務依頼】\n{request}"
                ),
            },
        },
        {
            "name": "Executor：成果物の作成",
            "description": "Plannerの結果を踏まえて具体的な成果物を作成する",
            "input_data": {
                "employee_id": "executor",

                "instructions": (
                    (
                        "Knowledge Baseに登録された資料を根拠として最終回答を作成してください。\n"
                        "前のTaskの結果は未検証の参考情報として扱い、事実としてそのまま採用しないでください。\n"
                        "資料に明確に記載された事実だけを確定情報として記述してください。\n"
                        "資料に記載されていない情報は推測で補わず、「資料に記載なし」と明記してください。\n"
                        "一般知識による補足や、資料にない処理手順・内部動作の創作は禁止します。\n"
                        "資料から確認できない関係性や動作を断定しないでください。\n"
                        "参照したファイル名を最後に記載してください。"
                    ) if is_research else ""
                ),

                "question": (
                    "前のTaskの企画結果を踏まえ、"
                    "次の業務依頼に対する具体的な成果物を作成してください。\n\n"
                    f"【業務依頼】\n{request}"
                ),
            },
        },
    ]

    application = WorkflowApplication()
    result = application.run(tasks)

    print("\n=== WORKFLOW RESULT ===")
    print(f"Status: {result['status']}")

    if result.get("workflow_id"):
        print(f"Workflow ID: {result['workflow_id']}")

    if result["status"] == "completed":
        final_result = result.get("final_result") or {}
        print("\n=== 最終成果物 ===")
        print(final_result.get("answer", "回答がありません。"))

    elif result["status"] == "paused":
        print("\nWorkflowは一時停止しました。")
        print(f"理由: {result.get('error')}")


def main():
    print("================================")
    print("       Company AI OS 1.0")
    print("================================")

    while True:
        print("\n1. 通常会話")
        print("2. 業務実行（Planner → Executor）")
        print("3. 終了")

        choice = input("\nモードを選択してください：").strip()

        if choice == "1":
            run_conversation()

        elif choice == "2":
            run_business_workflow()

        elif choice == "3":
            print("Company AI OSを終了します。")
            break

        else:
            print("1、2、3のいずれかを選択してください。")


if __name__ == "__main__":
    main()
