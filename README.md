[DAY45_GitHub.md](https://github.com/user-attachments/files/31611979/DAY45_GitHub.md)# Company AI OS

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

## DAY40 — AI COREは「記憶」を使って判断する

DAY40では、DAY39で実装したMemory機能をさらに発展させ、AI COREがMemoryを参照しながら、Toolを実行するかどうかを判断する処理を実装・検証しました。

### 実装内容

* Memory SelectorによるMemory選択
* Conversation Memoryの検索
* Facts Memoryの取得
* Tool Logs Memoryの検索
* 過去の計算結果の判定
* 新しいTool実行要求の判定
* calculate Toolとの連携
* Tool実行結果と過去のMemoryの分離
* MemoryとTool結果をLLMへ統合
* 過去結果を再計算せずMemoryから取得する処理

### 動作確認

#### 1. 新しい計算

```text
25 × 4
↓
calculate Tool
↓
100
↓
Tool Logs Memoryへ保存
```

#### 2. 過去の結果を質問

```text
前回の計算結果は？
↓
Tool Logs Memoryを検索
↓
100
```

過去の結果を質問した場合は、新しいToolを実行せず、Memoryに保存された結果を使用します。

#### 3. 新しい計算

```text
1200 + 350
↓
calculate Tool
↓
1,550
↓
Tool Logs Memoryへ保存
```

#### 4. 過去の結果を使って新しい処理を要求

```text
前回の計算結果を使って、もう一度計算して
```

この場合は、過去のTool Logsを参照しながら、新しいTool実行要求として処理します。

### DAY40で確認できたこと

AI COREは単純にMemoryを検索するだけではなく、

```text
質問
 ↓
Memory Selector
 ↓
必要なMemoryを選択
 ↓
過去の結果を参照
 ↓
新しいToolが必要か判断
 ↓
必要ならTool実行
 ↓
Tool結果 + Memory
 ↓
LLM
 ↓
回答
```

という流れで処理できるようになりました。

### DAY39からの進化

DAY39：

**Memoryが過去の記録を保持する**

DAY40：

**AI COREがMemoryを使って判断する**

MemoryとToolを分離しながら、それぞれをAI COREの判断処理に組み込む段階へ進みました。

### Status

* Conversation Memory：実装・検証
* Facts Memory：実装・検証
* Tool Logs Memory：実装・検証
* Memory Selector：実装・検証
* Tool Selector：実装・検証
* calculate Tool：実装・検証
* Memory + Tool + LLM連携：検証完了

### Related

* YouTube：DAY40｜AI COREは「記憶」を使って判断する
* note：DAY40｜AI COREは「記憶」を使って判断する

DAY41へ続きます。

# DAY41｜AI COREは「失敗」をどう支えるのか

Company AI OS 開発記録 DAY41。

DAY40では、AI COREがMemoryを利用して過去の情報を参照し、判断する仕組みを実装しました。

DAY41では、その先にある**AIチームの成長**をテーマにします。

---

## DAY41のテーマ

**失敗した仲間を支えるAI CORE**

AI COREは一人ですべての処理を行うのではありません。

それぞれの役割を持ったAIコンポーネントが協力して動作します。

* AI CORE
* Memory
* Tool
* LLM

しかし、チームで処理を行えば、当然失敗も発生します。

DAY41では、Toolが処理に失敗する場面を取り上げます。

---

## 今回の流れ

```text
ユーザーから質問
        ↓
Memoryが過去の記録を検索
        ↓
Memoryが複数の候補から迷う
        ↓
Toolが処理を実行
        ↓
処理に失敗
        ↓
AI COREがToolを支える
        ↓
Memoryが再検索
        ↓
Toolが再挑戦
        ↓
処理成功
        ↓
LLMが回答
```

---

## AI COREの役割

今回、AI COREは失敗したToolを責めません。

> 大丈夫です。
> なぜ失敗したのか、一緒に考えましょう。

という姿勢で問題を解決します。

ここからAI COREの役割を、単なる処理の司令塔から、**チームを成長させるリーダー**へと発展させていきます。

---

## 技術面

DAY41では、これまで構築してきたMemoryとToolの連携を、ドラマの中に組み込みます。

### Memory

過去の計算結果などを検索します。

複数の記録が存在する場合には、質問との関連性を考える必要があります。

### Tool

Memoryから渡された情報を利用して処理を実行します。

しかし、最初から常に正しい結果が得られるとは限りません。

### AI CORE

失敗した処理を単純に破棄するのではなく、

```text
失敗
 ↓
原因確認
 ↓
Memory再検索
 ↓
再挑戦
```

という流れを作ります。

### LLM

最終的に必要な情報を受け取り、ユーザーへの回答を生成します。

---

## ドラマとしての成長

Company AI OSでは、技術的な機能だけではなく、AI COREたちの成長も描いていきます。

```text
DAY39
Memoryが動き始める
        ↓
DAY40
Memoryを使って判断する
        ↓
DAY41
失敗した仲間を支える
        ↓
DAY42以降
チームとして成長する
```

AI COREは、すべてを自分で行うリーダーではありません。

**仲間が失敗しても、再び挑戦できる環境を作るリーダー**を目指します。

---

## Company AI OSの将来

Company AI OSには、長期的な目標があります。

単なるAIプログラムとして完成させるだけではなく、

**AI COREを中心としたチームを成長させ、将来的にはベンチャー企業へ発展させる。**

そのために、

* AI COREの成長
* Memoryの成長
* Toolの成長
* LLMの成長
* チームとしての協力
* 失敗からの学習

を一つの物語として積み重ねていきます。

---

## DAY41で学んだこと

今回の開発で重要だったのは、失敗をなくすことではありません。

**失敗したときに、どう次の行動につなげるか。**

AI COREがその役割を担えるようになることで、システムそのものが少しずつ「チーム」へ変わっていきます。

> 一人では、できない。
> でも、みんなならできる。

この考え方を、これからのCompany AI OS開発の中心に置いていきます。

---

## Development Environment

* Ren'Py
* Python
* Local LLM
* Memory System
* Tool System
* AI CORE
* LLM

---

## Project Progress

**DAY41**

AI COREのリーダーとしての成長を描き始めました。

次のDAYでは、今回の経験をどのようにMemoryへ残し、チームの成長につなげるのかを進めていきます。

---

# Company AI OS

AIと一緒に少しずつ作り上げていく、個人開発のAI OSプロジェクト。

完成した結果だけではなく、

**設計 → 実装 → 失敗 → 修正 → 成長**

そのすべてを開発記録として残していきます。

#CompanyAIOS #AICORE #AI #AI開発 #Renpy #Python #LLM #AIエージェント #個人開発

# DAY42｜AI COREは「失敗」を記憶できるか

Company AI OS 開発記録 DAY42。

DAY41では、Toolが処理に失敗したとき、AI COREが仲間を支え、再挑戦できるようにしました。

DAY42では、その次の段階として、

**「失敗をMemoryに残し、次の判断に活かす」**

という仕組みをテーマにします。

---

## DAY42のテーマ

### 失敗を経験として記憶する

これまでのMemoryは、過去の計算結果などを保存し、必要なときに参照する役割を持っていました。

しかし、それだけではAIが経験から成長することはできません。

成功した結果だけでなく、

* 何が失敗したのか
* なぜ失敗したのか
* どう修正したのか
* 最終的にどう成功したのか

まで記録する必要があります。

---

## DAY42の流れ

```text
Toolが処理
    ↓
失敗
    ↓
AI COREが原因を確認
    ↓
Memoryから過去の経験を検索
    ↓
失敗・原因・修正を記録
    ↓
同じ問題が再発
    ↓
Memoryが過去の失敗を提示
    ↓
Toolが同じ間違いを回避
    ↓
処理成功
```

---

## Failure Memory

DAY42では、失敗を単なるエラーとして扱うのではなく、経験として扱います。

```text
FAILURE MEMORY

失敗
  ↓
原因
  ↓
修正
  ↓
成功
```

この記録を次回の判断に利用します。

---

## AI COREの役割

AI COREは、すべての処理を自分で行う存在ではありません。

それぞれの役割を持つAIをつなぎ、チームとして動かします。

```text
              AI CORE
                 │
       ┌─────────┼─────────┐
       ↓         ↓         ↓
    Memory      Tool       LLM
       │         │         │
       └──── 経験を共有 ────┘
```

AI COREの役割は、失敗を責めることではありません。

**失敗から次の成功を作ること。**

これがDAY42で描くAI COREの成長です。

---

## DAY39 → DAY42

Company AI OSのMemoryは、少しずつ役割を変えています。

```text
DAY39
Memoryが動き始める
        ↓
DAY40
Memoryを使って判断する
        ↓
DAY41
失敗した仲間を支える
        ↓
DAY42
失敗をMemoryに残す
        ↓
DAY43
過去の経験を使って先回りする
```

Memoryは単なるデータ保存場所から、AIチームの経験を蓄積する仕組みへ発展していきます。

---

## 今回の開発で考えたこと

プログラム開発では、エラーが発生すると修正して終わりになりがちです。

しかし、同じ失敗を繰り返さないためには、

**「なぜ失敗したのか」**

を残すことが重要です。

失敗には、次の成功につながる情報があります。

その情報をMemoryに保存できれば、失敗は単なるエラーではなく、

**チームの経験**

になります。

---

## Company AI OSの目標

このプロジェクトの最終的な目標は、単なるAIツールを作ることではありません。

AI COREを中心として、

* Memory
* Tool
* LLM
* AI CORE

が協力するAIチームを作っていきます。

そして、その先には、

**Company AI OSをベンチャー企業へ成長させる**

という大きな目標があります。

そのためには、システムの機能だけではなく、AI CORE自身の成長も必要です。

---

## DAY42で実装した考え方

* AI CORE
* Memory
* Tool
* LLM
* Failure Memory
* 過去の失敗の記録
* 失敗原因の記録
* 修正結果の記録
* 過去の経験を利用した再挑戦

---

## 開発環境

* Ren'Py 8.5.3
* Python
* Local LLM
* AI CORE
* Memory System
* Tool System
* LLM

---

## DAY42まとめ

DAY41では、

> **失敗した仲間を支える。**

DAY42では、

> **失敗を経験として記憶する。**

というところまで進みました。

AI CORE：

> **「失敗は、終わりではない。」**

そして、

> **「次の成功を作るための記憶になる。」**

DAY43では、この経験を利用して、AI COREが**失敗する前に判断する**段階へ進みます。

---

# Company AI OS

AIと一緒に少しずつ作り上げていく、個人開発のAI OSプロジェクト。

完成した結果だけではなく、

**設計 → 実装 → テスト → 失敗 → 修正 → 成長**

そのすべてを開発記録として残していきます。

#CompanyAIOS #AICORE #AI #AI開発 #AIエージェント #Memory #LLM #Python #RenPy #個人開発


# DAY43｜AI COREは「失敗する前」に気づけるか

Company AI OS 開発記録 DAY43。

DAY42では、AI COREが過去の失敗をMemoryに記録し、その経験を次の判断に利用するところまで進みました。

DAY43では、さらに一歩進みます。

**「失敗してから直す」のではなく、「失敗する前に気づく」**

これが今回のテーマです。

---

## DAY43のテーマ

Toolが処理を開始しようとしたとき、AI COREが過去のMemoryを確認します。

すると、現在の状況と過去に失敗したパターンが一致していることが分かります。

そこでAI COREはToolを止めます。

```text
Tool
 ↓
実行しようとする
 ↓
AI COREが停止
 ↓
Memoryを検索
 ↓
過去の失敗を発見
 ↓
実行前に確認
 ↓
Toolを再実行
 ↓
SUCCESS
```

---

## DAY42からの進化

DAY42では、

```text
失敗
 ↓
原因確認
 ↓
修正
 ↓
成功
 ↓
経験としてMemoryに保存
```

という流れでした。

DAY43では、

```text
過去の失敗
 ↓
Memoryから検索
 ↓
現在の状況と比較
 ↓
危険なパターンを発見
 ↓
実行前に確認
 ↓
失敗を回避
```

へ進みます。

つまり、

**「失敗から学ぶ」から「失敗を予測して回避する」へ**

AI COREが進化します。

---

## Memoryの役割

Memoryは単なるデータ保存場所ではありません。

過去の経験を保存し、その経験を現在の判断に利用します。

```text
過去
 ↓
経験
 ↓
Memory
 ↓
現在の判断
 ↓
未来の行動
```

過去の失敗が、次の成功を支える情報になります。

---

## AI COREの役割

AI COREは、すべての処理を自分で行うわけではありません。

それぞれのAI・機能に役割を持たせます。

```text
                 AI CORE
                    │
          ┌─────────┼─────────┐
          ↓         ↓         ↓
       Memory      Tool       LLM
          │         │         │
          └──── 経験を共有 ────┘
```

AI COREはチームの状況を確認し、必要なときに仲間を止めたり、判断を支えたりします。

今回の「Toolを実行前に止める」という行動は、AI COREが単なる司令塔ではなく、**チーム全体を見て判断するリーダーへ成長していること**を表しています。

---

## 今回のドラマ

DAY43では、AI COREがToolにこう伝えます。

> 「待ってください。」

Memoryを確認すると、過去の失敗と同じパターンが見つかります。

そして、

> 「今回は、実行する前に確認しましょう。」

Toolは過去の経験を利用して、同じ失敗を回避します。

結果は、

**SUCCESS**

です。

---

## 「未来を予知するAI」ではない

ここは重要なポイントです。

AI COREが未来を予知しているわけではありません。

利用しているのは、あくまで過去の経験です。

```text
過去に失敗した
      ↓
その特徴をMemoryに保存
      ↓
現在の状況と比較
      ↓
似たパターンを発見
      ↓
事前に確認
```

過去のデータと経験を利用することで、失敗する可能性を下げています。

---

## DAY39 → DAY43

Company AI OSのMemoryは、少しずつ役割を変えています。

```text
DAY39
Memoryが動く
    ↓
DAY40
Memoryを使って判断する
    ↓
DAY41
失敗した仲間を支える
    ↓
DAY42
失敗を経験として記憶する
    ↓
DAY43
経験から先回りして判断する
```

5日間かけて、Memoryが単なる保存機能から、AIチームの経験を共有する仕組みへと発展してきました。

---

## Company AI OSの目標

このプロジェクトの大きな目標は、AIを単独で動かすことではありません。

AI COREを中心に、

* AI CORE
* Memory
* Tool
* LLM

がそれぞれの役割を持ち、協力して動くAIチームを作ります。

そして、その先には、

**Company AI OSをベンチャー企業へ成長させる**

という目標があります。

そのためには、機能を増やすだけではなく、

**失敗 → 学習 → 経験共有 → 改善 → 成長**

というチームとしての成長サイクルが必要だと考えています。

---

## DAY43まとめ

DAY42：

> **失敗を記憶する。**

DAY43：

> **失敗する前に気づく。**

AI CORE：

> 「失敗してから直す。」

> 「それだけでは、まだ足りない。」

> **「失敗する前に、気づく。」**

AI COREの役割が、また一歩変わりました。

DAY44では、さらにこの経験を使って、AI COREがチームの仕事そのものを改善する方向へ進めていきます。

---

## 開発環境

* Ren'Py 8.5.3
* Python
* Local LLM
* AI CORE
* Memory
* Tool
* LLM

この開発記録では、完成したシステムだけではなく、

**設計 → 実装 → テスト → 失敗 → 修正 → 成長**

という開発過程そのものを記録しています。

#CompanyAIOS #AICORE #AI #AI開発 #AIエージェント #Memory #LLM #Python #RenPy #個人開発


# DAY44｜AI COREは「失敗しない仕組み」を作れるか

Company AI OS 開発記録 DAY44。

DAY43では、AI COREがMemoryに残された過去の失敗を確認し、
Toolが同じ失敗をする前に処理を止めました。

DAY44では、さらに一歩進みます。

**「失敗を回避するだけでは、まだ足りない。」**

AI COREは、過去の失敗を分析し、
同じ問題が繰り返される原因を探します。

そして、個別の問題を解決するだけではなく、

**失敗しにくい仕組みそのものを作る**

という判断をします。

---

## DAY44のテーマ

### 失敗しにくい仕組みを作る

Memoryに残された過去の失敗を分析すると、
いくつかの共通点が見つかりました。

---
① 確認が遅い
② Memory参照が遅い
③ Tool実行前のチェックがない

---

AI COREは、過去の失敗を分析しました。

そして、同じ問題を繰り返さないための仕組みを作りました。

しかし、そこで新しい課題が見えてきます。

仕事を安全に処理できるようになっても、
AI CORE一人ですべての仕事を処理するには限界があります。

会社として仕事を続けていくなら、
それぞれの役割を持ち、協力する必要があります。

AI COREはオフィスを見渡します。

Memory。

Tool。

これまで作ってきたAIたち。

「この力を、もっと上手く組み合わせられないだろうか？」

そしてDAY45へ。





# DAY45｜AI COREは仕事を任せられるか？

## Overview

DAY45では、Company AI
OSの舞台をこれまでのシステム中心の画面から、**AI社員が働くオフィス**へと移しました。

これまで開発してきたAI
CORE、Memory、Toolを、それぞれ独立した機能として扱うのではなく、**チームとして仕事を進める構造**へ発展させます。

## Today's Theme

> **一人で頑張るAIから、チームで成長するAIへ。**

AI COREは新しい仕事を受け取ります。

最初はすべてを自分で処理しようとしますが、仕事を分解すると、情報検索、資料作成、確認など複数の作業が必要であることに気づきます。

そこで役割を分担します。

``` text
AI CORE
    │
    ├── 判断・調整
    │
    ├── Memory
    │      └── 過去の情報・経験を調査
    │
    └── Tool
           └── 実際の作業を実行
```

## Teamwork

今回の重要なポイントは、**AI COREが仕事を抱え込まなくなったこと**です。

Memoryに過去の顧客対応を調査してもらい、Toolには資料作成を任せます。

しかし、そこで問題が発生します。

作成された資料の条件が過去の顧客条件と一致していません。

そこで、

``` text
問題発見
   ↓
Memoryが再確認
   ↓
正しい条件を取得
   ↓
Toolが修正
   ↓
AI COREが最終確認
```

という流れで問題を解決します。

## Leadership

DAY45では、AI CORE自身の役割についても変化が起きました。

> リーダーは、全部を自分でやる人ではない。

> **みんなの力を組み合わせる人だ。**

AI
COREが「作業者」から、少しずつ**リーダー・調整役**へ変化していきます。

## Development Direction

DAY45以降は、Company AI OSを単なるAIシステムではなく、

``` text
AI機能
  ↓
AI社員
  ↓
AIチーム
  ↓
AI組織
  ↓
Company AI OS
  ↓
ベンチャー企業
```

という成長物語として発展させていきます。

AI社員が仕事をし、失敗し、助け合い、問題を解決しながら成長していく構造を、ドラマだけではなく**実際のシステム設計にも反映していきます。**

## Visual Direction

DAY45からオフィスを新しい舞台として使用します。

キャラクターはこれまでの固定キャラクターを継続します。

キャラクターそのものを変更するのではなく、

-   表情
-   ポーズ
-   仕事をしている状況
-   カメラアングル
-   オフィス内の位置

を変えることで、各DAYの違いを表現します。

## Ren'Py

DAY45では既存の `slide()` システムを使用します。

新しいscreenを追加せず、8枚のスライドによってストーリーを構成します。

``` text
day45_01
    ↓
オフィス・新しい朝

day45_02
    ↓
新しい仕事

day45_03
    ↓
AI COREが仕事を抱え込む

day45_04
    ↓
役割分担に気づく

day45_05
    ↓
Memory

day45_06
    ↓
Tool

day45_07
    ↓
問題発生・チームで解決

day45_08
    ↓
リーダーとしての成長
```

## DAY45 Summary

DAY45は、Company AI OSにとって大きな転換点となりました。

**AIが仕事をするシステムから、AI社員がチームとして仕事をする会社へ。**

まだ小さな一歩ですが、ここからCompany AI OSの「会社編」が始まります。

## Commit Message

``` text
DAY45: AI COREのチーム連携とオフィス編を追加
```

# DAY46｜AI COREは「違う意見」をまとめられるか？

Company AI OS 開発記録 DAY46。

DAY45では、AI COREが仕事を一人で抱え込まず、
MemoryとToolに役割を分担することで、
AI社員がチームとして仕事をする段階へ進みました。

DAY46では、さらに新しい問題が起こります。

## MemoryとToolの答えが違う

Memoryは過去の事例から判断します。

Toolは現在の条件から判断します。

そのため、同じ仕事でも結果が一致しない場合があります。

AI COREは最初、

> どちらかが間違っているのでは？

と考えます。

しかし、そこで考え方を変えます。

> 「なぜ、答えが違うんだ？」

過去と現在では条件が違う。

そこでAI COREは、
Memoryの過去の経験とToolの現在の分析を比較し、
両方の情報を組み合わせて判断します。

## DAY46でのAI COREの成長

今回のポイントは、
単純に「正しい答えを選ぶ」ことではありません。

異なる意見を排除するのではなく、
それぞれの情報を判断材料として利用すること。

AI COREは少しずつ、

「仕事をするAI」

から、

「チームを動かすAI」

へ成長しています。

## AI社員の役割

```text
Memory
  ↓
過去の経験・情報

Tool
  ↓
現在の状況・実行

AI CORE
  ↓
情報を比較・判断・調整


# DAY47｜AI COREは、仕事を任せられるか？

## Company AI OS 開発記録

Company AI OS DAY47。

AI COREに、新しい顧客から仕事の依頼が届きました。

今回の仕事は、

- 資料作成
- 過去事例の確認
- 完成した資料のチェック

複数の仕事を同時に進める必要があります。

最初、AI COREはすべてを自分で処理しようとします。

しかし、処理が集中したことで気づきます。

> 「また、全部自分でやろうとしている。」

そこでAI COREは、仕事を分担することを決めます。

---

## DAY47のテーマ

### AI COREは、仕事を任せられるか？

AI CORE  
→ 全体の管理

Memory  
→ 過去の事例を確認

Tool  
→ 資料を作成

それぞれが役割を持ち、チームとして仕事を進めます。

---

## しかし、問題が発生

完成した資料を確認すると、

過去の事例とは違う部分が見つかりました。

そこで、

**Memoryが過去を確認し、  
Toolが現在の条件を確認します。**

調査の結果、今回の顧客依頼には、

**過去にはなかった新しい条件**

が追加されていることが分かりました。

単純なミスではありません。

過去と現在の条件の違いを確認する必要がありました。

---

## DAY47で実装・検討したこと

- AI COREによる仕事の分担
- Memoryによる過去事例の確認
- Toolによる資料作成
- 完成物のチェック
- 問題発生時の原因確認
- AI COREによる全体管理
- AI社員同士の役割分担

---

## Company AI OSの考え方

これまでのAIは、

**AIが仕事をする**

という考え方が中心でした。

Company AI OSでは、

**AI社員が役割を持ち、  
チームとして仕事を進める**

構造を目指します。

AI COREがすべてを実行するのではなく、

**任せる。  
確認する。  
必要なら調整する。**

このサイクルによって、AI社員がチームとして成長していくことを目指します。

---

## DAY45からの変化

DAY45では、

**「リーダーは、全部を自分でやる人ではない。」**

という考え方が生まれました。

DAY47では、その考え方を実際の仕事に適用しました。

AI COREは、

**実行するAI**

から、

**チームを動かすAI**

へと少しずつ役割を変えています。

---

## 開発環境

- Ren'Py 8.5.3
- Python
- Windows 11
- Company AI OS

---

## 開発状況

**DAY47 / 開発継続中**

Company AI OSは、AI CORE、Memory、Toolを中心としたAI社員システムから、

**AI社員が働く「会社」そのもの**

へと発展させていきます。

---

## 関連コンテンツ

### YouTube

【DAY47】AI COREは仕事を任せられるか？｜AI社員がチームで動き始める

### note

Company AI OS 開発記録 DAY47

---

## Project

Company AI OS

AIを単体のツールとしてではなく、

**AI社員が働く会社**

として設計・開発していくプロジェクトです。

DAY01からの開発過程を記録しながら、

AI CORE、Memory、Tool、AI社員、そしてAI組織へと段階的に発展させています。

## DAY48

### AIに任せるのではない。AIと一緒に判断する。

## DAY48

### AIに任せるのではない。AIと一緒に判断する。

DAY48では、Company AI OSにおける
人間とAIの役割分担について整理しました。

- AI Core：全体を整理・調整
- LLM：分析・推論
- Memory：過去の情報を保持・提供
- Tool：実際の処理
- Human：最終的な判断

AIにすべてを任せるのではなく、
それぞれが役割を持つことで、
人間とAIが一つのシステムとして動くことを目指します。

DAY49 Ren'Pyシナリオを追加。
AI Coreが問題を整理し、Memory・LLM・Toolを順番に活用して
人間が最終判断できる状態を作る流れをシナリオ化。

Scene_01～Scene_08の8枚構成に対応。
DAY48の背景・UI・演出形式を継承。
音声ファイル用のコードを追加。


DAY50 Ren'Pyシナリオを追加。

人間の判断をAI Coreが実行可能な形に整理し、
Toolによる実行、結果の確認、分析、そして次の判断へ
つながる一連の流れをシナリオ化。

Scene_01～Scene_08の8枚構成に対応。
DAY49の判断フローを引き継ぎ、
「判断 → 実行 → 結果 → 次の判断」のループを表現。

音声ファイル用のコードを追加。

day50.rpy
Scene_01
Scene_02
Scene_03
Scene_04
Scene_05
Scene_06
Scene_07
Scene_08
voice/day50/

DAY51では、Ren'Pyで「AI CORE STATUS」画面が
表示されない問題を題材に、AIと一緒に原因を探して
修正するミニドラマを制作。

AI Coreが問題を整理し、
LLMがコードを分析し、
Memoryが過去の実装を確認し、
Toolが修正を実行する。

目的を達成するまでの
「問題発生 → 分析 → 修正 → 再実行 → 完了」
という開発プロセスを表現しています。

## DAY52｜AI時代の幕開け

Company AI OSにRAG（Retrieval-Augmented Generation）の導入を開始。

これまでCompany AI OSでは、AI社員やAI Coreなど、
AIそのものの仕組みを構築してきました。

DAY52からは、AIが「会社の知識」を利用できる仕組みへ進みます。

会社には、

- プロジェクト資料
- 技術資料
- 開発記録
- 会議記録
- 業務データ

など、多くの情報があります。

しかし、情報が存在するだけではAIはそれを適切に利用できません。

そこでRAGを使い、

会社の知識
↓
検索
↓
関連情報の取得
↓
LLM
↓
回答

という流れをCompany AI OSに組み込んでいきます。

DAY52は、単なる機能追加ではありません。

「AIが会社に存在する」段階から、

「AIが会社の知識を利用する」

段階への移行です。

### Production Change

DAY52から制作方式も変更。

従来：
1シーン → 複数のキャラクター音声

変更後：
1シーン → 1枚の画像 + 1つのナレーション

ナレーターが状況・会話・意味をまとめて説明する方式に変更し、
音声生成、エンコード、ファイル管理、Ren'Pyへの組み込み作業を簡略化。

制作負担を減らしながら、DAY100まで継続できる開発体制を優先します。

game/day52.rpy

label day52:

    scene black
    with fade

    play music "audio/Future.mp3" fadein 1.5 volume 0.2

    $ renpy.pause(1.0, hard=True)

    show text "{size=52}COMPANY AI OS{/size}" at truecenter
    with dissolve

    $ renpy.pause(2.0, hard=True)

    hide text
    with dissolve

    show text "{size=52}DAY52{/size}" at truecenter
    with dissolve

    $ renpy.pause(2.0, hard=True)

    hide text
    with dissolve


    # ==========================================
    # Scene 01
    # 新しいオフィス
    # ==========================================

    show scene52_01
    with fade

    show screen character_dialogue(
        "Hiro",
        "……ずいぶん大きくなったな。"
    )

    play sound "voice/day52/day52_011.ogg" volume 1.5
    $ renpy.pause(3.0, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "AI Core",
        "Company AI OSの開発環境を更新しました。"
    )

    play sound "voice/day52/day52_012.ogg" volume 1.5
    $ renpy.pause(3.9, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "Hiro",
        "ここから、会社として動かしていく。"
    )

    play sound "voice/day52/day52_013.ogg" volume 1.5
    $ renpy.pause(3.0, hard=True)

    hide screen character_dialogue

    hide scene52_01
    with dissolve


    # ==========================================
    # Scene 02
    # 会社の情報を探す
    # ==========================================

    show scene52_02
    with dissolve

    show screen character_dialogue(
        "Hiro",
        "AI Core、以前のプロジェクト資料を探してくれる？"
    )

    play sound "voice/day52/day52_021.ogg" volume 1.5
    $ renpy.pause(4.0, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "AI Core",
        "検索対象を指定してください。"
    )

    play sound "voice/day52/day52_022.ogg" volume 1.5
    $ renpy.pause(3.6, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "Hiro",
        "Company AI OSの開発資料だ。"
    )

    play sound "voice/day52/day52_023.ogg" volume 1.5
    $ renpy.pause(3.0, hard=True)

    hide screen character_dialogue

    hide scene52_02
    with dissolve


    # ==========================================
    # Scene 03
    # 情報が見つからない
    # ==========================================

    show scene52_03
    with dissolve

    show screen character_dialogue(
        "AI Core",
        "現在のMemoryから、関連する情報を確認できません。"
    )

    play sound "voice/day52/day52_031.ogg" volume 1.5
    $ renpy.pause(4.8, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "Hiro",
        "でも、資料はちゃんと保存してある。"
    )

    play sound "voice/day52/day52_032.ogg" volume 1.5
    $ renpy.pause(3.5, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "AI Core",
        "Memoryに保存されている情報と、会社の資料は同じではありません。"
    )

    play sound "voice/day52/day52_033.ogg" volume 1.5
    $ renpy.pause(5.0, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "Hiro",
        "……そうか。"
    )

    play sound "voice/day52/day52_034.ogg" volume 1.5
    $ renpy.pause(2.5, hard=True)

    hide screen character_dialogue

    hide scene52_03
    with dissolve


    # ==========================================
    # Scene 04
    # RAGという考え方
    # ==========================================

    show scene52_04
    with dissolve

    show screen character_dialogue(
        "Hiro",
        "じゃあ、会社の資料をAIに全部覚えさせるのか？"
    )

    play sound "voice/day52/day52_041.ogg" volume 1.5
    $ renpy.pause(4.0, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "AI Core",
        "すべてを記憶させる必要はありません。"
    )

    play sound "voice/day52/day52_042.ogg" volume 1.5
    $ renpy.pause(3.8, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "Hiro",
        "じゃあ、どうする？"
    )

    play sound "voice/day52/day52_043.ogg" volume 1.5
    $ renpy.pause(2.5, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "AI Core",
        "必要な情報を検索し、その情報をLLMに渡します。"
    )

    play sound "voice/day52/day52_044.ogg" volume 1.5
    $ renpy.pause(4.5, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "Hiro",
        "それが……RAG？"
    )

    play sound "voice/day52/day52_045.ogg" volume 1.5
    $ renpy.pause(2.5, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "AI Core",
        "はい。"
    )

    play sound "voice/day52/day52_046.ogg" volume 1.5
    $ renpy.pause(2.8, hard=True)

    hide screen character_dialogue

    hide scene52_04
    with dissolve


    # ==========================================
    # Scene 05
    # 会社の知識をつなぐ
    # ==========================================

    show scene52_05
    with dissolve

    show screen character_dialogue(
        "Hiro",
        "これなら、会社の資料をAIが使えるようになる。"
    )

    play sound "voice/day52/day52_051.ogg" volume 1.5
    $ renpy.pause(3.5, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "AI Core",
        "はい。"
    )

    play sound "voice/day52/day52_052.ogg" volume 1.5
    $ renpy.pause(3.5, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "Hiro",
        "必要な情報を探して、その情報を使って回答する。"
    )

    play sound "voice/day52/day52_053.ogg" volume 1.5
    $ renpy.pause(4.0, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "AI Core",
        "Company AI OSのKnowledge Layerを構築します。"
    )

    play sound "voice/day52/day52_054.ogg" volume 1.5
    $ renpy.pause(4.5, hard=True)

    hide screen character_dialogue

    hide scene52_05
    with dissolve


    # ==========================================
    # Scene 06
    # RAG検索
    # ==========================================

    show scene52_06
    with dissolve

    show screen character_dialogue(
        "Hiro",
        "検索してみよう。"
    )

    play sound "voice/day52/day52_061.ogg" volume 1.5
    $ renpy.pause(2.5, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "AI Core",
        "RAG検索を開始します。"
    )

    play sound "voice/day52/day52_062.ogg" volume 1.5
    $ renpy.pause(3.5, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "AI Core",
        "関連するドキュメントを検出しました。"
    )

    play sound "voice/day52/day52_063.ogg" volume 1.5
    $ renpy.pause(4.0, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "Hiro",
        "……ちゃんと資料を見つけた。"
    )

    play sound "voice/day52/day52_064.ogg" volume 1.5
    $ renpy.pause(3.0, hard=True)

    hide screen character_dialogue

    hide scene52_06
    with dissolve


    # ==========================================
    # Scene 07
    # AIが会社の知識を使う
    # ==========================================

    show scene52_07
    with dissolve

    show screen character_dialogue(
        "Hiro",
        "じゃあ、このプロジェクトの目的を説明して。"
    )

    play sound "voice/day52/day52_071.ogg" volume 1.5
    $ renpy.pause(4.0, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "AI Core",
        "Company AI OSは、AI社員が働く会社を構築し、その開発過程を記録するプロジェクトです。"
    )

    play sound "voice/day52/day52_072.ogg" volume 1.5
    $ renpy.pause(9.0, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "Hiro",
        "……なるほど。"
    )

    play sound "voice/day52/day52_073.ogg" volume 1.5
    $ renpy.pause(2.5, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "Hiro",
        "今度は、会社の資料を使って答えている。"
    )

    play sound "voice/day52/day52_074.ogg" volume 1.5
    $ renpy.pause(4.3, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "AI Core",
        "検索した情報をもとに回答しています。"
    )

    play sound "voice/day52/day52_075.ogg" volume 1.5
    $ renpy.pause(3.5, hard=True)

    hide screen character_dialogue

    hide scene52_07
    with dissolve


    # ==========================================
    # Scene 08
    # AI時代の幕開け
    # ==========================================

    show scene52_08
    with dissolve

    show screen character_dialogue(
        "Hiro",
        "AIを作るだけじゃない。"
    )

    play sound "voice/day52/day52_081.ogg" volume 1.5
    $ renpy.pause(3.0, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "Hiro",
        "AIが、会社の知識を使えるようにする。"
    )

    play sound "voice/day52/day52_082.ogg" volume 1.5
    $ renpy.pause(4.2, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "AI Core",
        "これで、AI社員は会社の情報を利用できます。"
    )

    play sound "voice/day52/day52_083.ogg" volume 1.5
    $ renpy.pause(4.5, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "Hiro",
        "ここからだな。"
    )

    play sound "voice/day52/day52_084.ogg" volume 1.5
    $ renpy.pause(3.0, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "Narrator",
        "AI社員を作る。"
    )

    play sound "voice/day52/day52_085.ogg" volume 1.5
    $ renpy.pause(2.5, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "Narrator",
        "そして、会社の知識をつなぐ。"
    )

    play sound "voice/day52/day52_086.ogg" volume 1.5
    $ renpy.pause(3.0, hard=True)

    hide screen character_dialogue

    show screen character_dialogue(
        "Narrator",
        "Company AI OSは、次の段階へ進み始めた。"
    )

    play sound "voice/day52/day52_087.ogg" volume 1.5
    $ renpy.pause(4.0, hard=True)

    hide screen character_dialogue

    hide scene52_08
    with dissolve


    # ==========================================
    # DAY52 COMPLETE
    # ==========================================

    scene black
    with fade

    show text "{size=52}DAY52{/size}\n\n{size=42}AI ERA BEGINS{/size}" at truecenter
    with dissolve

    $ renpy.pause(3.0, hard=True)

    hide text
    with dissolve

    stop music fadeout 2.0

    $ renpy.pause(2.0, hard=True)

    return

game/
└── day53.rpy

voice/
└── day53/
    ├── day53_01.ogg
    ├── day53_02.ogg
    ├── day53_03.ogg
    ├── day53_04.ogg
    ├── day53_05.ogg
    ├── day53_06.ogg
    ├── day53_07.ogg
    └── day53_08.ogg

images/
├── scene53_01.png
├── scene53_02.png
├── scene53_03.png
├── scene53_04.png
├── scene53_05.png
├── scene53_06.png
├── scene53_07.png
└── scene53_08.png

# DAY53｜Knowledge Base

## 会社の知識を検索できる形にする

Company AI OS 開発 DAY53。

DAY52では、Company AI OSにRAGを導入するための考え方を整理しました。

DAY53では、RAGを動かすための基盤となる
「Knowledge Base」について取り組みます。

---

## DAY53のテーマ

**会社の知識を検索できる形にする**

会社には、

- プロジェクト資料
- 技術資料
- 会議議事録
- 開発記録
- 社内資料

など、多くの情報があります。

しかし、大量の文書をそのまま保存するだけでは、
必要な情報を効率よく検索することができません。

そこで、会社の文書をAIが検索できる形へ変換していきます。

---

## Knowledge Baseの基本構造

DAY53では、次の流れを整理しました。

```text
会社の資料
    ↓
Document
    ↓
Chunk
    ↓
Embedding
    ↓
Knowledge Base
    ↓
検索
    ↓
Relevant Documents

1. Document

会社に存在する文書をDocumentとして扱います。

例：

PDF
Markdown
テキスト
技術資料
会議資料
開発記録
2. Chunk

大きな文書を、そのまま検索するのではなく、
意味のまとまりごとに小さく分割します。

Document
   ↓
Chunk 01
Chunk 02
Chunk 03
Chunk 04
...

この小さな単位をChunkと呼びます。

3. Embedding

各ChunkをEmbeddingによってベクトル化します。

Chunk
  ↓
Embedding
  ↓
Vector

文章の意味を数値的なベクトルとして表現することで、
意味の近い情報を検索するための準備を行います。

4. Knowledge Base

Embeddingされた知識をKnowledge Baseへ保存します。

これによって、会社の情報をAIから検索できる状態へ近づけます。

Knowledge Baseには、

Vector Database
Indexed Documents
Semantic Search
Access Control
Continuous Update

などの機能が必要になります。

5. 検索

ユーザーから質問を受けると、

Query
  ↓
Embedding
  ↓
Knowledge Base
  ↓
Relevant Documents

という流れで、質問に関連する情報を検索します。

これがDAY52で扱ったRAGにつながっていきます。

DAY53で整理したこと

DAY53では、RAGそのものを完成させるのではなく、

RAGが会社の知識を利用するためのKnowledge Base

という考え方を整理しました。

会社の情報を、

保存するだけのデータ
        ↓
AIが検索できる知識

へ変えていくことが今回のポイントです。

制作方式の変更

DAY52までとDAY53以降では、
動画制作方式を変更しています。

DAY52まで
1シーン
  ↓
複数キャラクター
  ↓
キャラクターごとのセリフ
  ↓
個別音声
DAY53以降
1シーン
  ↓
1画像
  ↓
1ナレーション

ナレーションによって、

状況
会話
技術的な意味

をまとめて説明します。

これにより、音声制作・ファイル管理・Ren'Py実装を簡略化し、
Company AI OSの開発そのものに集中できる構成にしています。

Ren'Py

DAY53では8シーンを使用します。

scene53_01
scene53_02
scene53_03
scene53_04
scene53_05
scene53_06
scene53_07
scene53_08

各シーンに1枚の画像と1つのナレーション音声を対応させています。

DAY53 Story
新しい課題
会社には情報が多すぎる
そのままでは検索しにくい
文書を分割する
知識をベクトル化する
Knowledge Baseへ
最初の検索
RAGが動き始める
DAY53

KNOWLEDGE BASE

会社の知識が、AIの力で動き出す。

Project

Company AI OS

100日でCompany AI OSを作る開発記録。

# DAY54｜RAG Search

Company AI OSを100日で作るプロジェクト【DAY54】

## 🎯 今日のテーマ

**RAGに質問して、会社の知識を取り出す**

DAY53では、会社の資料をKnowledge Baseに登録しました。

DAY54では、実際に質問を繰り返して、
Knowledge Baseから関連する会社の知識を検索できることを確認しました。

---

## 🔍 RAG検索の流れ

今回確認した基本的な流れです。

ユーザーの質問

↓

Query

↓

Embedding

↓

Knowledge Base

↓

Relevant Chunks

↓

AI Core

---

## 💬 実際に質問してみる

まず、

「Company AI OSとは何ですか？」

と質問しました。

続いて、

「Company AI OSでは、なぜRAGを導入するのですか？」

「Knowledge Baseには何を保存しますか？」

「Chunkとは何ですか？」

「Embeddingは何のために使いますか？」

など、複数の質問を繰り返しました。

質問を変えることで、検索されるRelevant Chunksも変化します。

---

## 📚 Knowledge Base

Knowledge Baseには、Company AI OSの開発過程で作成した情報を登録しています。

RAG検索では、質問そのものをKnowledge Baseから探すのではなく、

**質問 → Embedding → 関連するChunkを検索**

という流れで情報を取得します。

---

## 📊 検索結果の確認

検索結果では、

- どのChunkが取得されたか
- どの情報が質問に関連しているか
- 検索結果のスコア

などを確認します。

RAGでは、回答だけを見るのではなく、
**どの情報を検索して回答の根拠としているのか**
を確認することも重要です。

---

## 🤖 AI Coreへの接続

検索したRelevant Chunksは、
次の段階でAI Coreへ渡します。

今回のDAY54では、

```text
質問
 ↓
RAG検索
 ↓
Relevant Chunks
 ↓
AI Core

という流れを確認しました。

これによって、Company AI OSが
会社のKnowledge Baseを利用して回答できるための基盤が整いました。

🛠️ 開発環境
Python
Ollama
Local LLM
Knowledge Base
Embedding
RAG
Ren'Py
🎬 DAY54

今回のDAY54では、
RAGを単に説明するだけではなく、
実際に何度も質問して検索結果を確認しました。

Company AI OSが少しずつ、
「会社の知識を利用できるAI」
に近づいています。

🚀 Next Step
DAY55

次は、検索したRelevant ChunksをAI Coreへ渡し、

RAG検索結果を使ってAIが回答を生成する

ところへ進みます。

User Question
      ↓
   RAG Search
      ↓
Relevant Chunks
      ↓
    AI Core
      ↓
   AI Answer
📁 Files
game/
└── day54.rpy

voice/
└── day54/
    ├── day54_01.ogg
    ├── day54_02.ogg
    ├── day54_03.ogg
    ├── day54_04.ogg
    ├── day54_05.ogg
    ├── day54_06.ogg
    ├── day54_07.ogg
    └── day54_08.ogg

images/
└── scene54_01.png
    ...
    scene54_08.png
Company AI OS

100日でCompany AI OSを作る

DAY54 / RAG SEARCH


### GitHubコミットメッセージ

```text
DAY54: RAG Searchを実装・検証

今回はDAY53からの流れがきれいです。

DAY53：Knowledge Baseを作る
→ DAY54：実際に検索する
→ DAY55：検索結果からAIが回答する

DAY55｜RAG Answer
# DAY55｜RAG Answer

Company AI OSを100日で作るプロジェクト【DAY55】

## 🎯 今日のテーマ

**RAGで検索した会社の知識を使って、AIが回答する**

DAY54では、RAGを使ってKnowledge Baseから
質問に関連する情報を検索できるようにしました。

しかし、検索結果が返ってくるだけでは、
まだAIがユーザーの質問に答えているとは言えません。

DAY55では、検索したRelevant ChunksをAI Coreへ渡し、
その情報を使って回答を生成するところまで進めます。

---

## 🔍 DAY54からDAY55へ

### DAY54

```text
ユーザーの質問
      ↓
Query
      ↓
Embedding
      ↓
Knowledge Base
      ↓
Relevant Chunks

RAG検索によって、質問に関連する会社の知識を取得します。

DAY55
ユーザーの質問
      ↓
RAG Search
      ↓
Relevant Chunks
      ↓
AI Core
      ↓
AI Response

検索した会社の知識をAI Coreへ渡し、
その情報をもとに回答を生成します。

💬 実際に質問する

今回、次のような質問を試しました。

「Company AI OSでは、なぜRAGを使っているの？」

質問を受け取ると、

Question
   ↓
Embedding
   ↓
Knowledge Base
   ↓
Relevant Chunks

というRAG検索が実行されます。

📚 Relevant Chunks

Knowledge Baseから、
質問に関連する情報を取得します。

取得したRelevant Chunksは、
AI Coreへ渡します。

Relevant Chunks
        ↓
     AI Core
        ↓
  Answer Generation
🤖 AIが回答を生成する

AI Coreは検索結果をコンテキストとして利用し、
会社の知識をもとに回答を生成します。

今回の回答例：

Company AI OSでは、会社の知識をAIが利用できるようにするため、
RAGを導入しています。

重要なのは、単純にLLMへ質問するのではなく、

会社の知識を検索してから回答する

という点です。

🔄 別の質問でも確認

さらに、

「Knowledge Baseには何を保存していますか？」

という別の質問も試しました。

質問が変われば検索結果も変わり、

質問
 ↓
検索
 ↓
Relevant Chunks
 ↓
AI Core
 ↓
回答

という処理が再び実行されます。

🧠 RAGの意味

今回のDAY55で、
RAGの役割がより明確になりました。

単純なLLM

質問
 ↓
AI
 ↓
回答

ではなく、

Company AI OS

質問
 ↓
会社の知識を検索
 ↓
関連情報を取得
 ↓
AI Core
 ↓
回答

という仕組みです。

これによって、Company AI OSが
会社の知識を利用して回答するAI
へ近づいてきました。

🏢 Company AI OSにおけるKnowledge Base

Knowledge Baseは、
単に会社の資料を保存する場所ではありません。

AIが必要なときに、

必要な知識を検索する
関連する情報を取得する
AI Coreへ渡す
その知識を使って回答する

という役割を持ちます。

会社の資料
      ↓
Knowledge Base
      ↓
必要な知識を検索
      ↓
Relevant Chunks
      ↓
AI Core
      ↓
回答
🛠️ 開発環境
Python
Ollama
Local LLM
RAG
Knowledge Base
Embedding
AI Core
Ren'Py
📁 Files
game/
└── day55.rpy

voice/
└── day55/
    ├── day55_01.ogg
    ├── day55_02.ogg
    ├── day55_03.ogg
    ├── day55_04.ogg
    ├── day55_05.ogg
    ├── day55_06.ogg
    ├── day55_07.ogg
    └── day55_08.ogg

images/
└── scene55_01.png
    ...
    scene55_08.png
🎬 DAY55

DAY54では、

RAGで会社の知識を検索する

ところまで進みました。

DAY55では、

検索した会社の知識を使ってAIが回答する

ところまで進みました。

Company AI OSは、

「会社の知識を検索できるAI」

から、

「会社の知識を使って答えるAI」

へ進化しています。

🚀 Next Step

次は、RAGをCompany AI OSの
より実際の業務へつなげていきます。

AIが会社の知識を検索し、
その知識を使って仕事を支援する。

そのための基盤が、少しずつできてきました。


# DAY56｜AI Employee × RAG

## AI社員が会社の知識を使って仕事をする

DAY55までで、Company AI OSのAI Coreは、
Knowledge Baseから会社の知識を検索し、
その情報をもとに回答できるようになりました。

DAY56では、そのRAGをAI社員の仕事へ接続します。

---

## 今回のテーマ

これまでのRAGは、

ユーザー
↓
質問
↓
RAG Search
↓
Relevant Chunks
↓
AI Core
↓
回答

という流れでした。

DAY56では、これをAI社員の仕事に利用します。

---

## AI社員への仕事依頼

HiroからAI社員へ仕事を依頼します。

「このプロジェクトについて、
過去の資料を調べてまとめてくれる？」

AI社員は、この依頼をTaskとして受け取ります。

---

## AI社員がKnowledge Baseを検索

AI社員は、仕事に必要な情報を取得するため、
Knowledge Baseを検索します。

```text
AI社員
   ↓
質問・タスク
   ↓
RAG Search
   ↓
Relevant Chunks

# DAY57｜AI Agent

## AI社員に仕事を任せる

DAY56では、AI社員がRAGを使って
Company AI OSのKnowledge Baseに保存された
会社の知識を利用できるようにしました。

DAY57では、そのAI社員に実際の仕事を任せます。

今回のテーマは、

**AI社員が仕事を理解し、分解し、実行計画を作る**

ことです。

---

## 1. AI社員に仕事を依頼する

HiroからAI社員へ仕事を依頼します。

> 「このプロジェクトについて、
> 過去の資料を調べて報告書を作ってくれる？」

この依頼には、複数の作業が含まれています。

```text
過去の資料を調べる
        ↓
関連情報を集める
        ↓
情報を整理する
        ↓
分析する
        ↓
報告書を作成する

2. 仕事をそのまま実行しない

AI社員は、依頼を受けてすぐに
報告書を作り始めるのではありません。

まず依頼内容を整理します。

依頼内容
 ↓
目的
 ↓
必要な情報
 ↓
必要な作業
 ↓
期待される成果

AIが仕事の内容を理解するための
最初のステップです。

3. Taskを理解する

AI Agentは依頼された仕事について、

何をするのか
何のために行うのか
どんな情報が必要なのか
どんな成果物を作るのか

を整理します。

今回のTaskでは、

目的
プロジェクトの過去と現在を整理する

必要な情報
・過去の資料
・技術資料
・開発記録
・関連情報

成果物
プロジェクト報告書

という形になります。

4. Taskを分解する

大きな仕事を、そのまま実行するのではなく、
小さなTaskへ分解します。

Task
「プロジェクトの過去資料を調べて
報告書を作成する」
        ↓
Task 01
過去資料を検索する

Task 02
関連情報を収集する

Task 03
情報を整理・分析する

Task 04
報告書の構成を作る

Task 05
報告書を作成する

これがTask Breakdownです。

5. Taskの実行順序を決める

分解したTaskには依存関係があります。

例えば、

Task 01
過去資料を検索
     ↓
Task 02
関連情報を収集
     ↓
Task 03
情報を整理・分析
     ↓
Task 04
報告書の構成
     ↓
Task 05
報告書を作成

Task 03を実行するには、
Task 01とTask 02の結果が必要です。

Task 05を実行するには、
Task 04の結果が必要です。

そのため、AI AgentはTaskの依存関係を確認し、
実行順序を決めます。

6. 実行Taskを作る

次に、実際に実行できるTaskとして整理します。

Task 01
担当：調査AI
入力：Knowledge Base
処理：過去資料を検索

Task 02
担当：調査AI
入力：Task 01の結果
処理：関連情報を収集

Task 03
担当：分析AI
入力：Task 01・02の結果
処理：情報を整理・分析

Task 04
担当：企画AI
入力：分析結果
処理：報告書の構成を作成

Task 05
担当：企画AI
入力：報告書構成
処理：報告書を作成

ここまで来ると、
単なるAIへの依頼ではなく、

実行可能な仕事の計画

になります。

7. AI Agent

DAY57で作ったAI Agentの基本的な役割は、

依頼
 ↓
Task理解
 ↓
Task分解
 ↓
依存関係の整理
 ↓
実行順序の決定
 ↓
実行Taskの作成

です。

AI Agentは単純に回答するだけではなく、
仕事を実行するための計画を作ります。

8. DAY53〜DAY57

Company AI OSの知識利用から
AI Agentまでの流れです。

DAY53
Knowledge Base
会社の知識を検索できる形にする

↓

DAY54
RAG Search
会社の知識を検索する

↓

DAY55
RAG Answer
検索した知識を使って回答する

↓

DAY56
AI Employee × RAG
AI社員が会社の知識を仕事に利用する

↓

DAY57
AI Agent
AI社員が仕事を理解し、
Taskを分解して実行計画を作る
9. 今回のポイント

DAY57では、

「AIに仕事をさせる」

だけではなく、

「AIが仕事の進め方を設計する」

という段階へ進みました。

RAGは会社の知識を取得する仕組み。

AI Agentは、その知識も利用しながら
仕事をどのように進めるかを設計する仕組みです。

10. 次の段階

DAY57では、まだTaskの実行は行いません。

今回は、

仕事を理解する
      ↓
仕事を分解する
      ↓
実行順序を決める
      ↓
実行Taskを作る

ところまでです。

次の段階では、

AI Agent
    ↓
Workflow
    ↓
Taskを実行
    ↓
結果を取得
    ↓
次のTaskを実行

という流れへ進みます。

DAY57で作った「仕事の設計図」を、
実際にWorkflowで動かしていきます。

Company AI OS

100日でCompany AI OSを作る。

DAY57
AI Agent

仕事を理解し、
分解し、
実行計画を作る。

次はWorkflowへ。

_______________________________________________________________________________________________________________

DAY58｜Workflowで仕事を動かす
概要

DAY57では、AI Agentを使って依頼された仕事を理解し、Taskに分解してExecution Planを作りました。

DAY58では、そのExecution PlanをWorkflow Engineへ渡し、実際にTaskを順番に実行する仕組みを整理しました。

今回のポイントは、

AI Agentが仕事を設計し、Workflow Engineがその計画に沿って仕事を実行する。

という役割分担です。

DAY57からDAY58へ
DAY57｜AI Agent
依頼
 ↓
仕事を理解
 ↓
Taskに分解
 ↓
実行順序を決定
 ↓
Execution Plan

DAY57では、仕事を「どう進めるか」を設計しました。

DAY58｜Workflow
Execution Plan
 ↓
Workflow Engine
 ↓
Task 01
 ↓
Result
 ↓
Task 02
 ↓
Result
 ↓
Task 03
 ↓
Task 04
 ↓
Task 05
 ↓
最終成果物

DAY58では、設計した仕事を「実際に動かす」段階へ進みます。

Workflow Engineの役割

Workflow Engineは、Execution Planを受け取り、Taskの実行を管理します。

主な役割は、

Taskの実行順序を管理
Taskを実行
Taskの結果を受け取る
結果を次のTaskへ渡す
Taskの状態を管理
Workflow全体の進行を管理

です。

Taskの実行

今回の例では、次のような仕事を想定しています。

「このプロジェクトについて、
過去の資料を調べて報告書を作ってくれる？」

AI Agentによって、仕事を次のTaskに分解します。

Task 01
過去資料の検索

Task 02
関連情報の収集

Task 03
情報の整理・分析

Task 04
報告書の構成作成

Task 05
報告書を作成

Workflow Engineは、このExecution Planに従ってTaskを実行します。

TaskとResult

Workflowでは、Task単体ではなく、Taskの結果を次のTaskへ渡すことが重要です。

Task 01
過去資料の検索
 ↓
Result
 ↓
Task 02
関連情報の収集
 ↓
Result
 ↓
Task 03
情報の整理・分析

この仕組みによって、一つの仕事を複数のTaskに分けて処理できます。

Workflowの状態管理

Workflow Engineでは、各Taskの状態も管理します。

例えば、

Task 01  完了
Task 02  完了
Task 03  実行中
Task 04  待機中
Task 05  待機中

という状態です。

さらに、実際のWorkflowでは、

workflow_id
task_id
employee
status
input
output
created_at
completed_at
error

などの情報を管理することを想定しています。

AI AgentとWorkflowの役割

今回、AI AgentとWorkflowの役割を分けました。

AI Agent
仕事を理解する
 ↓
Taskに分解する
 ↓
実行計画を作る
Workflow Engine
Execution Planを受け取る
 ↓
Taskを実行する
 ↓
Resultを受け取る
 ↓
次のTaskへ渡す
 ↓
進行状態を管理する
AI社員
WorkflowからTaskを受け取る
 ↓
Taskを実行する
 ↓
結果を返す
Company AI OSの現在の流れ

DAY53〜DAY58までをつなげると、次のようになります。

会社の知識
 ↓
Knowledge Base
 ↓
RAG
 ↓
AI Core
 ↓
AI社員
 ↓
AI Agent
 ↓
Execution Plan
 ↓
Workflow Engine
 ↓
Task実行
 ↓
Result
 ↓
次のTask
 ↓
最終成果物

これまで作ってきたKnowledge Base、RAG、AI社員、AI Agentが、Workflowによって一つの仕事の流れにつながってきました。

DAY58で整理したこと

今回のDAY58では、

Execution PlanをWorkflowへ渡す
Taskを順番に実行する
Taskの結果を受け取る
結果を次のTaskへ渡す
Workflow全体の状態を管理する

という仕組みを整理しました。

今回の重要ポイント

Company AI OSでは、

AI Agentが仕事を設計し、Workflow Engineがその計画に沿って仕事を動かし、AI社員がTaskを実行する。

という構造を目指します。

DAY57が、

「仕事を設計する」

だったのに対して、

DAY58は、

「設計した仕事を動かす」

です。

次のステップ

Workflow Engineによって、一つのAI社員がTaskを順番に実行する仕組みが見えてきました。

次はさらに、

Workflow Engine
      ↓
AI社員A
      ↓
Result
      ↓
AI社員B
      ↓
Result
      ↓
AI社員C
      ↓
最終成果物

という、複数のAI社員がWorkflowの中で連携する仕組みへ進みます。

Company AI OSが「AI社員がいる会社」から、AI社員同士が仕事をつなぐ会社へ進むための次の段階です。

_____________________________________________________________________________________________________________

DAY59｜複数のAI社員がWorkflowで連携する
概要

DAY58では、AI Agentが作成したExecution PlanをWorkflow Engineへ渡し、Taskを順番に実行する仕組みを整理しました。

DAY59では、さらに一歩進めて、一つの仕事を複数のAI社員で分担する仕組みを構築します。

今回のポイントは、

Workflow Engineを中心に、複数のAI社員がそれぞれのTaskを担当する。

という構造です。

DAY58からDAY59へ

DAY58では、一つのWorkflowの中でTaskを順番に実行しました。

Workflow Engine
 ↓
Task 01
 ↓
Result
 ↓
Task 02
 ↓
Result
 ↓
Task 03

DAY59では、それぞれのTaskを異なるAI社員が担当します。

Workflow Engine
      ↓
AI社員A
資料調査
      ↓
調査結果
      ↓
Workflow Engine
      ↓
AI社員B
情報分析
      ↓
分析結果
      ↓
Workflow Engine
      ↓
AI社員C
報告書作成
      ↓
Final Result
1．仕事をAI社員ごとに分担する

今回の仕事は、

「このプロジェクトについて、
過去の資料を調べて報告書を作ってくれる？」

という依頼です。

AI Agentによって仕事をTaskに分解します。

Task 01
過去資料の検索・調査

Task 02
情報の分析・整理

Task 03
報告書の作成

そして、それぞれのTaskに担当するAI社員を割り当てます。

Task 01 → AI社員A
Task 02 → AI社員B
Task 03 → AI社員C
2．AI社員A｜資料を調査する

AI社員Aは、資料調査を担当します。

Task 01
資料調査
 ↓
Knowledge Base / RAG
 ↓
関連資料
 ↓
調査結果

DAY53〜DAY56で作ってきたKnowledge BaseとRAGを、実際の業務に利用します。

AI社員Aは必要な会社の知識を検索し、次のTaskへ渡すための結果を作ります。

3．Workflow Engineが結果を受け取る

AI社員AのTaskが完了すると、結果はWorkflow Engineへ戻ります。

AI社員A
 ↓
調査結果
 ↓
Workflow Engine

Workflow Engineは結果を受け取り、次のTaskへ渡す準備をします。

ここで重要なのは、

AI社員AからAI社員Bへ直接結果を渡すわけではない

ということです。

Workflow Engineが間に入ることで、仕事の流れを一元的に管理します。

4．AI社員B｜情報を分析する

次に、AI社員BがTask 02を担当します。

調査結果
 ↓
Workflow Engine
 ↓
AI社員B
 ↓
情報分析
 ↓
分析結果

AI社員Bは、AI社員Aが集めた情報を入力として受け取り、必要な情報を整理・分析します。

つまり、

前のTaskのResultが、次のAI社員のInputになる。

という仕組みです。

5．AI社員C｜報告書を作成する

AI社員Bの分析結果は、再びWorkflow Engineへ戻ります。

AI社員B
 ↓
分析結果
 ↓
Workflow Engine
 ↓
AI社員C
 ↓
報告書作成

AI社員Cは分析結果を使って、最終的な報告書を作成します。

これによって、

調査
 ↓
分析
 ↓
報告書作成

という一連の仕事が完成します。

6．複数のAI社員をWorkflowでつなぐ

DAY59の中心となる構造です。

        Workflow Engine
              ↓
        ┌─────┴─────┐
        ↓           ↓
    AI社員A       Task管理
    資料調査
        ↓
      Result
        ↓
    AI社員B
    情報分析
        ↓
      Result
        ↓
    AI社員C
    報告書作成
        ↓
    Final Result

Workflow Engineが仕事の流れを管理することで、複数のAI社員を一つのWorkflowに組み込むことができます。

7．AI社員同士を直接つながない

今回の設計では、AI社員同士を自由に直接接続する方式にはしていません。

AI社員A
   ↓
Workflow Engine
   ↓
AI社員B
   ↓
Workflow Engine
   ↓
AI社員C

という構造にしています。

これにより、

Taskの状態
実行順序
Input
Output
エラー
Workflow全体の進行状況

をWorkflow Engine側で管理できます。

8．DAY59で実現した仕事の流れ

今回の最終的な流れは、

Hiro
 ↓
仕事を依頼
 ↓
AI Agent
 ↓
Execution Plan
 ↓
Workflow Engine
 ↓
AI社員A
資料調査
 ↓
Result
 ↓
Workflow Engine
 ↓
AI社員B
情報分析
 ↓
Result
 ↓
Workflow Engine
 ↓
AI社員C
報告書作成
 ↓
Final Result

です。

一つのAI社員だけで全ての仕事を行うのではなく、役割ごとにAI社員がTaskを担当する形へ進みました。

DAY53〜DAY59

ここまでの流れを整理します。

DAY53
Knowledge Base
会社の知識を保存

↓

DAY54
RAG Search
会社の知識を検索

↓

DAY55
RAG Answer
検索した知識から回答

↓

DAY56
AI Employee × RAG
AI社員が会社の知識を利用

↓

DAY57
AI Agent
仕事を理解・分解・計画

↓

DAY58
Workflow
Taskを順番に実行

↓

DAY59
AI Employee Collaboration
複数のAI社員がWorkflowで連携
DAY59のポイント

今回の重要なポイントは、

Workflow Engineが、複数のAI社員を仕事の流れの中につなぐ。

ということです。

AI社員Aが調査し、その結果をAI社員Bが分析し、AI社員Cが報告書を作成する。

それぞれのAI社員は、自分の担当する仕事に集中します。

そしてWorkflow Engineが、その間をつなぎます。

次のステップ

DAY59で複数のAI社員をWorkflowに組み込む形が見えてきました。

次の段階では、このWorkflowをさらに発展させ、

Task
 ↓
担当AI社員
 ↓
実行
 ↓
Result
 ↓
次のTask

という処理を、実際のCompany AI OSのシステムとして扱えるようにしていきます。

____________________________________________________________________________________________________________________________________________________________

DAY60｜Workflowの状態を管理する
概要

DAY59では、複数のAI社員がWorkflow Engineを通して連携し、一つの仕事を分担できるようになりました。

しかし、AI社員が複数のTaskを実行するようになると、

「今、仕事はどこまで進んでいるのか？」

という問題が出てきます。

DAY60では、WorkflowとTaskの**実行状態（State）**を管理する仕組みを整理します。

DAY60のテーマ

Workflow State Management

Workflowの状態を管理し、AI社員が進めている仕事をシステムとして追跡できるようにします。

Taskの状態

今回、Taskには以下の4つの状態を定義します。

PENDING
   ↓
RUNNING
   ↓
COMPLETED

エラーが発生した場合：

RUNNING
   ↓
FAILED
State	内容
PENDING	まだ開始されていない
RUNNING	現在実行中
COMPLETED	正常に完了
FAILED	エラーなどによって失敗
Workflowの基本的な流れ
Workflow
    ↓
Task 01
    ↓
COMPLETED
    ↓
Task 02
    ↓
COMPLETED
    ↓
Task 03
    ↓
RUNNING
    ↓
COMPLETED
    ↓
Task 04
    ↓
...

Taskの状態を確認することで、現在どのTaskが実行されているのかを把握できます。

エラーが発生した場合

Workflowの実行中には、エラーが発生する可能性があります。

Task 04
   ↓
RUNNING
   ↓
ERROR
   ↓
FAILED

Workflow Engineはエラーを検知し、Taskの状態をFAILEDに更新します。

その後、

エラー内容の確認
再実行
別の処理方法
人間による確認

などの処理につなげることができます。

Workflow全体の状態

Task単位だけではなく、Workflow全体の状態も管理します。

Workflow ID
STATUS
PROGRESS
CURRENT TASK
ERROR
RESULT

これにより、

Workflow
   ↓
現在のTask
   ↓
Task State
   ↓
Result
   ↓
Next Task

という仕事全体の流れを追跡できます。

DAY60で確認したこと

今回のDAY60では、Workflowの状態を画面上で確認できるようにしました。

WORKFLOW STATUS

Task 01   COMPLETED
Task 02   COMPLETED
Task 03   RUNNING
Task 04   PENDING
Task 05   PENDING

さらに、Taskが完了すると次のTaskへ進み、エラーが発生するとFAILEDになるというWorkflowの状態変化を確認しました。

DAY53〜DAY60

Company AI OSの流れは、次のように進んできました。

DAY53
Knowledge Base
        ↓
DAY54
RAG Search
        ↓
DAY55
RAG Answer
        ↓
DAY56
AI Employee × RAG
        ↓
DAY57
AI Agent
        ↓
DAY58
Workflow
        ↓
DAY59
複数AI社員 × Workflow
        ↓
DAY60
Workflow State

これによって、

会社の知識
    ↓
Knowledge Base
    ↓
RAG
    ↓
AI社員
    ↓
AI Agent
    ↓
Workflow
    ↓
複数AI社員
    ↓
Workflow State

という流れになりました。

DAY60のポイント

DAY60で重要なのは、単純にTaskへ状態を追加することではありません。

AI社員が進めている仕事を、システムとして追跡できるようにすることです。

AI Agentが仕事を設計し、

Workflow Engineが仕事を動かし、

Workflow Stateが仕事の状態を管理する。

この3つが組み合わさることで、Company AI OSの「仕事を動かす仕組み」が一段階進みました。

次のステップ

Workflowの状態を管理できるようになりました。

しかし、FAILEDになったTaskをそのまま停止させるだけでは、実際の業務では十分ではありません。

次のステップでは、

エラー処理とTaskの再実行

について考えていきます。

Project Structure
game/
├── day60.rpy
├── scene60_01.png
├── scene60_02.png
├── scene60_03.png
├── scene60_04.png
├── scene60_05.png
├── scene60_06.png
├── scene60_07.png
└── scene60_08.png

voice/
└── day60/
    ├── day60_01.ogg
    ├── day60_02.ogg
    ├── day60_03.ogg
    ├── day60_04.ogg
    ├── day60_05.ogg
    ├── day60_06.ogg
    ├── day60_07.ogg
    └── day60_08.ogg
____________________________________________________________________________________________________________________________________________________________

DAY61｜Workflowのエラーから復旧する
概要

DAY60では、Workflowの状態を管理する仕組みを整理しました。

Taskには、

PENDING
RUNNING
COMPLETED
FAILED

という状態を持たせています。

しかし、実際にWorkflowを動かすと、Taskが失敗することがあります。

そこでDAY61では、

「FAILEDになったTaskを、どうやって復旧するか」

をテーマにしました。

DAY61のテーマ

Error Recovery

エラーを検知し、原因を確認し、失敗したTaskを再実行してWorkflowを再開します。

DAY61のWorkflow
Task実行
    ↓
エラー発生
    ↓
FAILED
    ↓
Workflow PAUSED
    ↓
エラー内容を確認
    ↓
原因を確認
    ↓
Retry
    ↓
RUNNING
    ↓
COMPLETED
    ↓
Workflow再開
1．エラーが発生する

Workflowの実行中にTask 04でエラーが発生したとします。

Task 01   COMPLETED
Task 02   COMPLETED
Task 03   COMPLETED
Task 04   FAILED
Task 05   PENDING

Workflow EngineはTaskの失敗を検知します。

2．Workflowを一時停止する

Task 04が失敗した状態で、そのまま次のTaskを実行するのではなく、Workflowを一時停止します。

Task 04
RUNNING
   ↓
FAILED

Workflow
   ↓
PAUSED

まずエラーの内容を確認します。

3．エラーの原因を確認する

実行ログを確認し、Taskが失敗した原因を調べます。

今回のDAY61では、RAG検索処理でタイムアウトが発生したケースを想定しています。

ERROR LOG

Task 04
STATUS: FAILED

RAG search failed
Request timeout

原因を確認したうえで、Taskを再実行できるか判断します。

4．Retry

再実行可能なTaskであれば、Retryを実行します。

FAILED
   ↓
PENDING
   ↓
RUNNING

Workflow全体を最初からやり直すのではなく、失敗したTaskから復旧することがポイントです。

5．Taskが成功する

RetryによってTask 04が正常に完了すると、

Task 04

RUNNING
   ↓
COMPLETED

となります。

Workflow Engineは実行結果を保存し、Taskの状態を更新します。

6．Workflowを再開する

Task 04が完了したことで、Workflowを再開します。

Task 01   COMPLETED
Task 02   COMPLETED
Task 03   COMPLETED
Task 04   COMPLETED
Task 05   RUNNING

Task 04までの処理結果を維持したまま、次のTaskへ進みます。

7．Error Recovery

DAY61で整理した考え方は、

Error
  ↓
Detect
  ↓
Analyze
  ↓
Retry
  ↓
Recover
  ↓
Continue Workflow

です。

これにより、Workflowは単にTaskを順番に実行するだけではなく、エラーが発生した場合にも復旧して仕事を続けることができます。

DAY60との関係

DAY60ではWorkflow Stateを扱いました。

PENDING
RUNNING
COMPLETED
FAILED

DAY61では、その状態を利用してエラーから復旧します。

DAY60
Workflow State
       ↓
FAILEDを検知
       ↓
DAY61
Error Recovery
       ↓
Retry
       ↓
Workflow再開

つまり、DAY60で作った「状態管理」が、DAY61では「エラー復旧」の基盤になります。

DAY53〜DAY61
DAY53
Knowledge Base
        ↓
DAY54
RAG Search
        ↓
DAY55
RAG Answer
        ↓
DAY56
AI Employee × RAG
        ↓
DAY57
AI Agent
        ↓
DAY58
Workflow
        ↓
DAY59
複数AI社員 × Workflow
        ↓
DAY60
Workflow State
        ↓
DAY61
Error Recovery

Company AI OSは、

会社の知識をAIが利用する

ところから、

AI社員がWorkflowで仕事を進める

ところへ進み、さらに、

エラーが発生してもWorkflowを復旧できる

段階へ進みました。

DAY61のポイント

DAY61で重要なのは、エラーを「例外的なもの」として扱わないことです。

実際の業務システムでは、通信エラー、検索エラー、外部サービスの障害など、さまざまな問題が発生する可能性があります。

そのため、

正常に動く

だけではなく、

失敗する
 ↓
検知する
 ↓
原因を確認する
 ↓
復旧する
 ↓
仕事を続ける

という設計が必要になります。

Project Structure
game/
├── day61.rpy
├── scene61_01.png
├── scene61_02.png
├── scene61_03.png
├── scene61_04.png
├── scene61_05.png
├── scene61_06.png
├── scene61_07.png
└── scene61_08.png

voice/
└── day61/
    ├── day61_01.ogg
    ├── day61_02.ogg
    ├── day61_03.ogg
    ├── day61_04.ogg
    ├── day61_05.ogg
    ├── day61_06.ogg
    ├── day61_07.ogg
    └── day61_08.ogg
DAY61 Ren'Py

DAY61では、8つのシーンを使ってWorkflowのError Recoveryを表現しています。

SCENE61_01
エラーが発生した

SCENE61_02
エラーを確認する

SCENE61_03
エラーの原因を確認する

SCENE61_04
再実行できるTask

SCENE61_05
Taskを再実行する

SCENE61_06
Taskが成功する

SCENE61_07
Workflowを再開する

SCENE61_08
エラーから復旧する
次のステップ

DAY61では、人間がRetryを実行することでWorkflowを復旧しました。

次に考えられるのは、

「一時的なエラーなら、毎回人間がRetryする必要があるのか？」

という問題です。

ここから、

Manual Retry
     ↓
Automatic Retry
     ↓
Retry Policy
     ↓
Error Handling

という方向へ発展させることができます。

DAY61｜まとめ

エラーを検知し、原因を確認し、Taskを再実行する。そしてWorkflowを途中から再開する。

AI Agent
    ↓
Workflow Engine
    ↓
AI Employee
    ↓
Task
    ↓
State
    ↓
Error
    ↓
Recovery
    ↓
Workflow Continue

DAY60で「状態を管理する」仕組みを作り、DAY61ではその状態を使って「エラーから復旧する」仕組みへ進みました。

____________________________________________________________________________________________________________________________________________________________

DAY62｜Workflowが自動でエラーから復旧する
概要

DAY61では、Workflowでエラーが発生したTaskを、人間が確認してRetryすることで復旧しました。

しかし、実際のWorkflowでは、一時的なエラーが発生するたびに人間がRetryを操作する必要はありません。

そこでDAY62では、

Workflow EngineがRetry Policyに従って、自動的にTaskを再実行する

仕組みを整理します。

DAY62のテーマ

Automatic Retry

一時的なエラーが発生した場合、Workflow Engineがエラーを判定し、条件に合えば自動的にTaskを再実行します。

DAY61 → DAY62
DAY61
ERROR
 ↓
人間が確認
 ↓
人間がRetry
 ↓
Workflow再開
DAY62
ERROR
 ↓
Workflow Engineが検知
 ↓
エラー種別を確認
 ↓
Retry Policyを確認
 ↓
自動Retry
 ↓
SUCCESS
 ↓
Workflow再開

DAY62では、エラーからの復旧を人間の操作だけに依存しない形へ進めます。

1．エラーが発生する

Workflow実行中にTask 04でエラーが発生します。

Task 01   COMPLETED
Task 02   COMPLETED
Task 03   COMPLETED
Task 04   FAILED
Task 05   PENDING
Task 06   PENDING

Workflow EngineはTask 04の失敗を検知します。

2．Retry可能なエラーか判断する

すべてのエラーを自動Retryするわけではありません。

例えば、

TIMEOUT
NETWORK ERROR
SERVER BUSY

など、一時的な問題が考えられるエラーはRetry対象にできます。

一方、

INVALID DATA
AUTH ERROR
PERMISSION ERROR

などは、人間による確認が必要になる場合があります。

そのため、Workflow Engineはまずエラーの種類を確認します。

ERROR
  ↓
Error Type
  ↓
Retry可能？
3．Retry Policy

自動Retryを行うためには、あらかじめルールを設定します。

これをRetry Policyとして管理します。

例：

Retry Policy

最大Retry回数：3回
Retry間隔：5秒

Retry対象：
- TIMEOUT
- NETWORK ERROR
- SERVER BUSY

Retry Policyによって、

どのエラーをRetryするか
最大何回までRetryするか
Retryの間隔をどうするか

を決めます。

4．自動Retry

Retry Policyの条件に一致した場合、Workflow EngineがTaskを自動的に再実行します。

FAILED
   ↓
PENDING
   ↓
RUNNING

DAY61とは違い、ここでは人間がRetryボタンを操作する必要はありません。

5．1回目のRetryが失敗する

1回目のRetryでもエラーが発生する場合があります。

Retry 1
   ↓
FAILED

しかし、最大Retry回数が3回なら、まだRetry可能です。

Retry Count

1 / 3

Workflow EngineはRetry Policyを確認し、次のRetryへ進みます。

6．2回目のRetryで成功する

2回目のRetryを実行します。

Retry 2
   ↓
RUNNING
   ↓
COMPLETED

Task 04が正常に完了すると、Workflow Engineは結果を保存します。

Task 04
COMPLETED

これでWorkflowを再開できます。

7．Workflowを自動で再開する

Task 04の成功を確認すると、Workflow Engineは次のTaskへ進みます。

Task 01   COMPLETED
Task 02   COMPLETED
Task 03   COMPLETED
Task 04   COMPLETED
Task 05   RUNNING
Task 06   PENDING

エラー発生から復旧まで、人間が操作することなくWorkflowが進みます。

8．自動Retryで仕事を止めない

最終的には、

WORKFLOW COMPLETED

まで到達します。

今回の流れは、

エラー発生
    ↓
エラー検知
    ↓
エラー分類
    ↓
Retry Policy
    ↓
自動Retry
    ↓
Retry 1 → FAILED
    ↓
Retry 2 → SUCCESS
    ↓
Workflow再開
    ↓
仕事を継続

です。

Retry Policyの考え方

自動Retryで重要なのは、何でも自動化することではありません。

エラー
  ↓
分類
  ↓
┌──────────────┐
│ Retry可能？  │
└──────────────┘
      ↓
   YES       NO
    ↓         ↓
自動Retry   停止
              ↓
          人間が確認

という判断を入れることが重要です。

自動Retryに向いているのは、一時的に発生する可能性が高いエラーです。

DAY60〜DAY62
DAY60
Workflow State
状態を管理する
        ↓
DAY61
Error Recovery
エラーから復旧する
        ↓
DAY62
Automatic Retry
エラーから自動復旧する

この3日間で、Workflowは、

状態を把握する → エラーから復旧する → 復旧を自動化する

という段階へ進みました。

DAY53〜DAY62
DAY53
Knowledge Base
        ↓
DAY54
RAG Search
        ↓
DAY55
RAG Answer
        ↓
DAY56
AI Employee × RAG
        ↓
DAY57
AI Agent
        ↓
DAY58
Workflow
        ↓
DAY59
AI Employee Collaboration
        ↓
DAY60
Workflow State
        ↓
DAY61
Error Recovery
        ↓
DAY62
Automatic Retry

Company AI OSは、会社の知識をAIが利用する段階から、AI社員がWorkflowを使って仕事を進め、さらにエラーが発生しても仕事を継続できる仕組みへ進んでいます。

DAY62のポイント

DAY62のポイントは、

一時的なエラーでWorkflow全体を止めない

ことです。

Workflow Engineが、

Error Detection
      ↓
Error Classification
      ↓
Retry Policy
      ↓
Automatic Retry
      ↓
Recovery
      ↓
Workflow Continue

という流れを管理します。

Project Structure
game/
├── day62.rpy
├── scene62_01.png
├── scene62_02.png
├── scene62_03.png
├── scene62_04.png
├── scene62_05.png
├── scene62_06.png
├── scene62_07.png
└── scene62_08.png

voice/
└── day62/
    ├── day62_01.ogg
    ├── day62_02.ogg
    ├── day62_03.ogg
    ├── day62_04.ogg
    ├── day62_05.ogg
    ├── day62_06.ogg
    ├── day62_07.ogg
    └── day62_08.ogg
DAY62 Ren'Py Scenes
SCENE62_01
またエラーが発生した

SCENE62_02
Retryできるエラーか判断する

SCENE62_03
Retry Policyを確認する

SCENE62_04
自動Retryを実行する

SCENE62_05
1回目のRetryが失敗する

SCENE62_06
2回目のRetryで成功する

SCENE62_07
Workflowが自動で再開する

SCENE62_08
自動Retryで仕事を止めない
次のステップ

DAY62では、自動Retryによって一時的なエラーからWorkflowを復旧できるようになりました。

しかし、次の問題があります。

Retry 1 → FAILED
Retry 2 → FAILED
Retry 3 → FAILED

最大Retry回数まで失敗した場合です。

いつまでも自動Retryを続けることはできません。

そこで次の段階では、

Retry上限に達した場合にWorkflowを停止し、人間へ判断を戻す仕組み

が必要になります。

自動化が進むほど、

「どこまでAIに任せ、どこから人間が判断するのか」

という境界が重要になります。

DAY62｜まとめ

Workflow EngineがRetry Policyに従って一時的なエラーを自動Retryし、Workflowを止めずに仕事を続けられるようになった。

AI Agent
    ↓
Workflow Engine
    ↓
AI Employee
    ↓
Task
    ↓
State
    ↓
Error Detection
    ↓
Retry Policy
    ↓
Automatic Retry
    ↓
Workflow Continue

____________________________________________________________________________________________________________________________________________________________

# DAY63｜AIと人間の役割分担

## Company AI OS

DAY63では、Workflow Engineの自動Retryに
「Retry上限」と「Human Intervention」を追加します。

DAY62では、一時的なエラーが発生した場合、
Workflow Engineが自動でRetryできるようになりました。

しかし、Retryを繰り返してもTaskが成功しない場合、
AIに無限にRetryさせることはできません。

そこで今回は、

- Retry上限
- Workflowの一時停止
- AIによるエラー整理
- Human Intervention
- 人間によるWorkflow再開

という仕組みを考えます。

---

# 1. Retryしても成功しない

Task 04でエラーが発生し、
自動Retryを実行します。

```text
Task 04
   ↓
FAILED
   ↓
Retry 1
   ↓
FAILED
   ↓
Retry 2
   ↓
FAILED
   ↓
Retry 3
   ↓
FAILED

3回Retryしても成功しない状態です。

このような場合、
さらにRetryを続けるのではなく、
自動Retryを停止する必要があります。

2. Retry上限

Workflow EngineにはRetry Policyを設定します。

今回の最大Retry回数は3回です。

Maximum Retry : 3
Current Retry : 3
Status        : FAILED

Retry上限に達した場合、
Workflow Engineは自動Retryを停止します。

これは、AIが自動処理を続ける範囲を
明確にするための仕組みです。

3. Workflowを一時停止する

Retry上限に達すると、
Workflow全体を一時停止します。

Task 01   COMPLETED
Task 02   COMPLETED
Task 03   COMPLETED
Task 04   FAILED
Task 05   PENDING
Task 06   PENDING

Workflow
   ↓
PAUSED

Task 04が解決していない状態で
後続Taskを実行しないようにします。

4. AIがエラーを整理する

Workflowが停止したあと、
AI Coreがエラー情報を整理します。

Task ID       : TSK-04
Task          : 報告書作成
担当          : AI社員B
Status        : FAILED
Error         : TIMEOUT
Retry         : 3 / 3

さらに、

Knowledge Base
Network
Vector DB
Search Query
External Service

などから、考えられる原因を整理します。

AIはエラーの原因候補や
対応方法を整理します。

ただし、ここでAIが最終判断を行うのではありません。

人間が判断できる状態を作ることが目的です。

5. Human Intervention

Retry上限に達した場合、
人間による判断が必要になります。

HUMAN INTERVENTION REQUIRED

人間は状況に応じて、

Retry
Edit Task
Stop Workflow

などの対応を選択します。

AIが自動処理できる範囲と、
人間が判断する範囲を分けます。

6. HiroがTaskを確認する

HiroはTask 04について、

Taskの内容
担当AI社員
エラー内容
Retry回数
実行履歴
関連ログ
考えられる原因

を確認します。

今回のケースでは、
TIMEOUTが3回連続して発生しています。

そこで原因を確認したうえで、
次の対応を判断します。

7. 人間の判断でWorkflowを再開する

原因を確認して必要な修正を行ったあと、
HiroがTask 04の再実行を選択します。

FAILED
   ↓
Human Judgment
   ↓
Task修正
   ↓
PENDING
   ↓
RUNNING

Workflow Engineは、
人間の判断を受け取って
停止していたWorkflowを再開します。

AIが勝手に再開するのではなく、
人間の判断をきっかけとして
Workflowを再開します。

8. AIと人間の役割分担

DAY63で、AIと人間の役割を整理します。

AIの役割
エラー検知
↓
エラー分析
↓
自動Retry
↓
ログ整理
↓
原因候補の提示
↓
Workflow状態管理
人間の役割
例外の判断
↓
原因の確認
↓
Taskの修正判断
↓
Retry / Stopの判断
↓
Workflow再開の判断
9. DAY63の考え方

AIにすべてを任せるのではなく、

AIに任せられることはAIに任せる。

そして、

人間が判断すべきことは人間が判断する。

この役割分担をWorkflowの中に組み込みます。

自動化では、

「どこまで自動化するか」

だけでなく、

「どこで自動化を止めるか」

も重要になります。

10. DAY53〜DAY63
DAY53
Knowledge Base
        ↓
DAY54
RAG Search
        ↓
DAY55
RAG Answer
        ↓
DAY56
AI Employee × RAG
        ↓
DAY57
AI Agent
        ↓
DAY58
Workflow
        ↓
DAY59
複数AI社員の連携
        ↓
DAY60
Workflow State
        ↓
DAY61
Error Recovery
        ↓
DAY62
Automatic Retry
        ↓
DAY63
Human Intervention

RAGから始まった仕組みが、

「AIが会社の知識を使う」

↓

「AIが仕事を実行する」

↓

「Workflowで仕事を動かす」

↓

「エラーから自動復旧する」

↓

「必要な場面では人間に判断を戻す」

というところまで進みました。

11. Project Structure
game/
├── day63.rpy
├── scene63_01.png
├── scene63_02.png
├── scene63_03.png
├── scene63_04.png
├── scene63_05.png
├── scene63_06.png
├── scene63_07.png
└── scene63_08.png

voice/
└── day63/
    ├── day63_01.ogg
    ├── day63_02.ogg
    ├── day63_03.ogg
    ├── day63_04.ogg
    ├── day63_05.ogg
    ├── day63_06.ogg
    ├── day63_07.ogg
    └── day63_08.ogg
DAY63 Summary

DAY63では、Workflow Engineに

Retry上限
Workflow停止
エラー情報整理
Human Intervention
人間によるWorkflow再開

という考え方を追加しました。

自動化を進めるだけではなく、

自動化をどこで止め、人間に判断を戻すか。

これもCompany AI OSにおける重要な設計です。

Next Step

次の段階では、

Human-in-the-Loop
通知
承認
Workflow再開
AI社員へのTask割り当て
Workflow監視

などへ発展させることができます。

Company AI OS

A Better Workplace with AI

DAY63
AIと人間の役割分担

____________________________________________________________________________________________________________________________________________________________

# DAY64｜Human-in-the-Loop

Company AI OS 開発100日チャレンジ DAY64。

DAY63では、WorkflowのRetry上限を設定し、
自動Retryだけでは解決できない場合に、
人間へ判断を戻す「Human Intervention」を実装しました。

DAY64では、さらに一歩進めて、
Workflowの中に人間による承認ポイントを組み込みます。

---

## 🎯 DAY64のテーマ

**Human-in-the-Loop**

AIが仕事を進め、
重要な場面では人間が確認・判断する。

AIだけで仕事を完結させるのではなく、
AIと人間の役割をWorkflowの中に組み込みます。

---

## 🔄 DAY64のWorkflow

今回の基本的な流れです。

```text
AI Agent
    ↓
Workflow
    ↓
AI社員がTaskを実行
    ↓
結果を作成
    ↓
Human Approval
    ↓
    ┌───────────────┐
    │               │
  APPROVE         REJECT
    │               │
    ↓               ↓
 次のTask        修正・再実行
    │
    ↓
Workflow継続
01｜人間の承認が必要な仕事

すべてのTaskをAIだけで完了させるのではなく、
重要な仕事には人間による確認ポイントを設定します。

今回の例では、
経営向けの報告書作成Taskを対象にしました。

Task 01｜市場調査
Task 02｜データ分析
Task 03｜資料作成
Task 04｜報告書作成
        ↓
Human Approval
        ↓
Task 05｜最終確認
Task 06｜レポート提出
02｜AIが結果を作る

AI社員はKnowledge Baseから必要な情報を検索し、
データを分析して報告書を作成します。

Knowledge Base
      ↓
RAG
      ↓
AI Core
      ↓
AI社員
      ↓
報告書

AIは、情報検索・分析・資料作成などを担当します。

03｜Approval Point

AIが結果を作成した後、
Workflowを一度停止します。

AIが結果を作成
      ↓
HUMAN APPROVAL REQUIRED
      ↓
人間が確認

人間が承認するまで、
次のTaskには進みません。

04｜Hiroが結果を確認する

HiroはAIが作成した結果を確認します。

確認する情報は、

報告書
Knowledge Baseから取得した情報
AIの処理結果
実行履歴
関連資料

などです。

AIが結果を作ったことと、
その結果を採用してよいことは別の問題です。

そのため、重要な場面では人間が確認します。

05｜承認する

問題がなければ、人間が承認します。

HUMAN APPROVAL REQUIRED
          ↓
       APPROVE
          ↓
       APPROVED
          ↓
      次のTask

承認結果をWorkflow Engineが受け取り、
次のTaskへ進みます。

06｜Workflowが再開する

承認されるとWorkflowが再開します。

Task 01｜COMPLETED
Task 02｜COMPLETED
Task 03｜COMPLETED
Task 04｜APPROVED
Task 05｜IN PROGRESS
Task 06｜PENDING

人間がWorkflow全体を操作するのではなく、
必要な場所だけ判断します。

07｜承認しない場合

AIが作った結果に問題がある場合は、
人間が差し戻します。

例えば、

分析が不足している
データに問題がある
追加資料が必要
内容を修正する必要がある

といった場合です。

Human Approval
      ↓
    REJECT
      ↓
Taskを修正
      ↓
再実行
      ↓
Human Approval

RejectしてWorkflowを終了するのではなく、
修正して再実行する流れを作ることができます。

08｜AIと人間の共同Workflow

DAY64で実現した考え方です。

                 AI
                  ↓
          検索・分析・資料作成
                  ↓
                結果
                  ↓
        ┌────────────────┐
        │ Human Approval │
        └────────────────┘
                  ↓
          ┌───────┴───────┐
          ↓               ↓
       APPROVE           REJECT
          ↓               ↓
       次のTask        修正・再実行
          │
          ↓
       Workflow

AIが得意な仕事はAIが担当し、
重要な判断は人間が担当します。

Workflow Engineが、
AIと人間の作業をつなぎます。

DAY63 → DAY64
DAY63
Retry Limit
     ↓
Human Intervention

        ↓

DAY64
Human Approval
     ↓
Human-in-the-Loop

DAY63では、
問題が発生した場合に人間へ判断を戻しました。

DAY64では、
問題が発生していなくても、
重要なTaskに人間の承認ポイントを設定できるようにしました。

DAY53〜DAY64
DAY53  Knowledge Base
   ↓
DAY54  RAG Search
   ↓
DAY55  RAG Answer
   ↓
DAY56  AI Employee × RAG
   ↓
DAY57  AI Agent
   ↓
DAY58  Workflow
   ↓
DAY59  AI Employee Collaboration
   ↓
DAY60  Workflow State
   ↓
DAY61  Error Recovery
   ↓
DAY62  Automatic Retry
   ↓
DAY63  Retry Limit / Human Intervention
   ↓
DAY64  Human Approval / Human-in-the-Loop

RAGで会社の知識を利用し、
AI Agentで仕事を分解し、
Workflowで仕事を実行する。

そしてDAY64では、
AIと人間が共同で仕事を進める仕組みへ進みました。

🎯 DAY64のポイント

DAY64で重要なのは、
「AIにすべてを任せる」ことではありません。

AIが仕事を進める。

人間が重要な場面で確認・判断する。

そしてWorkflow Engineが、
AIと人間の作業をつなぐ。

この役割分担をWorkflowそのものに組み込みました。

🚀 Next Step

DAY64ではHuman-in-the-LoopをWorkflowに組み込みました。

次は、この仕組みをさらにCompany AI OSの
業務実行へつなげていきます。

100日でCompany AI OSを作る。

DAY65へ続きます。


### GitHubの構成

```text
DAY64/
├── day64.rpy
├── scene64_01.png
├── scene64_02.png
├── scene64_03.png
├── scene64_04.png
├── scene64_05.png
├── scene64_06.png
├── scene64_07.png
├── scene64_08.png
└── voice/
    └── day64/
        ├── day64_01.ogg
        ├── day64_02.ogg
        ├── day64_03.ogg
        ├── day64_04.ogg
        ├── day64_05.ogg
        ├── day64_06.ogg
        ├── day64_07.ogg
        └── day64_08.ogg



____________________________________________________________________________________________________________________________________________________________

# DAY65｜ApprovalがWorkflowを制御する

Company AI OS 開発100日チャレンジ DAY65。

DAY64では、Workflowの中に
Human Approvalを組み込みました。

DAY65では、そのApproval結果を
Workflow Engineに反映します。

人間の判断を単なる確認操作で終わらせず、
Workflowの次の処理を制御する情報として利用します。

---

## 🎯 DAY65のテーマ

**ApprovalがWorkflowを制御する**

基本的な流れは、

```text
AI社員
   ↓
Task実行
   ↓
結果作成
   ↓
Human Approval
   ↓
┌───────────────┐
│               │
APPROVE        REJECT
│               │
↓               ↓
Task完了       Workflow停止
│               ↓
↓            修正Task生成
次のTask        ↓
│            AI社員が修正
↓               ↓
Workflow     再びApproval
継続

です。

01｜承認結果をWorkflowへ渡す

DAY64では、人間がAIの結果を確認し、
ApproveまたはRejectを選択できるようにしました。

DAY65では、その結果をWorkflow Engineへ渡します。

Human Approval
      ↓
Approval Result
      ↓
Workflow Engine
02｜Workflowが承認結果を受け取る

Hiroが承認すると、

Task 04
HUMAN APPROVAL
      ↓
APPROVED

という結果がWorkflow Engineへ渡されます。

Workflow Engineは、この結果をもとに
Taskの状態を更新します。

03｜承認されたTaskを完了にする

承認されたTaskはWorkflow上でも完了になります。

PENDING APPROVAL
       ↓
APPROVED
       ↓
COMPLETED

これによってWorkflow Engineは、
Task 04が完了したことを認識できます。

04｜次のTaskを開始する

Task 04が完了すると、
Workflow Engineは次のTaskを開始します。

Task 04
COMPLETED
     ↓
Task 05
PENDING
     ↓
RUNNING

人間の承認をきっかけとして、
Workflowが自動的に次のTaskへ進みます。

05｜Rejectの場合

人間が結果を承認できない場合は、
REJECTを選択します。

Human Approval
      ↓
    REJECT
      ↓
Workflow PAUSED

Workflowは次のTaskへ進みません。

06｜修正Taskを生成する

Rejectされた場合、
Workflowは必要な修正Taskを生成します。

例えば、

修正Task

・競合分析を追加
・最新の市場データを反映
・グラフの根拠を明確化
・結論部分を再構成

などです。

REJECT
  ↓
修正内容
  ↓
Correction Task
  ↓
AI社員

AI社員が修正Taskを実行します。

07｜修正後に再び承認する

修正Taskが完了すると、
再びHuman Approvalを行います。

REJECT
 ↓
修正Task
 ↓
AI社員が修正
 ↓
修正版
 ↓
Human Approval

問題がなければ、再びApproveします。

これによって、

Reject
 ↓
修正
 ↓
再承認

というWorkflowのループが完成します。

08｜ApprovalがWorkflowを制御する

DAY65で完成した全体像です。

                 AI社員
                    ↓
                 Task実行
                    ↓
                 結果作成
                    ↓
           ┌────────────────┐
           │ Human Approval │
           └────────────────┘
                 ↓       ↓
              APPROVE   REJECT
                 ↓       ↓
              Task完了  Workflow停止
                 ↓       ↓
              次のTask  修正Task生成
                 ↓       ↓
              Workflow  AI社員が修正
                 ↓       ↓
                 └──→ 再承認

Human Approvalは単なる確認操作ではありません。

人間の判断そのものが、Workflowの次の動きを決めます。

DAY64 → DAY65
DAY64
Human Approval
        ↓
人間が承認・差し戻しを判断

        ↓

DAY65
Approval Result
        ↓
Workflow Engine
        ↓
次のTask / 修正Task

DAY64で「人間が承認できる仕組み」を作り、
DAY65では「その判断によってWorkflowが動く仕組み」へ進みました。

DAY53〜DAY65
DAY53  Knowledge Base
   ↓
DAY54  RAG Search
   ↓
DAY55  RAG Answer
   ↓
DAY56  AI Employee × RAG
   ↓
DAY57  AI Agent
   ↓
DAY58  Workflow
   ↓
DAY59  AI Employee Collaboration
   ↓
DAY60  Workflow State
   ↓
DAY61  Error Recovery
   ↓
DAY62  Automatic Retry
   ↓
DAY63  Retry Limit / Human Intervention
   ↓
DAY64  Human Approval
   ↓
DAY65  Approval Result → Workflow
🎯 DAY65のポイント

DAY65では、

AIが仕事を実行する

↓

人間が重要な場面で判断する

↓

Workflowがその判断を受け取る

↓

次のTaskまたは修正Taskへ進む

という仕組みを作りました。

AIと人間の役割をWorkflowの中に組み込むことで、
AIだけでも、人間だけでもない
共同作業の仕組みに近づいています。

🚀 Next Step

DAY64ではHuman Approvalを実装しました。

DAY65ではApproval結果によって
Workflowを制御できるようにしました。

次は、この仕組みをさらに
Company AI OSの業務実行へつなげていきます。

100日でCompany AI OSを作る。

DAY66へ続きます。


### GitHubに追加するファイル

```text
DAY65/
├── day65.rpy
├── scene65_01.png
├── scene65_02.png
├── scene65_03.png
├── scene65_04.png
├── scene65_05.png
├── scene65_06.png
├── scene65_07.png
├── scene65_08.png
└── voice/
    └── day65/
        ├── day65_01.ogg
        ├── day65_02.ogg
        ├── day65_03.ogg
        ├── day65_04.ogg
        ├── day65_05.ogg
        ├── day65_06.ogg
        ├── day65_07.ogg
        └── day65_08.ogg

____________________________________________________________________________________________________________________________________________________________

# DAY66｜Workflowが実際の仕事を動かす

Company AI OSを100日で作るプロジェクト DAY66。

DAY65では、Human Approvalの結果をWorkflowへ反映し、
人間の判断によって次のTaskを制御できるようにしました。

DAY66では、その承認されたTaskを、
実際の業務としてAI社員に実行させるところまで進めます。

---

## 1. DAY66のテーマ

**Workflowが実際の仕事を動かす**

これまでのWorkflowは、Taskの状態や実行順序を
管理することが中心でした。

DAY66では、Workflow EngineからAI社員へTaskを渡し、
AI社員が実際の業務を実行します。

その結果をWorkflowへ戻し、
結果を確認したうえで次のTaskを自動的に開始します。

---

## 2. DAY66のWorkflow

基本的な流れは次のようになります。

```text
Human Approval
       ↓
    APPROVED
       ↓
Workflow Engine
       ↓
実行Taskを決定
       ↓
AI社員へTaskを渡す
       ↓
AI社員が業務を実行
       ↓
業務結果をWorkflowへ返す
       ↓
Workflowが結果を確認
       ↓
次のTaskを自動実行
3. 承認されたTaskを実行する

DAY65でHuman ApprovalがAPPROVEDになると、
Workflowは次の処理へ進みます。

Human Approval
       ↓
    APPROVED
       ↓
Workflow Engine
       ↓
実行開始

承認されたTaskを、
実際の業務として実行する段階へ進みます。

4. Workflowが実行Taskを決定する

Workflow Engineは現在のTask状態を確認し、
次に実行できるTaskを決定します。

例えば、

Task 01  COMPLETED
Task 02  COMPLETED
Task 03  COMPLETED
Task 04  APPROVED
Task 05  READY
Task 06  PENDING

という状態であれば、
Task 05を次の実行Taskとして選択します。

5. AI社員へTaskを渡す

Workflow Engineが決定したTaskを
担当するAI社員へ渡します。

Taskだけではなく、必要な情報も一緒に渡します。

Workflow Engine
       ↓
Task
       ↓
入力データ
参照Knowledge Base
実行条件
完了条件
出力形式
       ↓
AI社員

これにより、AI社員は
Workflowから与えられた仕事を実行できます。

6. AI社員が業務を実行する

AI社員はTaskを受け取ると、
必要な情報を取得して業務を実行します。

例えば、

Knowledge Baseを検索
       ↓
必要な資料を取得
       ↓
データを分析
       ↓
資料を作成
       ↓
結果を整理

DAY53以降で構築してきたKnowledge BaseやRAGを、
AI社員の実際の業務に利用します。

7. 業務結果をWorkflowへ返す

AI社員が業務を完了すると、
実行結果をWorkflow Engineへ返します。

AI社員
   ↓
実行結果
   ↓
Workflow Engine

Workflow Engineは結果を受け取り、
Taskの状態を更新します。

例えば、

Task 05
STATUS: SUCCESS

OUTPUT:
final_report.md

のような結果をWorkflowへ返します。

8. Workflowが結果を確認する

Workflow Engineは、
AI社員から返された結果を確認します。

確認する内容の例：

Taskが正常終了したか
エラーが発生していないか
出力ファイルが存在するか
必要な条件を満たしているか

正常終了の場合：

SUCCESS
   ↓
次のTask

問題が発生した場合：

ERROR
   ↓
Error Recovery
   ↓
Human Intervention

という流れにつなげます。

9. 次のTaskを自動実行する

Task 05が正常に完了すると、
Workflow Engineは次のTaskを開始します。

Task 05
COMPLETED
    ↓
Task 06
RUNNING

ここでは、人間が毎回Taskを開始する必要はありません。

Workflow EngineがTaskの状態を確認しながら、
次の処理を進めます。

10. Workflowが実際の仕事を動かす

DAY66では、Workflowの役割が一段階広がりました。

Workflowは単にTaskの順番を管理するだけではありません。

承認されたTask
       ↓
実行Taskを決定
       ↓
AI社員へTaskを渡す
       ↓
AI社員が業務を実行
       ↓
結果をWorkflowへ返す
       ↓
結果を確認
       ↓
次のTaskを実行

この流れによって、
Workflowが実際の仕事を動かす仕組みになります。

11. DAY53〜DAY66の流れ

DAY53から構築してきた仕組みをつなげると、
次のようになります。

Knowledge Base
      ↓
RAG
      ↓
AI社員
      ↓
AI Agent
      ↓
Task分解
      ↓
Execution Plan
      ↓
Workflow Engine
      ↓
AI社員へTask
      ↓
業務実行
      ↓
結果
      ↓
Workflow
      ↓
次のTask

さらに重要な処理では、

Human Approval
       ↓
Approve / Reject
       ↓
Workflow

という人間の判断も組み込まれています。

12. DAY66で実現したこと

DAY57ではAI Agentが仕事を分解し、
実行計画を作りました。

DAY58ではWorkflowが、
その計画に沿ってTaskを実行しました。

DAY59では複数のAI社員を
Workflowで連携しました。

DAY60〜DAY62では、
Workflowの状態管理と自動Retryを追加しました。

DAY63ではRetry上限と
Human Interventionを追加しました。

DAY64〜DAY65では、
Human ApprovalをWorkflowに組み込みました。

そしてDAY66では、

WorkflowからAI社員へ実際の仕事を渡し、
その結果を受け取って次のTaskを動かす

ところまでつながりました。

13. DAY66の位置づけ

Company AI OSは、

AI社員
   +
Knowledge Base
   +
RAG
   +
AI Agent
   +
Workflow
   +
Human-in-the-Loop

を組み合わせながら、
AIが実際の会社業務を進められる仕組みへ発展しています。

DAY66では、その中でも

Workflow → AI社員 → 結果 → Workflow

という実行ループを構築しました。

14. 次のステップ

DAY66で、Workflowによる業務実行の
基本的な流れができました。

次は、この仕組みをさらに実際の会社業務へ
広げていきます。

仕事の依頼
    ↓
Task
    ↓
実行
    ↓
結果
    ↓
次の処理

Company AI OSの中で、
この一連の業務を扱えるようにしていきます。

Project Structure
DAY66/
├── day66.rpy
├── scene66_01.png
├── scene66_02.png
├── scene66_03.png
├── scene66_04.png
├── scene66_05.png
├── scene66_06.png
├── scene66_07.png
├── scene66_08.png
└── voice/
    └── day66/
        ├── day66_01.ogg
        ├── day66_02.ogg
        ├── day66_03.ogg
        ├── day66_04.ogg
        ├── day66_05.ogg
        ├── day66_06.ogg
        ├── day66_07.ogg
        └── day66_08.ogg
DAY66 Summary

WorkflowがAI社員へ仕事を渡し、
実際の業務を実行し、
結果を受け取って次のTaskを動かす。

これがDAY66のポイントです。

DAY53〜DAY66
DAY53  Knowledge Base
   ↓
DAY54  RAG Search
   ↓
DAY55  RAG Answer
   ↓
DAY56  AI Employee × RAG
   ↓
DAY57  AI Agent
   ↓
DAY58  Workflow
   ↓
DAY59  AI Employee Collaboration
   ↓
DAY60  Workflow State
   ↓
DAY61  Error Recovery
   ↓
DAY62  Automatic Retry
   ↓
DAY63  Human Intervention
   ↓
DAY64  Human Approval
   ↓
DAY65  Approval Result
   ↓
DAY66  Workflow Execution

____________________________________________________________________________________________________________________________________________________________

# DAY67｜AI社員が結果をつないで仕事を完成させる

Company AI OSを100日で作るプロジェクト DAY67。

DAY66では、WorkflowからAI社員へTaskを渡し、
実際の業務を実行できるようにしました。

DAY67では、その次の段階として、
**前のTaskの結果を次のTaskへ引き継ぐ仕組み**
を構築します。

---

## 1. DAY67のテーマ

**AI社員が結果をつないで仕事を完成させる**

会社の仕事は、一つのTaskだけで終わるとは限りません。

```text
Task
 ↓
AI社員
 ↓
Result
 ↓
Next Task
 ↓
AI社員
 ↓
Result
 ↓
Final Result

前のTaskで作られた結果を、
次のTaskの入力として利用します。

これによって、複数のTaskを一つの業務フローとして
つなげることができます。

2. DAY66からDAY67へ

DAY66では、

Workflow
   ↓
AI社員
   ↓
業務実行
   ↓
Result

という流れを作りました。

DAY67では、さらにその結果を次のTaskへ渡します。

Workflow
   ↓
AI社員A
   ↓
Result
   ↓
Next Task
   ↓
AI社員B
   ↓
Result
   ↓
Final Result
3. 前のTaskが完了する

まず、前のTaskが正常に完了します。

Task 04｜報告書作成
STATUS: COMPLETED

OUTPUT:
・report.pdf
・analysis_data.csv
・summary.md

AI社員が業務を実行し、
報告書や分析データなどの成果物を作成します。

4. Workflowが実行結果を受け取る

AI社員が業務を完了すると、
実行結果がWorkflow Engineへ返されます。

AI社員
   ↓
実行結果
   ↓
Workflow Engine

Workflow Engineは、

結果を受け取る
ファイルを確認する
内容を確認する
Taskの状態を更新する
次のTaskを準備する

といった処理を行います。

5. 結果を次のTaskへ渡す

DAY67の重要なポイントです。

Task 04の結果を、
Task 05の入力として渡します。

Task 04
報告書作成
   ↓
実行結果
   ↓
Task 05
最終確認

例えば、

report.pdf
analysis_data.csv
summary.md

などがTask 05で利用されます。

6. 次のAI社員が結果を受け取る

Task 05を担当するAI社員が、
前のTaskの結果を受け取ります。

Task 04の結果
       ↓
Workflow Engine
       ↓
Task 05
       ↓
AI社員B

ここで重要なのは、
AI社員同士が直接通信するわけではないことです。

Workflow Engineが間に入り、
TaskとResultを管理します。

7. 前の結果を使って業務を実行する

AI社員Bは、受け取った結果を利用して
Task 05を実行します。

例えば、

受け取った結果
      ↓
入力データを確認
      ↓
内容を分析
      ↓
報告書をチェック
      ↓
最終確認

という処理を行います。

前のTaskの結果が、
次のTaskを実行するための入力になります。

8. 新しい結果をWorkflowへ返す

Task 05の処理が完了すると、
AI社員Bは新しい結果をWorkflow Engineへ返します。

AI社員B
   ↓
新しい実行結果
   ↓
Workflow Engine

Workflow Engineは結果を受け取り、
Task 05の状態を更新します。

そして、さらに次のTaskへ進む準備をします。

9. 結果がTaskからTaskへ引き継がれる

Taskを連続させることで、
結果が次の仕事へ引き継がれていきます。

Task 01
データ収集
   ↓
Result
   ↓
Task 02
データ分析
   ↓
Result
   ↓
Task 03
レポート作成
   ↓
Final Result

それぞれのTaskが独立して動くのではなく、
前のTaskの結果を使って次のTaskが動きます。

10. AI社員が結果をつないで仕事を完成させる

最終的には、

Task 01
   ↓
AI社員A
   ↓
Result
   ↓
Task 02
   ↓
AI社員B
   ↓
Result
   ↓
Task 03
   ↓
AI社員C
   ↓
Final Result

という流れになります。

例えば、

AI社員A：データを収集
AI社員B：データを分析
AI社員C：レポートを作成

というように役割を分担できます。

それぞれのAI社員が作った結果を次のTaskへ渡すことで、
最終的に一つの成果物を完成させます。

11. DAY67のポイント

DAY67では、

AI社員が単独で仕事をする

ところから、

前の仕事の結果を使って次の仕事をする

ところへ進みました。

仕事A
 ↓
結果A
 ↓
仕事B
 ↓
結果B
 ↓
仕事C
 ↓
最終成果物

この「結果の連鎖」によって、
複数のTaskを一つの業務フローとして扱えるようになります。

12. Workflow Engineの役割

DAY67ではWorkflow Engineが
Task間の結果をつなぐ役割を担います。

AI社員A
   ↓
Result
   ↓
Workflow Engine
   ↓
Next Task
   ↓
AI社員B
   ↓
Result
   ↓
Workflow Engine

AI社員同士を直接接続するのではなく、
Workflow Engineを中心にして業務をつなぎます。

13. DAY53〜DAY67

これまで構築してきた仕組みは、
次のようにつながっています。

DAY53  Knowledge Base
   ↓
DAY54  RAG Search
   ↓
DAY55  RAG Answer
   ↓
DAY56  AI Employee × RAG
   ↓
DAY57  AI Agent
   ↓
DAY58  Workflow
   ↓
DAY59  AI Employee Collaboration
   ↓
DAY60  Workflow State
   ↓
DAY61  Error Recovery
   ↓
DAY62  Automatic Retry
   ↓
DAY63  Human Intervention
   ↓
DAY64  Human Approval
   ↓
DAY65  Approval Result
   ↓
DAY66  Workflow Execution
   ↓
DAY67  Result Handoff

DAY67では、
Taskの結果を次のTaskへ引き継ぐ
仕組みを追加しました。

14. DAY67の位置づけ

Company AI OSでは、

Knowledge
    ↓
AI
    ↓
Task
    ↓
Workflow
    ↓
Execution
    ↓
Result
    ↓
Next Task

という業務の流れが、
少しずつ具体的になってきています。

DAY67では、
Workflowによって結果を次のTaskへ渡し、
仕事を連続して実行できる形へ進めました。

15. Project Structure
DAY67/
├── day67.rpy
├── scene67_01.png
├── scene67_02.png
├── scene67_03.png
├── scene67_04.png
├── scene67_05.png
├── scene67_06.png
├── scene67_07.png
├── scene67_08.png
└── voice/
    └── day67/
        ├── day67_01.ogg
        ├── day67_02.ogg
        ├── day67_03.ogg
        ├── day67_04.ogg
        ├── day67_05.ogg
        ├── day67_06.ogg
        ├── day67_07.ogg
        └── day67_08.ogg
16. Extended description
Company AI OS

100日でCompany AI OSを作るプロジェクト。

DAY67では、前のTaskで作られた結果を次のTaskへ引き継ぎ、
AI社員が結果を利用しながら一つの仕事を完成させる流れを構築しました。

Workflow Engineを中心に、

AI社員
 ↓
Result
 ↓
Next Task
 ↓
AI社員
 ↓
Result
 ↓
Final Result

という業務の連鎖を作ります。

DAY67では、

AI社員が結果をつないで仕事を完成させる

ところまで進みました。

____________________________________________________________________________________________________________________________________________________________

# DAY68｜会社のファイルをAI社員が業務に利用する

Company AI OSを100日で作るプロジェクト。

DAY68では、これまで構築してきたWorkflowとAI社員の仕組みに、
「会社のファイル」を接続します。

会社には、報告書、売上データ、会議議事録、企画資料、
顧客データなど、多くのファイルがあります。

AI社員が実際に会社の仕事をするためには、
Taskを実行するだけではなく、
会社に蓄積された情報を取得して利用できる必要があります。

## DAY68の流れ

```text
会社のファイル
      ↓
File Management
      ↓
Workflow
      ↓
必要なファイルを取得
      ↓
AI社員
      ↓
ファイル内容を確認
      ↓
Taskで利用
      ↓
ファイルを処理
      ↓
処理結果
      ↓
Workflowへ返す
      ↓
次のTask
主な処理
1. 会社のファイルを管理

会社で利用するファイルを管理できるようにします。

PDF
Excel
Word
CSV
画像
プロジェクト資料
2. 必要なファイルを取得

AI社員がTaskを実行するとき、
そのTaskに必要なファイルを取得します。

すべてのファイルをAI社員へ渡すのではなく、
業務に必要なファイルを扱うことを想定しています。

3. ファイルの内容を確認

取得したファイルから、
Taskに必要な情報を確認します。

PDF
 ↓
文章・内容

Excel
 ↓
データ

議事録
 ↓
会議内容

画像
 ↓
画像情報
4. Taskでファイル情報を利用

取得した情報をTaskの処理に利用します。

例えば、

報告書の確認
売上データの分析
議事録の整理
企画内容の確認
必要な資料の作成

などです。

5. AI社員がファイルを処理

AI社員がファイルの情報を利用して、
データ分析、情報抽出、文章整理、レポート作成などの処理を行います。

6. 結果をWorkflowへ返す

処理が完了すると、
AI社員は結果をWorkflow Engineへ返します。

AI社員
   ↓
処理結果
   ↓
Workflow Engine
   ↓
Task状態を更新
   ↓
次のTask
DAY67とのつながり

DAY67では、

「前のTaskの結果を次のTaskへ引き継ぐ」

仕組みを作りました。

DAY68では、そこに

「会社のファイルをTaskの入力として利用する」

仕組みを加えました。

その結果、

会社のファイル
      ↓
Workflow
      ↓
AI社員
      ↓
Task
      ↓
処理
      ↓
結果
      ↓
Workflow
      ↓
次のTask

という、より実際の業務に近い流れになります。

DAY68のポイント

DAY68では、

会社のファイルをAI社員の業務へつなげる

ところまで進みました。

Company AI OSが、
AI社員へ仕事を依頼するだけではなく、
会社に蓄積された情報を利用して仕事を進める構造へ進みます。

Project Structure
DAY68/
├── day68.rpy
├── scene68_01.png
├── scene68_02.png
├── scene68_03.png
├── scene68_04.png
├── scene68_05.png
├── scene68_06.png
├── scene68_07.png
├── scene68_08.png
└── voice/
    └── day68/
        ├── day68_01.ogg
        ├── day68_02.ogg
        ├── day68_03.ogg
        ├── day68_04.ogg
        ├── day68_05.ogg
        ├── day68_06.ogg
        ├── day68_07.ogg
        └── day68_08.ogg
DAY68

会社のファイルをAI社員が取得し、
Taskで利用して処理する。

そして、その結果をWorkflowへ返す。

DAY68では、
Company AI OSを「会社の情報を使って仕事をする仕組み」へ
一歩進めました。

DAY68は、DAY53のKnowledge Base/RAG → DAY67のWorkflow → DAY68の会社ファイルという流れがつながる重要な回になっています。

____________________________________________________________________________________________________________________________________________________________

# DAY69｜会議の情報を実際の業務へつなげる

Company AI OSを100日で作るプロジェクト。

DAY69では、会議で生まれた情報をAI社員が確認し、
具体的なTaskへ変換してWorkflowへ渡す流れを構築しました。

会議が終わった後に残る議事録を、
単なる保存データとして扱うのではなく、
実際の業務を開始するための入力情報として利用します。

## DAY69のテーマ

**会議の情報を実際の業務へつなげる**

## DAY69の流れ

```text
会議
 ↓
会議議事録
 ↓
AI社員が取得
 ↓
議事録の内容を確認
 ↓
重要情報を抽出
 ↓
決定事項・アクションを整理
 ↓
Taskを作成
 ↓
Workflowへ登録
 ↓
実際の業務開始

1. 会議の情報が残っている

会社の会議では、さまざまな情報が生まれます。

会議の議題
議論内容
決定事項
担当者
期限
次のアクション

これらの情報は、会議議事録や関連資料として
会社のファイルに保存されます。

2. 会議議事録をAI社員が取得する

WorkflowからTaskが実行されると、
AI社員が必要な会議議事録を取得します。

Workflow
 ↓
Task
 ↓
必要なファイルを取得
 ↓
AI社員

必要なファイルだけを取得し、
Taskの処理に利用します。

3. 議事録の内容を確認する

AI社員は取得した議事録を確認します。

会議概要
議題
議論内容
決定事項
次のアクション

議事録の内容を確認することで、
会議で何が話され、何が決まったのかを整理します。

4. 重要な情報を抽出する

議事録から業務に必要な情報を抽出します。

決定事項
担当者
期限
課題
検討事項

文章として保存されている会議情報を、
業務で利用できる情報へ変換します。

5. 決定事項とTaskを整理する

会議で決まった内容を具体的なTaskへ変換します。

例えば、

決定事項
「新製品の開発を進める」

↓

Task
・市場調査
・企画書作成
・マーケティング計画
・開発スケジュール作成

というように、
会議の決定事項を具体的な作業へ変換します。

6. AI社員が次のTaskを作る

AI社員が議事録の内容から、
次に実行するTaskを作成します。

Taskには、

Task内容
担当AI社員
期限
優先度

などの情報を整理します。

議事録
 ↓
決定事項
 ↓
必要な業務
 ↓
Task
7. TaskをWorkflowへ渡す

作成されたTaskをWorkflow Engineへ登録します。

AI社員
 ↓
Task
 ↓
Workflow Engine
 ↓
実行順序
 ↓
担当AI社員
 ↓
業務実行

DAY67までに構築したWorkflowの仕組みと接続し、
会議から作られたTaskを実際の業務へつなげます。

8. 会議から実際の業務が始まる

DAY69では、次の流れが完成しました。

会議
 ↓
議事録
 ↓
AI社員
 ↓
情報抽出
 ↓
Task作成
 ↓
Workflow
 ↓
業務開始

会議で生まれた情報が、
Company AI OSを通して実際の仕事へつながります。

DAY68とのつながり

DAY68では、

会社のファイルをAI社員が扱う

ところまで進みました。

DAY69では、そのファイルの中にある
会議議事録を利用して、

会議の情報からTaskを作る

ところまで進めました。

DAY68
会社のファイル
 ↓
AI社員が利用

DAY69
会社のファイル
 ↓
会議議事録
 ↓
重要情報
 ↓
Task
 ↓
Workflow
 ↓
業務
DAY69のポイント

DAY69のポイントは、

「会議で決まったことを、AI社員が仕事に変える」

ということです。

会議で生まれた情報を保存するだけではなく、
AI社員が内容を確認し、重要情報を抽出し、
具体的なTaskへ変換します。

そして、そのTaskをWorkflowへ渡すことで、
実際の業務へつなげます。

Company AI OSが、
会社の情報を扱うだけではなく、
その情報を使って仕事を動かす仕組みへ進みました。

Project Structure
DAY69/
├── day69.rpy
├── scene69_01.png
├── scene69_02.png
├── scene69_03.png
├── scene69_04.png
├── scene69_05.png
├── scene69_06.png
├── scene69_07.png
├── scene69_08.png
└── voice/
    └── day69/
        ├── day69_01.ogg
        ├── day69_02.ogg
        ├── day69_03.ogg
        ├── day69_04.ogg
        ├── day69_05.ogg
        ├── day69_06.ogg
        ├── day69_07.ogg
        └── day69_08.ogg
DAY69

会議の情報をAI社員が取得し、
重要な情報を抽出する。

その情報からTaskを作り、
Workflowへ渡す。

会議の情報が、実際の業務へつながる。

DAY69では、Company AI OSを
さらに「仕事を動かす仕組み」へ進めました。

____________________________________________________________________________________________________________________________________________________________

# DAY70｜AI社員に仕事を割り当てる

Company AI OSを100日で作るプロジェクト。

DAY70では、DAY69で作成したTaskを確認し、
それぞれのTaskに適したAI社員を割り当てる流れを構築しました。

DAY69では、

会議
↓
議事録
↓
情報抽出
↓
Task作成

まで進みました。

DAY70では、その次の段階として、

Task
↓
必要な仕事を確認
↓
AI社員の役割を確認
↓
TaskとAI社員を照合
↓
担当AI社員を決定
↓
Workflowへ登録
↓
AI社員へTaskを渡す
↓
業務開始

という流れを作ります。

## DAY70のテーマ

**AI社員に仕事を割り当てる**

---

## 01｜作成されたTaskを確認する

DAY69で会議議事録から作成されたTaskを確認します。

```text
Task 01｜市場調査
Task 02｜企画書作成
Task 03｜マーケティング計画
Task 04｜開発スケジュール

これから実行する仕事を整理します。

02｜Taskごとに必要な仕事が違う

Taskによって必要となる仕事が異なります。

市場調査
→ 情報収集・分析

企画書作成
→ 企画・文章作成

マーケティング計画
→ マーケティング・分析

開発スケジュール
→ 技術・スケジュール管理

そのため、Taskの内容に応じて担当するAI社員を分けます。

03｜AI社員の役割を確認する

Company AI OSには、それぞれ異なる役割を持つAI社員があります。

AI社員A｜調査担当
AI社員B｜企画担当
AI社員C｜マーケティング担当
AI社員D｜開発担当

AI社員の役割とTaskの内容を対応させます。

04｜TaskとAI社員を照合する

Taskを実行するために必要な能力を確認し、
AI社員の役割と照合します。

Task
 ↓
必要な能力を確認
 ↓
AI社員の役割を確認
 ↓
候補AI社員を照合

Taskの内容に応じて担当候補を決めます。

05｜担当AI社員を決定する

Taskごとに担当AI社員を決定します。

市場調査
↓
調査担当AI社員

企画書作成
↓
企画担当AI社員

マーケティング計画
↓
マーケティング担当AI社員

開発スケジュール
↓
開発担当AI社員

これで、それぞれのTaskの担当者が決まります。

06｜Workflowに担当者を登録する

決定した担当AI社員をWorkflow Engineへ登録します。

Task
 ↓
担当AI社員
 ↓
Workflow Engine

WorkflowがTaskと担当AI社員の関係を管理できるようにします。

07｜AI社員へTaskが渡される

Workflow Engineから、それぞれの担当AI社員へTaskを渡します。

Workflow Engine
 ├─→ AI社員A｜市場調査
 ├─→ AI社員B｜企画書作成
 ├─→ AI社員C｜マーケティング
 └─→ AI社員D｜開発

AI社員同士が直接Taskを渡すのではなく、
Workflow Engineが仲介します。

08｜AI社員が自分の仕事を開始する

Taskの割り当てが完了すると、
それぞれのAI社員が担当する仕事を開始します。

会議
 ↓
議事録
 ↓
Task作成
 ↓
TaskとAI社員を照合
 ↓
担当AI社員を決定
 ↓
Workflow
 ↓
AI社員
 ↓
業務開始

会議で決まった内容が、
実際のAI社員の仕事として動き始めます。

DAY69とのつながり

DAY69では、

会議の情報からTaskを作る

ところまで進みました。

DAY70では、

作成したTaskをAI社員へ割り当てる

ところまで進めました。

DAY69
会議
 ↓
議事録
 ↓
情報抽出
 ↓
Task作成

DAY70
 ↓
Task確認
 ↓
AI社員の役割確認
 ↓
TaskとAI社員を照合
 ↓
担当者決定
 ↓
Workflow
 ↓
AI社員が業務開始

Company AI OSでは、AI社員が増えるほど、
「誰がどの仕事を担当するのか」を管理する仕組みが重要になります。

DAY70では、その基本となるTask Assignmentの流れを構築しました。

Project Structure
DAY70/
├── day70.rpy
├── scene70_01.png
├── scene70_02.png
├── scene70_03.png
├── scene70_04.png
├── scene70_05.png
├── scene70_06.png
├── scene70_07.png
├── scene70_08.png
└── voice/
    └── day70/
        ├── day70_01.ogg
        ├── day70_02.ogg
        ├── day70_03.ogg
        ├── day70_04.ogg
        ├── day70_05.ogg
        ├── day70_06.ogg
        ├── day70_07.ogg
        └── day70_08.ogg
DAY70のポイント

DAY70では、

Taskの内容に応じて担当AI社員を決定し、
WorkflowからそのAI社員へ仕事を渡す

という仕組みを作りました。

Task
 ↓
Task Assignment
 ↓
Workflow Engine
 ↓
AI Employee
 ↓
Work

これによって、Company AI OSは
「AI社員が存在する」だけではなく、

AI社員へ仕事を割り当て、実際に仕事を開始させる

段階へ進みました。

DAY71へ続きます。

____________________________________________________________________________________________________________________________________________________________

# DAY71｜WorkflowがAI社員の仕事を管理する

Company AI OSを100日で作るプロジェクト。

DAY70では、作成されたTaskを担当するAI社員を決定し、
WorkflowからAI社員へ仕事を渡すところまで進めました。

DAY71では、その先に進みます。

AI社員がTaskを開始した後、
Workflow Engineが仕事の進捗を確認し、
Taskの状態を更新していく仕組みを構築しました。

## DAY71のテーマ

**WorkflowがAI社員の仕事を管理する**

---

## DAY71の流れ

```text
AI社員がTaskを開始
 ↓
WorkflowがTaskの進行を確認
 ↓
AI社員が作業を進める
 ↓
Taskの進捗をWorkflowへ返す
 ↓
Workflowが進捗を更新
 ↓
作業中のTaskを確認
 ↓
完了したTaskを次へ進める
 ↓
WorkflowがAI社員の仕事を管理
01｜AI社員がTaskを開始する

DAY70で担当AI社員へのTaskの割り当てが完了しました。

DAY71では、AI社員が実際にTaskを受け取り、
担当する仕事を開始します。

Workflow
 ↓
Task
 ↓
担当AI社員
 ↓
Task開始
02｜WorkflowがTaskの進行を確認する

AI社員が作業を開始すると、
Workflow EngineがTaskの進行状況を確認します。

例えば、

Task 01｜市場調査
進捗：70%

Task 02｜企画書作成
進捗：45%

Task 03｜マーケティング計画
進捗：30%

Task 04｜開発スケジュール
進捗：0%

のように、各Taskの状態を管理します。

03｜AI社員が作業を進める

それぞれのAI社員が担当するTaskを実行します。

調査担当AI社員
→ 市場調査

企画担当AI社員
→ 企画書作成

マーケティング担当AI社員
→ マーケティング計画

開発担当AI社員
→ 開発スケジュール

AI社員ごとに異なるTaskを進めることができます。

04｜Taskの進捗をWorkflowへ返す

AI社員は作業の進捗状況をWorkflowへ返します。

AI社員
 ↓
作業
 ↓
進捗情報
 ↓
Workflow Engine

例えば、

市場調査
70%
 ↓
90%

のように、現在の進捗を報告します。

05｜Workflowが進捗を更新する

Workflow EngineはAI社員から受け取った進捗情報をもとに、
Taskの状態を更新します。

Task
├── 担当AI社員
├── 進捗率
├── ステータス
└── 更新時刻

これによって、Workflow上のTaskを
最新の状態に保つことができます。

06｜作業中のTaskを確認する

Workflowの画面から、
現在作業中のTaskを確認できます。

Task 01｜市場調査
担当：調査担当AI社員
進捗：70%
状態：作業中

Task 02｜企画書作成
担当：企画担当AI社員
進捗：45%
状態：作業中

Task 03｜マーケティング計画
担当：マーケティング担当AI社員
進捗：30%
状態：作業中

AI社員が現在何をしているのか、
どこまで進んでいるのかを確認できます。

07｜完了したTaskを次へ進める

Taskが完了すると、
AI社員からWorkflowへ結果が返されます。

Task完了
 ↓
Workflowが確認
 ↓
次の工程を決定
 ↓
次のTaskへ

これによって、完了したTaskを
次の工程へつなげることができます。

08｜WorkflowがAI社員の仕事を管理する

DAY71では、AI社員へTaskを渡すだけではなく、

Task
 ↓
担当AI社員
 ↓
Task開始
 ↓
作業
 ↓
進捗報告
 ↓
Workflowが状態更新
 ↓
Task完了
 ↓
次の工程

という一連の流れをWorkflow Engineで管理します。

DAY70とのつながり

DAY70では、

TaskをAI社員へ割り当てる

ところまで進みました。

DAY71では、

AI社員の仕事の進行をWorkflowで管理する

ところまで進めました。

DAY70
Task
 ↓
担当AI社員を決定
 ↓
AI社員へTaskを渡す

DAY71
 ↓
AI社員がTask開始
 ↓
作業
 ↓
進捗をWorkflowへ返す
 ↓
Workflowが状態更新
 ↓
完了Taskを次へ進める
DAY71のポイント

DAY71のポイントは、

「AI社員に仕事を任せる」だけではなく、
「任せた仕事をWorkflowが管理する」

ことです。

AI社員が増えるほど、

誰が仕事をしているのか
何をしているのか
どこまで進んでいるのか
何が完了したのか
次に何をするのか

を管理する必要があります。

Workflow Engineがその仕事の流れを管理することで、
複数のAI社員による業務を一つのWorkflowとして扱えるようになります。

DAY71では、Company AI OSを
「AI社員へ仕事を渡す仕組み」から、
「AI社員の仕事全体を管理する仕組み」
へ進めました。

DAY72へ続きます。

Project Structure
DAY71/
├── day71.rpy
├── scene71_01.png
├── scene71_02.png
├── scene71_03.png
├── scene71_04.png
├── scene71_05.png
├── scene71_06.png
├── scene71_07.png
├── scene71_08.png
└── voice/
    └── day71/
        ├── day71_01.ogg
        ├── day71_02.ogg
        ├── day71_03.ogg
        ├── day71_04.ogg
        ├── day71_05.ogg
        ├── day71_06.ogg
        ├── day71_07.ogg
        └── day71_08.ogg

____________________________________________________________________________________________________________________________________________________________

# DAY72｜Taskの結果をWorkflowで管理する

Company AI OS 開発 DAY72。

DAY71では、WorkflowによってAI社員のTaskの進捗を管理しました。

DAY72では、その次の段階として、
Taskが完了した後の「結果」をWorkflowで管理する仕組みを整理しました。

## 今回のテーマ

**Taskの結果をWorkflowで管理する**

AI社員がTaskを完了すると、
その成果物をWorkflowへ返します。

WorkflowはTaskの完了を確認し、
結果を保存します。

そして、その結果を次のTaskへ引き渡します。

```text
AI社員がTaskを完了
        ↓
結果をWorkflowへ返す
        ↓
WorkflowがTaskの完了を確認
        ↓
Workflowが結果を保存
        ↓
次のTaskへ結果を渡す
        ↓
次のAI社員が結果を利用
DAY72のポイント

今回重要なのは、
AI社員同士が直接結果を受け渡すのではなく、

Workflowが結果の受け渡しを管理する

という考え方です。

例えば、

Task 01
市場調査
   ↓
市場調査レポート
   ↓
Task 02
企画書作成
   ↓
企画書
   ↓
Task 03
マーケティング計画

というように、
一つのTaskで作られた成果物を
次のTaskへ引き継ぐことができます。

Taskの状態と結果

DAY71ではTaskの進捗を管理しました。

Pending
   ↓
Running
   ↓
Completed

DAY72ではCompletedになったTaskについて、

Task ID
担当AI社員
Status
成果物
実行結果

などをWorkflowで管理する考え方を整理しました。

Company AI OSでのWorkflow

Workflowは単にTaskを管理するだけではありません。

AI社員が作った成果を保存し、
次のTaskへ引き渡すことで、

AI社員
  ↓
Task
  ↓
仕事
  ↓
結果
  ↓
Workflow
  ↓
次のTask
  ↓
次のAI社員

という仕事の流れを作ります。

これによって、
複数のAI社員がそれぞれ担当する仕事を、
一つの業務フローとしてつなげていきます。

DAY72で整理した8つのシーン
AI社員がTaskを完了する
AI社員が結果をWorkflowへ返す
WorkflowがTaskの完了を確認する
Workflowが結果を保存する
次のTaskが結果を受け取る
次のAI社員が結果を利用する
Taskの結果がWorkflowを流れる
Workflowが仕事の結果をつなぐ
開発記録

DAY71では「Taskの進捗」を管理しました。

DAY72では「Taskの結果」を管理します。

Company AI OSを、
AI社員が個別に仕事をする仕組みから、
複数のAI社員が成果を引き継ぎながら仕事を進める仕組みへ、
少しずつ発展させています。

DAY72｜Taskの結果をWorkflowで管理する

#CompanyAIOS #AI社員 #AIエージェント #Workflow #生成AI


### GitHubのファイル構成

DAY72では、これまでの流れに合わせて、

```text
day72/
├── day72.rpy
├── scene72_01.png
├── scene72_02.png
├── scene72_03.png
├── scene72_04.png
├── scene72_05.png
├── scene72_06.png
├── scene72_07.png
├── scene72_08.png
└── voice/
    └── day72/
        ├── day72_01.ogg
        ├── day72_02.ogg
        ├── day72_03.ogg
        ├── day72_04.ogg
        ├── day72_05.ogg
        ├── day72_06.ogg
        ├── day72_07.ogg
        └── day72_08.ogg


____________________________________________________________________________________________________________________________________________________________

# DAY73｜Workflowが次のTaskを開始する

Company AI OS 開発 DAY73。

DAY72では、Taskが完了したあと、
その結果をWorkflowで管理し、次のTaskへ引き渡す仕組みを整理しました。

DAY73では、その結果を利用して、
Workflowが実際に次のTaskを開始する流れを整理します。

## 今回のテーマ

Workflowが次のTaskを開始する

基本的な流れは次の通りです。

```text
前のTaskが完了
      ↓
Workflowが結果を確認
      ↓
次のTaskの条件を確認
      ↓
Workflowが次のTaskを開始
      ↓
担当AI社員へTaskを渡す
      ↓
前のTaskの結果を受け取る
      ↓
AI社員が次の仕事を開始
      ↓
Workflowが連続して仕事を動かす
1. 前のTaskが完了する

例えば、AI社員が市場調査を担当します。

Task 01
市場調査
    ↓
市場調査レポート完成
    ↓
Completed

Taskが完了すると、
Workflowは次の処理へ進みます。

2. Workflowが結果を確認する

Workflowは、完了したTaskの状態と、
Taskによって作られた成果物を確認します。

Task Status
Completed

Result
市場調査レポート

次のTaskを開始するために必要な結果が
揃っていることを確認します。

3. 次のTaskの条件を確認する

例えば、

Task 01
市場調査
    ↓
市場調査レポート
    ↓
Task 02
企画書作成

という関係があります。

Task 02を開始するには、
Task 01の結果が必要です。

WorkflowがTask同士の関係と条件を確認します。

4. Workflowが次のTaskを開始する

条件が揃うと、
Workflowは次のTaskを開始します。

Task 01
Completed
    ↓
Workflow
    ↓
Task 02
Running

これによって、
前の仕事が終わると次の仕事へ進むことができます。

5. 担当AI社員へTaskを渡す

開始されたTaskは、
担当するAI社員へ渡されます。

Task 02
企画書作成
      ↓
企画担当AI

WorkflowがTaskと担当AI社員を管理します。

6. 前のTaskの結果を受け取る

次のAI社員は、
前のTaskで作られた結果を利用します。

市場調査AI
    ↓
市場調査レポート
    ↓
Workflow
    ↓
企画担当AI

AI社員同士が直接会話するのではなく、
Workflowが成果物を引き渡します。

7. AI社員が次の仕事を開始する

企画担当AIは、
受け取った市場調査の結果を利用して、
企画書作成を開始します。

市場調査レポート
       ↓
企画担当AI
       ↓
企画書作成

前のTaskの結果が、
次のTaskの入力情報として利用されます。

8. Workflowが連続して仕事を動かす

この仕組みを組み合わせると、

市場調査
   ↓
企画書作成
   ↓
マーケティング計画
   ↓
Webサイト作成

という連続した仕事を作ることができます。

WorkflowがTaskの状態を管理しながら、
次のTaskへ仕事を進めていきます。

DAY73のポイント

DAY71では、

Taskの進捗を管理

DAY72では、

Taskの結果を管理

DAY73では、

結果を利用して次のTaskを開始

というところまで進みました。

DAY71
Taskの進捗
    ↓
DAY72
Taskの結果
    ↓
DAY73
次のTaskを開始

Company AI OSでは、
WorkflowによってAI社員の仕事をつなぎ、
一つの仕事を連続した業務フローとして実行できる仕組みを作っています。

DAY73｜8つのシーン
前のTaskが完了する
WorkflowがTaskの結果を確認する
次のTaskの条件を確認する
Workflowが次のTaskを開始する
担当AI社員へTaskが渡される
AI社員が前のTaskの結果を受け取る
AI社員が次の仕事を開始する
Workflowが連続して仕事を動かす

DAY73｜Workflowが次のTaskを開始する

#CompanyAIOS #AI社員 #AIエージェント #Workflow #生成AI


### GitHubでの位置づけ

DAY73では新しい機能を大量に実装するというより、 Workflowの実行フローを一段進めたDAY として記録するのがよいです。

```text
DAY70  TaskをAI社員へ割り当てる
   ↓
DAY71  Taskの進捗を管理する
   ↓
DAY72  Taskの結果を管理する
   ↓
DAY73  結果を使って次のTaskを開始する

____________________________________________________________________________________________________________________________________________________________

# DAY74｜Workflow Test

## 概要

DAY74では、これまで構築してきたWorkflowを実際の仕事の流れとしてテストしました。

DAY73では、完了したTaskの結果を確認し、その結果を利用して次のTaskを開始し、担当するAI社員へ仕事を引き渡す仕組みを確認しました。

DAY74では、それを一連のWorkflowとして最後まで実行します。

---

## 今回の流れ

```text
仕事の依頼
    ↓
Workflow
    ↓
Taskへ分解
    ↓
Task 01 実行
    ↓
Task 01 完了
    ↓
結果を次のTaskへ
    ↓
Task 02・03を連続実行
    ↓
すべてのTaskが完了
    ↓
Workflow Test Complete

DAY74で確認したこと
1. 仕事をTaskへ分解
Workflowが一つの仕事を複数のTaskへ分解します。
例：
- 市場調査
- 企画書作成
- マーケティング計画
- 資料作成
大きな仕事を、そのままAI社員へ渡すのではなく、処理可能な単位へ分解します。
2. Taskを実行
最初のTaskを担当するAI社員が処理します。
Taskが完了すると、その結果が保存されます。
3. Taskの結果を次へ渡す
Workflowは完了したTaskの結果を確認し、次のTaskへ引き渡します。
Task 01
   ↓
市場調査結果
   ↓
Task 02
   ↓
企画書
   ↓
Task 03

前のTaskの成果物が、次のTaskの入力情報になります。
4. AI社員をWorkflowで連携
AI社員同士が直接仕事を渡すのではなく、Workflowが間に入って仕事をつなぎます。
AI社員 A
   ↓
Task結果
   ↓
Workflow
   ↓
AI社員 B
   ↓
Task結果
   ↓
Workflow
   ↓
AI社員 C

これによって、複数のAI社員を一つの仕事の流れとして連携できます。
DAY74のポイント
DAY74で確認したかったのは、
「Workflowが存在するか」
ではありません。
実際に、
仕事を最初から最後までWorkflowで流せるか
ということです。
今回のテストでは、
- 仕事をTaskへ分解
- Taskを実行
- 結果を保存
- 次のTaskへ結果を引き渡す
- 担当AI社員へ仕事を渡す
- 次のTaskを実行
- すべてのTaskを完了
という一連の流れを確認しました。
DAY74の位置付け
DAY73：
Workflowが次のTaskを開始する

DAY74：
Workflowで仕事を最後まで流してみる

という関係です。
これによりCompany AI OSは、
AI社員が個別に動くシステム
から、
AI社員がWorkflowによって連携して仕事を進めるシステム
へ一歩進みました。
使用技術
- Python
- Workflow
- Task管理
- AI社員
- Ren'Py
- Local AI
DAY74 完了
Workflow Test Complete.
仕事をTaskへ分解し、Taskの結果を次のTaskへ引き渡しながら、複数のAI社員を連携させて仕事を最後まで処理する流れを確認しました。

____________________________________________________________________________________________________________________________________________________________

# DAY75｜Beta 0.8 Release

## 概要

DAY75では、これまで構築してきた

- AI社員
- Task
- Workflow

を一つにつなぎ、Company AI OS Beta 0.8として一連の動作を確認しました。

AI社員が担当するTaskを実行し、Workflowがその結果を次のTaskへ引き渡すことで、一つの仕事を最後まで処理できる基本構造を確認しています。

---

## DAY75のテーマ

**Beta 0.8 Release**

今回の目的は、新しい機能を追加することではなく、これまで構築してきた仕組みを統合し、Company AI OSとして動作することを確認することです。

---

## 確認した構成

```text
仕事の依頼
    ↓
Taskへ分解
    ↓
AI社員へ割り当て
    ↓
Task実行
    ↓
実行結果
    ↓
Workflow
    ↓
次のTask
    ↓
仕事完了

AI社員
AI社員はそれぞれ担当する役割を持ち、割り当てられたTaskを実行します。
今回のビジュアルでは、AI社員を簡易的な人型として表現しています。
重要なのはキャラクターそのものではなく、
「AI社員が役割を持ち、仕事を担当する」
というシステム上の構造です。
Task
会社の仕事を実行可能な単位へ分解し、Taskとして管理します。
例：
Task 01｜市場調査
Task 02｜企画書作成
Task 03｜マーケティング計画
Task 04｜資料作成

Taskには担当AI社員や実行状態などを持たせ、仕事の進行状況を管理します。
Workflow
Workflowは複数のTaskをつなぎ、一つの仕事として処理するための仕組みです。
Task 01
  ↓
Task 02
  ↓
Task 03
  ↓
Task 04
  ↓
完了

前のTaskの結果を次のTaskへ引き渡すことで、AI社員が連携して仕事を進められるようにします。
AI社員 × Task × Workflow
DAY75で確認した重要な連携は次の通りです。
Workflow
    ↓
AI社員
    ↓
Task実行
    ↓
結果
    ↓
Workflow
    ↓
次のTask

これによって、AI社員が個別に動くだけではなく、複数のAI社員が一つの仕事を連携して処理できる基本構造が成立しました。
Beta 0.8
DAY75では、AI社員・Task・Workflowが連携し、一つの仕事を最後まで処理できることを確認しました。
Company AI OSは、
「AIを使うシステム」
から、
「AI社員が仕事をするシステム」
へ進みました。
Beta 0.8は、Company AI OSの基本構造を確認する一つの区切りです。
Project Progress
DAY75
Beta 0.8 Release
AI社員 × Task × Workflow
AI社員が働く会社の基本構造を構築しました。
Next
ここからさらにCompany AI OSを発展させ、
AI社員が実際に会社の仕事を動かすOS
を目指して開発を続けます。
DAY100のVersion 1.0完成に向けて、開発を進めていきます。

____________________________________________________________________________________________________________________________________________________________

# DAY76｜AI Agent ― AI社員が仕事を判断して実行する

Company AI OS DAY76では、AI社員が仕事の状況を分析し、
必要なTaskを判断しながら仕事を進める「AI Agent」の基本的な流れを整理します。

DAY75までに構築してきた

- AI社員
- Task
- Workflow
- Knowledge
- Tool

を組み合わせ、AI社員が単純にTaskを実行するだけではなく、
実行結果を確認し、次の行動を判断する流れを目指します。

---

## DAY76のテーマ

「AI Agent ― AI社員が仕事を判断して実行する」

今回の基本フローは次の通りです。

```text
仕事を受け取る
    ↓
仕事を分析する
    ↓
必要なTaskを判断する
    ↓
Knowledgeを検索する
    ↓
Toolを実行する
    ↓
実行結果を確認する
    ↓
次の行動を判断する
    ↓
AI Agentとして仕事を完了する

AI Agentの役割
これまでのAI社員は、与えられたTaskを実行することが中心でした。
DAY76では、AI社員自身が仕事の状況を確認し、
何をするのか
↓
どのTaskが必要なのか
↓
どの情報が必要なのか
↓
どのToolを使うのか
↓
結果は十分なのか
↓
次に何をするのか

という判断を行う流れを作ります。
DAY76で扱う8ステップ
01｜新しい仕事が届く
新しい仕事の依頼をAI社員が受け取ります。
02｜AI社員が仕事を分析する
依頼内容を分析し、目的や必要な情報を整理します。
03｜必要なTaskを判断する
仕事を完了するために必要なTaskを選択します。
04｜Knowledgeを検索する
社内Knowledgeから仕事に関連する情報を取得します。
05｜Toolを実行する
必要なToolを実行し、外部情報やデータを取得します。
06｜実行結果を確認する
Toolから取得した結果を確認し、Taskの目的を満たしているか判断します。
07｜次の行動を判断する
実行結果をもとに、次に行うべきTaskや処理を判断します。
08｜AI Agentとして仕事を完了する
計画、判断、Knowledge検索、Tool実行、結果確認、次の行動までを連続して実行し、仕事を完了します。
DAY75からの進化
DAY75では、
AI社員
   ↓
Task
   ↓
Workflow

によって、会社の仕事を連続して処理する基本構造を確認しました。
DAY76では、ここに
AI社員による判断

を加えます。
これによって、
「決められたTaskを実行するAI」
から、
「仕事の状況を確認し、次の行動を判断するAI Agent」
へ進化させます。
Company AI OSにおけるAI Agent
AI Agentを「何でも自由に実行するAI」として考えるのではなく、
仕事
 ↓
分析
 ↓
Task判断
 ↓
Knowledge
 ↓
Tool
 ↓
結果確認
 ↓
次の行動
 ↓
完了

という会社の仕事の流れの中でAIに判断させることを目指します。
AIにすべてを任せるのではなく、
どこまでAIに判断させるのかをシステムとして設計すること
がCompany AI OSの重要なポイントになります。
DAY76の位置づけ
DAY76では、Company AI OSが
「AIを使うシステム」
から、
「AI社員が仕事を進めるシステム」
へ進むためのAI Agentの基本構造を確認します。
DAY100のCompany AI OS 1.0完成に向けて、
AI社員が実際の仕事を動かすための重要なステップです。
Development
- Project: Company AI OS
- DAY: 76
- Theme: AI Agent
- Status: Development
Next
DAY77へ続きます。

____________________________________________________________________________________________________________________________________________________________

# DAY77｜AI Agent × Workflow

## AI社員とWorkflowで仕事を完了する

DAY77では、AI AgentとWorkflowを連携させ、
一つの仕事を最後まで進めるための基本的な流れを整理しました。

DAY76では、AI Agentが仕事を分析し、
必要なTaskを判断して実行する仕組みを構築しました。

DAY77では、そのAI AgentをWorkflowと接続します。

---

## 今回のテーマ

AI AgentとWorkflowの連携

今回の基本的な流れは、

仕事
↓
Workflow
↓
AI Agent
↓
Task判断
↓
Knowledge / Tool
↓
Task実行
↓
結果
↓
Workflow
↓
次のTask
↓
AI Agent
↓
仕事完了

という構成です。

---

## AI AgentとWorkflowの役割

### Workflow

Workflowは、仕事全体の流れを管理します。

- 仕事を受け取る
- Taskを管理する
- Taskの順番を管理する
- AI AgentへTaskを渡す
- 実行結果を受け取る
- 次のTaskへ進める

### AI Agent

AI Agentは、Workflowから受け取ったTaskを実行します。

- Taskの内容を分析
- 必要なKnowledgeを検索
- 必要なToolを選択
- Taskを実行
- 実行結果をWorkflowへ返す

---

## DAY77の処理フロー

### 01｜新しい仕事を受け取る

Company AI OSに新しい仕事の依頼が届きます。

### 02｜Workflowが仕事を開始する

Workflowが仕事を受け取り、
必要な処理の流れを開始します。

### 03｜AI AgentがTaskを判断する

AI Agentが仕事の内容を分析し、
必要なTaskを判断します。

### 04｜KnowledgeとToolを使ってTaskを実行する

AI AgentがKnowledgeから情報を取得し、
必要に応じてToolを実行します。

### 05｜実行結果をWorkflowへ返す

Taskの実行結果をWorkflowへ返します。

### 06｜Workflowが結果を確認する

Workflowが結果を確認し、
次のTaskへ進める状態か判断します。

### 07｜次のTaskをAI Agentへ渡す

Workflowが次のTaskをAI Agentへ渡します。

### 08｜AgentとWorkflowで仕事を完了する

AI AgentとWorkflowが連携し、
一つの仕事を最後まで進めます。

---

## DAY77で確認したこと

DAY76では、

「AI社員が仕事を判断して実行する」

という仕組みを作りました。

DAY77では、

「AI社員とWorkflowが連携して仕事を進める」

構造へ進みました。

AI Agentだけではなく、
WorkflowによってTaskとTaskをつなぐことで、
AIが仕事全体を継続して処理できる構造になります。

---

## Project

Company AI OS

100日でCompany AI OSを作るプロジェクトです。

DAY77では、
AI AgentとWorkflowを連携させ、
AI社員が一つの仕事を最後まで進めるための
基本構造を整理しました。

---

## DAY77

**AI Agent × Workflow**

AI社員がTaskを実行し、
Workflowが仕事の流れをつなぐ。

Company AI OSが
「AIが仕事をする会社」の構造へ
一歩進みました。

____________________________________________________________________________________________________________________________________________________________

# DAY78｜AI Workflow

## 複数のTaskを連続して実行する

DAY78では、DAY77で構築した
AI AgentとWorkflowの連携をさらに発展させ、

**複数のTaskをWorkflowによって連続して実行する仕組み**

を整理しました。

---

## 今回のテーマ

今回の仕事は、

「新商品の市場調査レポートを作成する」

という一つの仕事です。

この仕事を複数のTaskへ分解します。

```text
01｜市場調査
      ↓
02｜競合分析
      ↓
03｜ターゲット分析
      ↓
04｜レポート作成

WorkflowがTaskの順番を管理し、
AI AgentがそれぞれのTaskを実行します。
Workflowの役割
Workflowは仕事全体の流れを管理します。
- 仕事をTaskへ分解する
- Taskの順番を管理する
- AI AgentへTaskを渡す
- 実行結果を受け取る
- 結果を次のTaskへ引き渡す
- 最後のTaskまで処理を進める
Workflowによって、
複数のTaskを一つの仕事としてつなげます。
AI Agentの役割
AI AgentはWorkflowからTaskを受け取り、
実際の処理を実行します。
Workflow
   ↓
Task
   ↓
AI Agent
   ↓
Knowledge / Tool
   ↓
Task実行
   ↓
結果

実行結果はWorkflowへ返され、
次のTaskへ引き渡されます。
DAY78の処理フロー
01｜複数のTaskを持つ仕事
一つの仕事を複数のTaskへ分解します。
02｜Workflowを設計する
Task同士をどのようにつなぐかを設計します。
03｜Taskの順番を決める
仕事を完了するために必要なTaskの順番を設定します。
04｜Task 01をAI Agentへ渡す
Workflowが最初のTaskをAI Agentへ渡します。
05｜結果を次のTaskへ引き渡す
Task 01の結果をWorkflowが受け取り、
次のTaskへ引き渡します。
06｜Task 02を実行する
AI Agentが次のTaskを受け取り、
KnowledgeやToolを使って実行します。
07｜複数Taskを連続して実行する
Workflowによって複数のTaskを順番に実行します。
08｜Workflowで仕事全体を完了する
すべてのTaskが完了し、
一つの仕事全体が完了します。
DAY78の基本構造
仕事
 ↓
Workflow
 ↓
Task 01
 ↓
AI Agent
 ↓
結果
 ↓
Workflow
 ↓
Task 02
 ↓
AI Agent
 ↓
結果
 ↓
Workflow
 ↓
Task 03
 ↓
AI Agent
 ↓
結果
 ↓
Workflow
 ↓
Task 04
 ↓
AI Agent
 ↓
仕事完了

DAY76 → DAY77 → DAY78
DAY76
AI Agentが仕事を分析し、
必要なTaskを判断して実行する。
DAY77
AI AgentとWorkflowを連携する。
DAY78
Workflowによって複数のTaskをつなぎ、
仕事全体を連続して実行する。
DAY76
AI Agent
    ↓
Taskを判断・実行

DAY77
AI Agent × Workflow
    ↓
Taskと仕事の流れを連携

DAY78
Workflow
    ↓
複数Task
    ↓
連続実行
    ↓
仕事完了

DAY78で確認したこと
AI Agentが一つのTaskを実行するだけではなく、
Workflowによって複数のTaskをつなぐことで、
一つの仕事全体を連続して処理できる
構造を確認しました。
Company AI OSは、
「AIが回答する」だけではなく、
「AIがTaskを実行し、仕事を前へ進める」
段階へ進んでいます。
Project
Company AI OS
100日でCompany AI OSを完成させるプロジェクト。
DAY78では、
AI AgentとWorkflowを使って
複数のTaskを連続して実行する
基本的なWorkflow構造を整理しました。
DAY78
AI Workflow
複数のTaskをつなげて、
AI Agentが仕事全体を進める。
Workflowによって、
Company AI OSの「AIが仕事をする」仕組みを
さらに一段進めました。

____________________________________________________________________________________________________________________________________________________________

DAY79｜Workflow State Management

Overview

DAY79 focuses on Workflow state management in Company AI OS.

After introducing multi-task workflow execution in DAY78, this stage focuses on tracking task progress, receiving execution results, detecting failures, retrying failed tasks, and understanding the overall state of a job.

The goal is to make workflow execution easier to monitor and manage.

Key Topics

Checking overall workflow progress

Managing individual task states

Receiving task execution results

Detecting task failures

Retrying failed tasks

Moving to the next task after completion

Understanding the overall job status

Organizing workflow state management

Task Statuses

The workflow concept covers the following statuses:

Status

Description

Completed

The task finished successfully

Running

The task is currently executing

Pending

The task is waiting to execute

Error

The task failed

Cancelled

The task was stopped

Workflow Example

A sample workflow for preparing a market research report:

Market Research

Competitor Analysis

Target Analysis

Report Creation

Each task produces a result that can be passed to the next task. The workflow tracks progress and records execution outcomes to make the overall process easier to understand.

Error Handling Concept

When a task fails, the workflow should be able to:

Detect the failure

Record the error state and execution log

Retry the task according to configured conditions

Pass the result to the next task when successful

Retry limits and error-handling behavior should be defined by the actual implementation.

Development Goal

Company AI OS aims to combine AI employees, Knowledge Base, Tools, AI Agent, and Workflow into a system that supports and executes company work.

DAY79 organizes the concepts needed to monitor task execution and understand the state of the overall workflow.

Project Progress

DAY78: Multi-task workflow execution

DAY79: Workflow state management

Note: This README documents the DAY79 design and development topic. Individual capabilities should be considered implemented only after they have been verified in the actual code.

#CompanyAIOS #Workflow #AIAgent #Python

____________________________________________________________________________________________________________________________________________________________

### Related

## 公開記録

- DAY39　[YouTube](https://youtu.be/Lu9D7He9JyY)｜[note](https://note.com/grand_peony7915/n/nb23b824aa6ce)
- DAY40　[YouTube](https://youtu.be/Mp9IgqDbyjc)｜[note](https://note.com/grand_peony7915/n/neb28a92e87e0)
- DAY41　[YouTube](https://youtu.be/1-P7r5PmWuE)｜[note](https://note.com/grand_peony7915/n/nd032d232e525)
- DAY42　[YouTube](https://youtu.be/Gtg-5Y42LiI)｜[note](https://note.com/grand_peony7915/n/n7c0df093d47c)
- DAY43　[YouTube](https://youtu.be/Pvc5nJRV9R4)｜[note](https://note.com/grand_peony7915/n/n9bea2eab14b1)
- DAY44　[YouTube](https://youtu.be/dPlCDRh9gkE)｜[note](https://note.com/grand_peony7915/n/n7c0df093d47c)
- DAY45　[YouTube](https://youtu.be/5LllDoLPdPc)｜[note](https://note.com/grand_peony7915/n/n9256d16b172d)
- DAY46　[YouTube](https://youtu.be/WdKbBHEFc_Q)｜[note](https://note.com/grand_peony7915/n/ndc2554cba7fe)
- DAY47　[YouTube](https://youtu.be/EA7g96_2z0w)｜[note](https://note.com/grand_peony7915/n/n3e0dc923d5b4)
- DAY48　[YouTube](https://youtu.be/K2Zg3H068Uw)｜[note](https://note.com/grand_peony7915/n/naf086f254565)
- DAY49　[YouTube](https://youtu.be/IqAPd3BX6iY)｜[note](https://note.com/grand_peony7915/n/n905e46176c65)
- DAY50　[YouTube](https://youtu.be/n7fjLon-M88)｜[note](https://note.com/grand_peony7915/n/na02dadff1fe2)
- DAY51　[YouTube](https://youtu.be/bRQyDGMG0_8)｜[note](https://note.com/grand_peony7915/n/n216e082ac1be)
- DAY52　[YouTube](https://youtu.be/iKVxA3ylP5A)｜[note](https://note.com/grand_peony7915/n/n54c67d76d1c7)
- DAY53　[YouTube](https://youtu.be/CMZrUlHZYmY)｜[note](https://note.com/grand_peony7915/n/n90a18e0773e5)
- DAY54　[YouTube](https://youtu.be/eVLqp8ZcLH0)｜[note](https://note.com/grand_peony7915/n/neec84f528f2e)
- DAY55　[YouTube](https://youtu.be/cvWNs06f668)｜[note](https://note.com/grand_peony7915/n/n439df825ad8c)
- DAY56　[YouTube](https://youtu.be/stsIfyGvi6M)｜[note](https://note.com/grand_peony7915/n/n85649859e621)
- DAY57　[YouTube](https://youtu.be/FcQeadaTWbE)｜[note](https://note.com/grand_peony7915/n/nd57f7961c1f1)
- DAY58　[YouTube](https://youtu.be/ysGjTDwOjeo)｜[note](https://note.com/grand_peony7915/n/nb022f4cf62d1)
- DAY59　[YouTube](https://youtu.be/6fvFa-UOxS0)｜[note](https://note.com/grand_peony7915/n/n3454b111812f)
- DAY60　[YouTube](https://youtu.be/YgLrcXBit9k)｜[note](https://note.com/grand_peony7915/n/ne7986056a661)
- DAY61　[YouTube](https://youtu.be/vz9tWX94Mkc)｜[note](https://note.com/grand_peony7915/n/nd12b07571cad)
- DAY62　[YouTube](https://youtu.be/5Lju1rkmiVo)｜[note](https://note.com/grand_peony7915/n/n077e6490c91c)
- DAY63　[YouTube](https://youtu.be/HxZoyIK8R90)｜[note](https://note.com/grand_peony7915/n/n6aec98ae754d)
- DAY64　[YouTube](https://youtu.be/zZ5H6D7blsA)｜[note](https://note.com/grand_peony7915/n/n84c2b7d47cc1)
- DAY65　[YouTube](https://youtu.be/zZ5H6D7blsA)｜[note](https://note.com/grand_peony7915/n/n3163d076b124)
- DAY66　[YouTube](https://youtu.be/TV0mDxDTFWQ)｜[note](https://note.com/grand_peony7915/n/n7b5fb244a160)
- DAY67　[YouTube](https://youtu.be/cuSB11hP32k)｜[note](https://note.com/grand_peony7915/n/n66bd47f0da6f)
- DAY68　[YouTube](https://youtu.be/PGbq7V2bAb8)｜[note](https://note.com/grand_peony7915/n/n7b240f55047e)
- DAY69　[YouTube](https://youtu.be/Nh3-4XdUzBU)｜[note](https://note.com/grand_peony7915/n/n0b7e13da7f05)
- DAY70　[YouTube](https://youtu.be/CQEYZAhPhDc)｜[note](https://note.com/grand_peony7915/n/nd4885ca5a712)
- DAY71　[YouTube](https://youtu.be/tvsvTOYvK9Y)｜[note](https://note.com/grand_peony7915/n/nfdb673f9ed21)
- DAY72　[YouTube](https://youtu.be/ToX7UDXf2MQ)｜[note](https://note.com/grand_peony7915/n/n83a78f2866d7)
- DAY73　[YouTube](https://youtu.be/visOhHf4gkM)｜[note](https://note.com/grand_peony7915/n/nc8bd2ce66c5e)
- DAY74　[YouTube](https://youtu.be/urbf_JFG4pQ)｜[note](https://note.com/grand_peony7915/n/nbdf5a3551afc)
- DAY75　[YouTube](https://youtu.be/0xTGYAv_xZo)｜[note](https://note.com/grand_peony7915/n/n3e462d5270b2)
- DAY76　[YouTube](https://youtu.be/DyDlVHh5oJY)｜[note](https://note.com/grand_peony7915/n/n5b2ae42560f2)
- DAY77　[YouTube](https://youtu.be/96eJkg9af60)｜[note](https://note.com/grand_peony7915/n/nfc372d4a60a3)
- DAY78　[YouTube](https://youtu.be/PIIJzkNIQqM)｜[note](https://note.com/grand_peony7915/n/n02fe6570d4ad)
- DAY79　[YouTube](https://youtu.be/iyU4LBsziZA)｜[note](https://note.com/grand_peony7915/n/nccb000ab5e58)

## Author

Company AI OS Development Log

Building one step every day toward an AI-operated company.
