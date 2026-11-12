import json
import os


MEMORY_FILE = "memory.json"
FACTS_FILE = "memory/facts.json"
DEVELOPMENT_HISTORY_FILE = "memory/development_history.json"

def load_development_history():

    if os.path.exists(DEVELOPMENT_HISTORY_FILE):

        with open(
            DEVELOPMENT_HISTORY_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    return []

def save_development_history(history):

    with open(
        DEVELOPMENT_HISTORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            history,
            f,
            ensure_ascii=False,
            indent=2
        )

def add_development_history(entry):

    history = load_development_history()

    history.append(entry)

    save_development_history(history)

    return True

def update_development_history(
    history_id,
    syntax_check=None,
    execution_test=None,
    status=None
):

    history = load_development_history()

    for entry in history:

        if entry.get("id") == history_id:

            if syntax_check is not None:
                entry["syntax_check"] = syntax_check

            if execution_test is not None:
                entry["execution_test"] = execution_test

            if status is not None:
                entry["status"] = status

            save_development_history(history)

            return True

    return False

def search_development_history(keyword="", limit=10):

    history = load_development_history()

    if not keyword:
        return history[-limit:]

    keyword_lower = keyword.lower()

    results = []

    for entry in reversed(history):

        entry_text = json.dumps(
            entry,
            ensure_ascii=False
        ).lower()

        if keyword_lower in entry_text:

            results.append(entry)

        if len(results) >= limit:
            break

    return list(reversed(results))

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    return []


def save_memory(messages):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)



def search_memory(messages, keyword, limit=10):

    keyword_lower = keyword.lower()

    # =========================
    # 重複排除用の共通処理
    # =========================

    def remove_duplicates(items):

        unique = []
        seen = set()

        for message in items:

            content = message.get(
                "content", ""
            ).strip()

            if not content or content in seen:
                continue

            seen.add(content)
            unique.append(message)

        return unique

    # =========================
    # 直前の会話を参照する質問
    # =========================

    recent_keywords = [
        "さっき",
        "先ほど",
        "直前",
        "直近",
        "今の",
        "今さっき",
        "以前"
    ]

    is_recent_question = any(
        word in keyword_lower
        for word in recent_keywords
    )

    if is_recent_question:

        # =========================
        # 質問から検索対象キーワードを抽出
        # =========================

        target_terms = [
            "合言葉",
            "名前",
            "好きな色",
            "好きな食べ物",
            "好きな動物",
            "会社名",
            "計算結果",
            "ランダムな数字",
            "設計",
            "目的",
            "テスト",
            "conversation memory"
        ]

        targets = [
            term for term in target_terms
            if term in keyword_lower
        ]

        change_terms = [
            "変更",
            "改善",
            "修正"
        ]

        is_change_question = any(
            term in keyword_lower
            for term in change_terms
        )

        # =========================
        # 現在の質問を除外
        # =========================

        current_question = keyword.strip()

        # =========================
        # userとassistantの会話ペアを取得
        # =========================

        results = []

        recent_pair_count = 0

        for i in range(len(messages) - 1, 0, -1):

            user_message = messages[i - 1]
            assistant_message = messages[i]

            if user_message.get("role") != "user":
                continue

            if assistant_message.get("role") != "assistant":
                continue

            recent_pair_count += 1

            if recent_pair_count > 10:
                break

            user_content = user_message.get(
                "content", ""
            ).strip()

            assistant_content = assistant_message.get(
                "content", ""
            ).strip()

            if not user_content or not assistant_content:
                continue

            # 現在の質問を除外
            if user_content == current_question:
                continue

            # =========================
            # 話題と質問意図の一致を確認
            # =========================

            combined_content = (
                user_content + " " + assistant_content
            ).lower()

            # 話題の一致
            if targets:

                if not all(
                    term in combined_content
                    for term in targets
                ):
                    continue

            # 変更・改善・修正の意図
            if is_change_question:

                user_content_lower = user_content.lower()

                if not any(
                    term in user_content_lower
                    for term in change_terms
                ):
                    continue

            results.append(user_message)
            results.append(assistant_message)


        return results
    # =========================
    # 通常のConversation検索
    # =========================

    results = []

    for message in reversed(messages):

        if message.get("role") != "user":
            continue

        content = message.get(
            "content", ""
        ).strip()

        if content == keyword.strip():
            continue

        if keyword_lower in content.lower():

            results.append(message)

    # 重複を除外
    results = remove_duplicates(results)

    # 最新順から古い順へ戻す
    results = list(reversed(results))

    return results[:limit]


def load_facts():
    if os.path.exists(FACTS_FILE):
        with open(FACTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    return {}


def save_fact(key, value):
    facts = load_facts()
    facts[key] = value

    with open(FACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(facts, f, ensure_ascii=False, indent=2)

def save_fact(key, value):
    facts = load_facts()
    facts[key] = value

    with open(FACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(facts, f, ensure_ascii=False, indent=2)

def delete_fact(key):
    facts = load_facts()

    if key not in facts:
        return False

    del facts[key]

    with open(FACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(facts, f, ensure_ascii=False, indent=2)

    facts_after_save = load_facts()

    return key not in facts_after_save

def remember_fact(text):

    # 記憶指示の判定
    remember_phrases = [
        "覚えてください",
        "覚えて下さい",
        "記憶してください",
        "記憶して下さい"
    ]

    if not any(
        phrase in text
        for phrase in remember_phrases
    ):
        return False

    # 最初の一文だけを取得
    first_sentence = text.split("。", 1)[0].strip()

    if "は" not in first_sentence:
        return False

    # キーと値を分離
    key, value = first_sentence.split("は", 1)

    key = key.strip().replace("私の", "")
    value = value.strip()

    # 文末の整理
    if value.endswith("です"):
        value = value[:-2].strip()

    value = value.rstrip("。.!！?？ ")

    if not key or not value:
        return False

    print("===== FACTS MEMORY DEBUG =====")
    print("実行ファイル:", __file__)
    print("保存先:", os.path.abspath(FACTS_FILE))

    # Facts Memoryへ保存・上書き
    save_fact(key, value)

    print("保存後の内容:", load_facts())
    print("==============================")

    return True

def search_tool_logs(keyword="", limit=10):

    log_file = "logs/tool.log"

    if not os.path.exists(log_file):
        return []

    results = []

    with open(
        log_file,
        "r",
        encoding="utf-8"
    ) as f:

        lines = f.readlines()

    keyword = keyword.lower()

    for line in reversed(lines):

        line = line.strip()

        if not line:
            continue

        # 古い get_tool_logs の入れ子ログを除外
        if " | get_tool_logs | " in line:
            continue

        # キーワードが指定されている場合だけ検索
        if keyword and keyword not in line.lower():
            continue

        results.append(line)

        if len(results) >= limit:
            break

    return list(reversed(results))


def search_tool_logs_by_keywords(keywords, limit=None):

    if keywords is None:
        return []

    log_file = "logs/tool.log"

    if not os.path.exists(log_file):
        return []

    results = []

    with open(
        log_file,
        "r",
        encoding="utf-8"
    ) as f:

        lines = f.readlines()

    # ログファイルを新しい順に処理する
    for line in reversed(lines):

        line = line.strip()

        if not line:
            continue

        # 古い入れ子ログを除外
        if " | get_tool_logs | " in line:
            continue

        line_lower = line.lower()

        for keyword in keywords:

            if keyword.lower() in line_lower:

                results.append(line)

                break

        # limitが指定されている場合だけ件数制限
        if limit is not None and len(results) >= limit:
            break

    # 表示時は古い順に戻す
    results.reverse()

    return results

