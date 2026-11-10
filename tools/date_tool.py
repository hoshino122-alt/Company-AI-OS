from datetime import datetime


def get_current_date():

    """現在の日付を取得します。"""
    return datetime.now().strftime("%Y-%m-%d")