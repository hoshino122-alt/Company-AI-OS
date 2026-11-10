
import os
import base64
import re
import html

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


# Gmail読み取り専用
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# Company AI OSのプロジェクト直下
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

CREDENTIALS_FILE = os.path.join(
    BASE_DIR,
    "credentials.json"
)

TOKEN_FILE = os.path.join(
    BASE_DIR,
    "token.json"
)


def _get_gmail_service():
    """Gmail APIの認証を行い、サービスを取得します。"""

    if not os.path.exists(CREDENTIALS_FILE):
        raise FileNotFoundError(
            "credentials.json が見つかりません。"
        )

    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(
            TOKEN_FILE,
            SCOPES
        )

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

    if not creds or not creds.valid:

        flow = InstalledAppFlow.from_client_secrets_file(
            CREDENTIALS_FILE,
            SCOPES
        )

        creds = flow.run_local_server(
            port=0,
            open_browser=True
        )

    with open(TOKEN_FILE, "w", encoding="utf-8") as token:
        token.write(creds.to_json())

    return build(
        "gmail",
        "v1",
        credentials=creds
    )

def _test_gmail_connection():
    """Gmail APIへの接続を確認します。"""

    try:
        service = _get_gmail_service()

        profile = service.users().getProfile(
            userId="me"
        ).execute()

        return {
            "status": "success",
            "email": profile.get("emailAddress"),
            "messages_total": profile.get("messagesTotal")
        }

    except Exception as exc:
        return {
            "status": "error",
            "message": str(exc)
        }


def search_gmail(query, max_results=5):
    """Gmailを検索してメール一覧を取得します。"""

    try:
        service = _get_gmail_service()

        results = service.users().messages().list(
            userId="me",
            q=query,
            maxResults=max_results
        ).execute()

        messages = results.get("messages", [])

        return {
            "status": "success",
            "count": len(messages),
            "messages": messages
        }

    except Exception as exc:
        return {
            "status": "error",
            "message": str(exc)
        }


def get_gmail_message(message_id):
    """指定されたメールの本文と基本情報を取得します。"""

    try:
        service = _get_gmail_service()

        message = service.users().messages().get(
            userId="me",
            id=message_id,
            format="full"
        ).execute()

        headers = message.get("payload", {}).get("headers", [])

        email_info = {}

        for header in headers:
            name = header.get("name", "").lower()

            if name in ["from", "to", "subject", "date"]:
                email_info[name] = header.get("value", "")

        return {
            "status": "success",
            "message_id": message_id,
            "headers": email_info,
            "snippet": message.get("snippet", ""),
            "body": _decode_gmail_body(
                message.get("payload", {})
            )
        }

    except Exception as exc:
        return {
            "status": "error",
            "message": str(exc)
        }



import re
import html


def _decode_gmail_body(payload):
    """GmailのMIMEデータから読みやすいテキスト本文を取り出します。"""

    mime_type = payload.get("mimeType", "")

    # multipart形式の場合
    if "parts" in payload:

        plain_text = ""
        html_text = ""

        for part in payload["parts"]:

            result = _decode_gmail_body(part)

            if not result:
                continue

            if part.get("mimeType") == "text/plain":
                plain_text += result + "\n"

            else:
                html_text += result + "\n"

        return html_text.strip() or plain_text.strip()

    # 本文データを取得
    body_data = payload.get(
        "body", {}
    ).get("data")

    if not body_data:
        return ""

    decoded_bytes = base64.urlsafe_b64decode(body_data)

    text = decoded_bytes.decode(
        "utf-8",
        errors="replace"
    )

    # HTMLの場合はタグを除去
    if mime_type == "text/html":

        text = re.sub(
            r"<(script|style)[^>]*>.*?</\1>",
            "",
            text,
            flags=re.IGNORECASE | re.DOTALL
        )

        text = re.sub(
            r"<br\s*/?>|</p>|</div>|</tr>",
            "\n",
            text,
            flags=re.IGNORECASE
        )

        text = re.sub(
            r"<[^>]+>",
            "",
            text
        )

        text = html.unescape(text)

        # 不要な空白を整理
        text = text.replace("\xa0", " ")
        text = re.sub(r"[ \t]+", " ", text)

        # 各行の前後の空白を除去
        lines = [
            line.strip()
            for line in text.splitlines()
        ]

        text = "\n".join(lines)

        # 連続する空行を最大1行に整理
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()

    if mime_type == "text/plain":
        return text.strip()

    return ""

def search_and_get_gmail_messages(query, max_results=2):

    if not isinstance(query, str) or not query.strip():
        return {
            "status": "error",
            "message": "Gmail検索キーワードを指定してください。"
        }

    try:
        max_results = int(max_results)

        if not 1 <= max_results <= 5:
            raise ValueError

    except (TypeError, ValueError):
        return {
            "status": "error",
            "message": "取得件数は1〜5件で指定してください。"
        }

    # Gmail検索
    search_result = search_gmail(
        query,
        max_results
    )

    if search_result.get("status") != "success":
        return search_result

    messages = []

    # 検索結果から本文を取得
    for item in search_result.get("messages", []):

        message = get_gmail_message(
            item["id"]
        )

        if message.get("status") == "success":

            messages.append({
                "headers": message.get("headers", {}),
                "body": message.get("body", "")
            })

    return {
        "status": "success",
        "count": len(messages),
        "messages": messages
    }
