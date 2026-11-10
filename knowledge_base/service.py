from pathlib import Path

from knowledge_base.document_loader import load_and_split
from knowledge_base.vector_store import VectorStore


class KnowledgeBase:
    """社内文書の登録と意味検索を管理する。"""

    def __init__(
        self,
        storage_path="data/knowledge_base/qdrant",
        collection_name="company_knowledge",
        embedding_model="embeddinggemma:latest",
    ):
        self.store = VectorStore(
            storage_path=storage_path,
            collection_name=collection_name,
            embedding_model=embedding_model,
        )

    def add_file(self, file_path):
        """指定された文書を読み込み、検索データとして登録する。"""
        documents = load_and_split(file_path)
        return self.store.add_documents(documents)

    def add_folder(self, folder_path):
        """フォルダ内の対応文書をまとめて登録する。"""
        folder = Path(folder_path)

        if not folder.exists() or not folder.is_dir():
            raise ValueError("登録対象のフォルダが見つかりません。")

        supported_extensions = {
            ".pdf", ".docx", ".txt", ".md", ".csv"
        }

        total_count = 0

        for file_path in folder.iterdir():
            if (
                file_path.is_file()
                and file_path.suffix.lower() in supported_extensions
            ):
                count = self.add_file(file_path)
                total_count += count

        return total_count

    def delete_file(self, file_path):
        """指定した文書をKnowledge Baseから削除する。"""
        self.store.delete_file(file_path)

    def update_file(self, file_path):
        """既存文書を削除して、新しい内容を登録する。"""
        documents = load_and_split(file_path)

        self.store.delete_file(file_path)

        return self.store.add_documents(documents)    
    
    def search(self, query, limit=5):
        """質問に関連する社内文書を検索する。"""
        if not isinstance(query, str) or not query.strip():
            raise ValueError("検索質問を入力してください。")

        return self.store.search(query, limit=limit)

    def close(self):
        self.store.close()
