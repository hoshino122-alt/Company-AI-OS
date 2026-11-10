
"""Answer validation utilities for Company AI OS."""

import re


def validate_answer(
    answer,
    required_keywords=None,
    max_length=None,
    forbidden_phrases=None,
    max_bullet_items=None,
    require_bullet_format=False,
    reject_duplicate_bullet_items=False,
):
    """
    Validate an AI employee's answer.

    Args:
        answer: The answer text to validate.
        required_keywords: Keywords that must appear in the answer.
        max_length: Optional maximum number of characters.
        forbidden_phrases: Phrases that must not appear in the answer.
        max_bullet_items: Maximum number of top-level list items.
        require_bullet_format: Whether a bullet list is required.

    Returns:
        A dictionary containing validation status and error messages.
    """
    errors = []

    if not isinstance(answer, str) or not answer.strip():
        return {
            "valid": False,
            "errors": ["回答が空、または文字列ではありません。"],
        }

    if required_keywords is not None:
        if not isinstance(required_keywords, (list, tuple)):
            raise TypeError("required_keywords must be a list or tuple.")

        for keyword in required_keywords:
            if not isinstance(keyword, str):
                raise TypeError(
                    "Each required keyword must be a string."
                )
            if not keyword.strip():
                raise ValueError(
                    "Required keywords must not be empty."
                )

        missing_keywords = [
            keyword
            for keyword in required_keywords
            if keyword not in answer
        ]

        if missing_keywords:
            errors.append(
                "必須キーワードが不足しています: "
                + ", ".join(missing_keywords)
            )

    if forbidden_phrases is not None:
        if not isinstance(forbidden_phrases, (list, tuple)):
            raise TypeError("forbidden_phrases must be a list or tuple.")

        for phrase in forbidden_phrases:
            if not isinstance(phrase, str):
                raise TypeError(
                    "Each forbidden phrase must be a string."
                )
            if not phrase.strip():
                raise ValueError(
                    "Forbidden phrases must not be empty."
                )

        found_phrases = [
            phrase
            for phrase in forbidden_phrases
            if phrase in answer
        ]

        if found_phrases:
            errors.append(
                "禁止フレーズが含まれています: "
                + ", ".join(found_phrases)
            )

    if max_length is not None:
        if (
            not isinstance(max_length, int)
            or isinstance(max_length, bool)
            or max_length < 1
        ):
            raise ValueError("max_length must be a positive integer.")

        if len(answer) > max_length:
            errors.append(
                f"回答が最大文字数を超えています: "
                f"{len(answer)}文字 > {max_length}文字"
            )

    if not isinstance(require_bullet_format, bool):
        raise ValueError(
            "require_bullet_format must be a boolean."
        )

    if require_bullet_format and max_bullet_items is None:
        raise ValueError(
            "max_bullet_items is required when "
            "require_bullet_format=True."
        )

    if max_bullet_items is not None:
        if (
            not isinstance(max_bullet_items, int)
            or isinstance(max_bullet_items, bool)
            or max_bullet_items < 1
        ):
            raise ValueError(
                "max_bullet_items must be a positive integer."
            )

    if require_bullet_format:
        has_top_level_bullet = any(
            line
            and not line[0].isspace()
            and re.match(r"^(?:[-*+]|\d+[.)])\s+", line)
            for line in answer.splitlines()
        )

        if not has_top_level_bullet:
            errors.append(
                "回答に最上位の箇条書き項目がありません。"
            )

    if max_bullet_items is not None:
        top_level_items = []

        for line in answer.splitlines():
            if not line or line[0].isspace():
                continue

            if re.match(r"^(?:[-*+]|\d+[.)])\s+", line):
                top_level_items.append(line)

        if len(top_level_items) > max_bullet_items:
            errors.append(
                "最上位の箇条書き項目数が上限を超えています: "
                f"{len(top_level_items)}項目 > "
                f"{max_bullet_items}項目"
            )


    if not isinstance(reject_duplicate_bullet_items, bool):
        raise ValueError(
            "reject_duplicate_bullet_items must be a boolean."
        )

    if reject_duplicate_bullet_items:
        seen_bullet_items = set()

        for line in answer.splitlines():
            if not line or line[0].isspace():
                continue

            match = re.match(
                r"^(?:[-*+]|\d+[.)])\s+(.+)$",
                line,
            )

            if not match:
                continue

            item = match.group(1).strip()

            if item in seen_bullet_items:
                errors.append(
                    f"箇条書き項目が重複しています: {item}"
                )
            else:
                seen_bullet_items.add(item)



    return {
        "valid": not errors,
        "errors": errors,
    }
