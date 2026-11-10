
import math


def calculate(a, b, operation):
    """2つの数値を指定された演算方法で計算します。"""

    # NaN・Infinityなど、有限でない数値を拒否
    if not math.isfinite(a) or not math.isfinite(b):
        return "有限の数値を指定してください。"

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            return "0では割れません。"

        return a / b

    else:
        return "不明な計算方法です。"
