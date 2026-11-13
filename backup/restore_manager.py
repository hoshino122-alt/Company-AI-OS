import hashlib
import json
import shutil
from datetime import datetime
from pathlib import Path


BACKUP_SOURCE = (
    Path.home()
    / "Desktop"
    / "Company-AI-OS-Backups"
    / "backup_20261113_112243"
)

RESTORE_ROOT = (
    Path.home()
    / "Desktop"
    / "Company-AI-OS-Restore-Test"
)


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def restore_backup():

    if not BACKUP_SOURCE.is_dir():
        raise FileNotFoundError(
            f"バックアップが見つかりません: {BACKUP_SOURCE}"
        )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    restore_dir = RESTORE_ROOT / f"restore_{timestamp}"
    restore_dir.mkdir(parents=True, exist_ok=False)

    print("テスト復元を開始します。")

    # Memory復元
    print("\n=== Memory Restore ===")

    memory_files = [
        Path("memory.json"),
        Path("memory/facts.json"),
    ]

    for relative_path in memory_files:

        source = BACKUP_SOURCE / relative_path
        destination = restore_dir / relative_path

        if not source.is_file():
            raise FileNotFoundError(source)

        with source.open("r", encoding="utf-8") as file:
            json.load(file)

        destination.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.copy2(source, destination)

        with destination.open("r", encoding="utf-8") as file:
            json.load(file)

        if calculate_sha256(source) != calculate_sha256(destination):
            raise RuntimeError(
                f"Memory復元検証失敗: {relative_path}"
            )

        print(f"復元・検証 OK: {relative_path}")

    # Qdrant復元
    print("\n=== Qdrant Restore ===")

    qdrant_relative = Path(
        "data/knowledge_base/qdrant"
    )

    qdrant_source = BACKUP_SOURCE / qdrant_relative
    qdrant_destination = restore_dir / qdrant_relative

    if not qdrant_source.is_dir():
        raise FileNotFoundError(qdrant_source)

    shutil.copytree(
        qdrant_source,
        qdrant_destination
    )

    source_files = sorted(
        path for path in qdrant_source.rglob("*")
        if path.is_file()
    )

    for source in source_files:

        relative_path = source.relative_to(qdrant_source)
        destination = qdrant_destination / relative_path

        if not destination.is_file():
            raise FileNotFoundError(destination)

        if calculate_sha256(source) != calculate_sha256(destination):
            raise RuntimeError(
                f"Qdrant復元検証失敗: {relative_path}"
            )

        print(f"SHA256 OK: {relative_path}")

    print("\n================================")
    print("テスト復元が完了しました。")
    print(f"復元先: {restore_dir}")
    print("Memory: JSON検証・SHA256照合 OK")
    print(f"Qdrant: {len(source_files)}ファイル検証 OK")
    print("本番データは変更していません。")
    print("================================")


if __name__ == "__main__":
    restore_backup()