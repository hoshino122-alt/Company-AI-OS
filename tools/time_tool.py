from datetime import datetime


def get_current_time():
    """現在の日時と時刻を取得します。"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")