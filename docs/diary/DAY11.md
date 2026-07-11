# DAY11 - OllamaでAI社員と会話する

## 概要

DAY11では、Company AI OSにローカルLLM「Ollama」を統合し、AI社員と会話できる機能を実装しました。

前回作成したMemory Managerと組み合わせることで、AI社員がユーザーからのメッセージを受け取り、Ollamaへ送信し、回答を返せるようになりました。

---

## 実装内容

- Ollamaライブラリの導入
- `ollama_client.py` の作成
- `OllamaClient` クラスの実装
- `chat()` メソッドの作成
- AI社員との連携
- AI社員との会話テスト

---

## ディレクトリ

```text
CompanyAIOS/
│
├── common/
│   ├── employee.py
│   ├── memory.py
│   └── ollama_client.py
```

---

## 学んだこと

AIの処理を `OllamaClient` クラスへまとめることで、

- AI社員
- AI秘書
- AI社長

など、Company AI OS全体で共通利用できる設計になりました。

ローカルLLMを利用することで、インターネット接続やAPI利用料金を気にせず開発できる点も大きなメリットです。

---

## 動作確認

以下の流れで動作を確認しました。

1. AI社員へメッセージ送信
2. Ollamaへリクエスト送信
3. AIが回答を生成
4. 回答を表示

正常に会話できることを確認しました。

---

## 次回

DAY12では、Memory Managerと連携し、AI社員が過去の会話を利用できるように実装します。