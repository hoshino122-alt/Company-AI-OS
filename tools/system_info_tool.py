import platform
import os


def get_system_info():

    """PCの基本的なシステム情報を取得します。"""

    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": os.cpu_count(),
    }