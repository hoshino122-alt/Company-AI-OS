from pathlib import Path
from uuid import uuid5, NAMESPACE_URL

import requests
from qdrant_client import QdrantClient, models


class VectorStore:
    def __init__(
        self,
        storage_path="data/knowledge_base/qdrant",
        collection_name="company_knowledge",
        embedding_model="embeddinggemma:latest",
        ollama_url="http://localhost:11434",
    ):
        self.collection_name = collection_name
        self.embedding_model = embedding_model
        self.ollama_url = ollama_url.rstrip("/")
        self.client = QdrantClient(path=str(Path(storage_path)))

        if not self.client.collection_exists(self.collection_name):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=768,
                    distance=models.Distance.COSINE,
                ),
            )

    def embed(self, text):
        response = requests.post(
            f"{self.ollama_url}/api/embeddings",
            json={
                "model": self.embedding_model,
                "prompt": text,
            },
            timeout=120,
        )
        response.raise_for_status()

        vector = response.json()["embedding"]

        if len(vector) != 768:
            raise ValueError(f"Embeddingの次元数が不正です: {len(vector)}")

        return vector

    def add_documents(self, documents):
        points = []

        for document in documents:
            text = document.get("text", "").strip()
            if not text:
                continue

            point_id = str(
                uuid5(
                    NAMESPACE_URL,
                    f"{document.get('source', '')}:{document.get('chunk_index', 0)}"
                )
            )

            points.append(
                models.PointStruct(
                    id=point_id,
                    vector=self.embed(text),
                    payload={
                        "text": text,
                        "source": document.get("source", ""),
                        "filename": document.get("filename", ""),
                        "chunk_index": document.get("chunk_index", 0),
                    },
                )
            )

        if points:
            self.client.upsert(
                collection_name=self.collection_name,
                points=points,
            )

        return len(points)

    def delete_file(self, file_path):
        """指定したファイルに属する文書チャンクを削除する。"""
        source_path = str(Path(file_path).resolve())

        self.client.delete(
            collection_name=self.collection_name,
            points_selector=models.FilterSelector(
                filter=models.Filter(
                    must=[
                        models.FieldCondition(
                            key="source",
                            match=models.MatchValue(value=source_path),
                        )
                    ]
                )
            ),
        )

    def search(self, query, limit=5, min_score=0.25):
        vector = self.embed(query)

        result = self.client.query_points(
            collection_name=self.collection_name,
            query=vector,
            limit=limit,
        )

        return [
            {
                **(point.payload or {}),
                "score": point.score,
            }
            for point in result.points
            if point.score is not None and point.score >= min_score
        ]

    def close(self):
        self.client.close()
