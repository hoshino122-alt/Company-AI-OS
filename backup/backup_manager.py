
import hashlib
import json
import shutil
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

BACKUP_ROOT = (
    Path.home()
    / "Desktop"
    / "Company-AI-OS-Backups"
)

MEMORY_TARGETS = [
    PROJECT_ROOT / "memory.json",
    PROJECT_ROOT / "memory" / "facts.json",
]

QDRANT_SOURCE = (
    PROJECT_ROOT / "data"
    / "knowledge_base"
    / "qdrant"
)


def calculate_sha256(file_path):
    """Calculate SHA256 hash of a file."""
    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def verify_file(source, destination):
    """Compare source and backup using SHA256."""
    source_hash = calculate_sha256(source)
    backup_hash = calculate_sha256(destination)

    if source_hash != backup_hash:
        raise RuntimeError(
            f"SHA256照合失敗: {source}"
        )

    print(f"SHA256 OK: {source.name}")


def create_backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_dir = BACKUP_ROOT / f"backup_{timestamp}"

    backup_dir.mkdir(parents=True, exist_ok=False)

    print("バックアップを開始します。")

    # =========================
    # Memory Backup
    # =========================

    print("\n=== Memory Backup ===")

    for source in MEMORY_TARGETS:

        if not source.is_file():
            raise FileNotFoundError(
                f"バックアップ対象が見つかりません: {source}"
            )

        # コピー前のJSON検証
        with source.open("r", encoding="utf-8") as file:
            json.load(file)

        relative_path = source.relative_to(PROJECT_ROOT)
        destination = backup_dir / relative_path

        destination.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.copy2(source, destination)

        # コピー後のJSON検証
        with destination.open("r", encoding="utf-8") as file:
            json.load(file)

        verify_file(source, destination)

        print(f"保存完了: {relative_path}")

    # =========================
    # Qdrant Backup
    # =========================

    print("\n=== Qdrant Backup ===")

    if not QDRANT_SOURCE.is_dir():
        raise FileNotFoundError(
            f"Qdrant保存先が見つかりません: {QDRANT_SOURCE}"
        )

    qdrant_relative = QDRANT_SOURCE.relative_to(PROJECT_ROOT)

    qdrant_destination = backup_dir / qdrant_relative

    shutil.copytree(
        QDRANT_SOURCE,
        qdrant_destination
    )

    source_files = sorted(
        path for path in QDRANT_SOURCE.rglob("*")
        if path.is_file()
    )

    backup_files = sorted(
        path for path in qdrant_destination.rglob("*")
        if path.is_file()
    )

    if len(source_files) != len(backup_files):
        raise RuntimeError(
            "Qdrantのファイル数が一致しません。"
        )

    for source in source_files:

        relative_path = source.relative_to(QDRANT_SOURCE)
        destination = qdrant_destination / relative_path

        if not destination.is_file():
            raise FileNotFoundError(
                f"Qdrantバックアップファイルがありません: {relative_path}"
            )

        verify_file(source, destination)

    print(f"Qdrant保存ファイル数: {len(source_files)}")

    # =========================
    # Completed
    # =========================

    print("\n================================")
    print("バックアップが完了しました。")
    print(f"保存先: {backup_dir}")
    print("Memory: JSON検証・SHA256照合 OK")
    print("Qdrant: SHA256照合 OK")
    print("================================")


if __name__ == "__main__":
    create_backup()
