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
## Author

Company AI OS Development Log

Building one step every day toward an AI-operated company.
