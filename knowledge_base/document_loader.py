from pathlib import Path
import csv

SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".txt", ".md", ".csv"}


def load_document(file_path):
    """PDF / Word / TXT / Markdown / CSVからテキストを読み込む。"""
    path = Path(file_path)


    if not path.is_file():
        raise FileNotFoundError(f"ファイルが見つかりません: {path}")

    suffix = path.suffix.lower()

    if suffix not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"未対応のファイル形式です: {suffix}")

    if suffix == ".pdf":
        from pypdf import PdfReader

        reader = PdfReader(str(path))
        pages = [page.extract_text() or "" for page in reader.pages]
        text = "\n\n".join(pages)

    elif suffix == ".docx":
        from docx import Document

        document = Document(str(path))
        paragraphs = [p.text for p in document.paragraphs if p.text.strip()]
        text = "\n".join(paragraphs)

    else:
        try:
            text = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            text = path.read_text(encoding="cp932")

    if not text.strip():
        raise ValueError(f"文書からテキストを取得できませんでした: {path.name}")

    return text


def split_text(text, chunk_size=1000, overlap=150):
    """テキストを重複部分を持たせながら分割する。"""
    if not isinstance(text, str):
        raise TypeError("textは文字列で指定してください。")

    if chunk_size <= 0:
        raise ValueError("chunk_sizeは1以上にしてください。")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlapは0以上、chunk_size未満にしてください。")

    text = text.strip()
    if not text:
        return []

    chunks = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))

        if end < len(text):
            boundary = text.rfind("\n", start, end)
            if boundary > start + chunk_size // 2:
                end = boundary

        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)

        if end >= len(text):
            break

        start = end - overlap

    return chunks


def load_and_split(file_path, chunk_size=1000, overlap=150):
    """文書を読み込み、検索用チャンクと基本情報を返す。"""
    path = Path(file_path)
    text = load_document(path)
    chunks = split_text(text, chunk_size, overlap)

    return [
        {
            "text": chunk,
            "source": str(path.resolve()),
            "filename": path.name,
            "chunk_index": index,
        }
        for index, chunk in enumerate(chunks)
    ]
