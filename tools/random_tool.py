import random


def generate_random_number(min_value, max_value):
    """指定した範囲からランダムな整数を1つ生成します。"""

    return random.randint(
        int(min_value),
        int(max_value)
    )