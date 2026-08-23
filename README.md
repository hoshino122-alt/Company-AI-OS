# Company AI OS

> Building an AI-powered operating system for managing a virtual company.

Company AI OS is an experimental project that aims to build a company operated by AI agents.

This repository documents the development process from DAY001 onward, gradually evolving from basic project architecture to a complete AI operating system.

---

## Project Vision

The goal of Company AI OS is to create an environment where AI agents can collaborate as employees inside a virtual company.

Future components include:

- 🤖 AI CEO
- 👨‍💼 AI Employees
- 📅 AI Secretary
- 🏢 Department Management
- ✅ Task Management
- 🗄 SQLite Database
- 🧠 Local LLM Integration
- 📚 Vector Database (RAG)
- ⚙ Workflow Automation

---

## Current Project Structure

```
company_ai_os/
│
├── database/
├── managers/
├── models/
├── data/
└── demo/
```

Each directory has a dedicated responsibility.

| Directory | Description |
|------------|-------------|
| database | Database connection and repositories |
| managers | Business logic |
| models | Data models |
| data | JSON configuration and sample data |
| demo | Demonstration programs |

---

## Development Log

This project is developed as a daily development journal.

- DAY001 – DAY033
  - Company AI OS prototype
  - Ren'Py interface
  - Basic AI framework

- DAY034
  - Project architecture refactoring
  - Python project structure
  - Foundation for future expansion

---

## Roadmap

Upcoming features:

- Employee Management
- Department Management
- Company Manager
- AI Task Assignment
- SQLite Integration
- Local LLM Support
- Multi-Agent Collaboration

---

## Technologies

- Python 3
- Ren'Py
- SQLite
- JSON
- Local LLM (planned)
- Ollama (planned)
- Qdrant (planned)

---

## Development Philosophy

Company AI OS is designed with scalability and modularity in mind.

Every component has a single responsibility, making the project easier to maintain and extend as new AI capabilities are added.

---

## Keywords

- AI Core
- Company AI OS
- Python
- Ren'Py
- Artificial Intelligence
- Local LLM

## Link

[DAY38 Documentation](docs/diary/DAY038.md)

## DAY39 — AI CORE Memory Awakens

DAY39では、AI COREにMemory機能を組み込み、過去の情報を利用して回答できる仕組みをテストしました。

### Implemented

* Conversation Memory
* Facts Memory
* Tool Logs Memory
* Memory Selector
* Tool実行結果の保存
* 過去のTool Logs検索
* 過去の計算結果の再利用
* AI CORE / TOOL / MEMORY / LLM のキャラクター化
* Ren'Pyによる会話ドラマ表現

### Memory Flow

```text
User Question
      ↓
Memory Selector
      ↓
Conversation Memory
Facts Memory
Tool Logs Memory
      ↓
Relevant Memory
      ↓
AI CORE
      ↓
LLM
      ↓
Answer
```

### Tool Result Memory

Toolを実行した結果は、

```text
execute_tool()
      ↓
log_tool()
      ↓
save_tool_log()
      ↓
Tool Logs Memory
```

という流れで保存されます。

DAY39では、過去の計算結果として

```text
1,550
```

をMemoryから取得し、

> 一番最後の計算結果は1,550です。

と回答できることを確認しました。

### Ren'Py Drama

DAY39ではMemory機能の動作を、AI CORE、TOOL、MEMORY、LLMのキャラクターによる会話として表現しました。

**TOOL → AI CORE → MEMORY → LLM → Answer**

という流れを視覚的に表現しています。

### Status

**DAY39 — Memory functionality tested successfully.**

AI COREが過去の情報を利用して回答する基本機能を確認しました。

**MEMORY AWAKENS**

---

### Related

* YouTube: DAY39
* note: DAY39 開発記録


## Author

Company AI OS Development Log

Building one step every day toward an AI-operated company.
