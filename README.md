## 1) ディレクトリ構成（スケール重視の標準案）

### 推奨ツリー（Vault直下）

```
arxiv-cs-2025/
  00_Inbox/
  01_Papers/
    2025/
      cs.AI/
      cs.CL/
      cs.CV/
      cs.LG/
      ...（arXivのCSカテゴリ単位）
  02_Topics/
  03_Entities/
    Authors/
    Orgs/
    Venues/
    Datasets/
    Methods/
  04_Syntheses/
    2025/
      cs.AI/
      cs.CL/
      cross-cutting/
  05_Dashboards/
  90_Attachments/
    pdf/
      2025/
    figures/
  99_Templates/
  _meta/
    tag-registry.md
    naming-rules.md
```

### 意図

* **00_Inbox**：自動取り込みの一時置き場（未整形・未重複チェック）
* **01_Papers/2025/<primary_category>/**：論文ノートの本体（“一次情報”）
* **02_Topics**：概念ノート（“知識”）。論文→トピックへリンクしていく
* **03_Entities**：著者・データセット・手法などの“固有名詞ノート”（任意だが後で効く）
* **04_Syntheses**：月次/四半期/カテゴリ別の統合（“二次情報”）
* **05_Dashboards**：Dataview/クエリの入口（読む・集計する場所）
* **90_Attachments**：PDF等の添付を集約（Obsidianの検索/同期負荷を制御しやすい）
* **99_Templates**：テンプレート固定（紙が増えるほど重要）

> 代替案として「01_Papers/2025/ にフラット格納＋プロパティで分類」も可能ですが、件数が非常に多い運用では、フォルダ分割（少なくとも primary category）を推奨します。

---

## 2) 命名規則（衝突回避・機械処理向け）

### 論文ノート（推奨）

* ファイル名：`P-<arxiv_id>.md`

  * 例：`P-2503.01234.md`
* 表示タイトルはYAMLに持たせる（ファイル名を安定キーにする）

### 添付PDF

* `90_Attachments/pdf/2025/<arxiv_id>.pdf`

  * 例：`.../pdf/2025/2503.01234.pdf`

これにより、重複・リネーム・リンク切れが大きく減ります。

---

## 3) ノート（章）構成

### 3.1 論文ノート（Paper Note）の章構成（推奨テンプレ）

YAML（プロパティ）＋本文見出しを固定化します。

**YAML例**

* `arxiv_id`：2503.01234
* `year`：2025
* `primary`：cs.CL
* `categories`：["cs.CL","cs.LG"]（cross-list含む）
* `status`：inbox / queued / summarized / verified / synthesized / dropped
* `ai_summary_level`：brief / full / deep
* `tasks`：["translation","repro"] のように配列で
* `methods`：["transformer","retrieval"]（語彙統制）
* `datasets`：["SQuAD","C4"]（語彙統制）
* `code`：URL（あれば）
* `pdf`：相対パス

**本文（見出し）**

1. `TL;DR（3行）`
2. `Problem / Setting（何を解く？前提は？）`
3. `Key Contributions（新規性を箇条書き）`
4. `Method（モデル・アルゴリズム・設計）`
5. `Experiments（データ・指標・比較）`
6. `Results（主要数値・主張の根拠）`
7. `Ablations / Analysis（効いている要因）`
8. `Limitations / Risks（制約・弱点・再現性）`
9. `Relation to Prior Work（関連と差分）`
10. `My Notes（自分の解釈・疑問・使い道）`
11. `Links（Topic/Method/Dataset/Author ノートへのリンク）`
12. `Action Items（次にやること）`

> 「AI要約だけで終わらない」よう、**Limitations / Risks** と **Action Items** を必須にすると後から統合が効きます。

---

### 3.2 カテゴリ別インデックス（例：cs.CL 2025）

`01_Papers/2025/cs.CL/_index.md` のようなノートを置くのがおすすめです。

見出し例：

* `Scope（含める範囲・除外）`
* `Monthly Highlights（2025-01〜）`
* `Top Papers（暫定）`
* `Emerging Themes（テーマ別クラスタ）`
* `Open Problems（未解決/次の一手）`
* `Backlog（未処理）`

---

### 3.3 統合ノート（Synthesis）

`04_Syntheses/2025/cs.CL/2025-Q1.md` のように、四半期などで固定。

見出し例：

* `Executive Summary（結論先出し）`
* `Theme 1..N（テーマ別に代表論文をリンク）`
* `Technique Trends（手法トレンド）`
* `Dataset/Benchmark Movement（評価軸の変化）`
* `Practical Takeaways（実務に効く要点）`
* `What to Read Next（次の優先順位）`

---

## 4) タグ構成（タグは最小限、分類はプロパティ中心）

大量運用では、タグを増やしすぎると破綻します。おすすめは **「タグ＝ワークフローと粗い種別」**、詳細分類は **YAMLプロパティ（methods/datasets/tasks など）**に寄せる設計です。

### 4.1 タグ（推奨：3系統だけ）

1. **種別**

* `#type/paper`
* `#type/topic`
* `#type/synthesis`
* `#type/entity`

2. **状態（ワークフロー）**

* `#status/inbox`
* `#status/queued`
* `#status/summarized`
* `#status/verified`
* `#status/synthesized`
* `#status/dropped`

3. **重要フラグ（任意）**

* `#flag/high-impact`
* `#flag/repro-needed`
* `#flag/survey-like`

> カテゴリ（cs.CLなど）までタグで持つと、cross-listで二重化しやすいので、**primary/categoriesはプロパティ**を推奨します。

---

## 5) プロパティ（語彙統制のコア）

タグより重要なのが、**プロパティの語彙統制**です。以下のどれかは必ず固定辞書化してください。

* `primary`：arXivカテゴリ（cs.AI等）
* `methods`：手法（例：transformer, diffusion, retrieval, GNN…）
* `tasks`：タスク（例：classification, summarization, code-gen…）
* `datasets`：データセット/ベンチ（例：ImageNet, GLUE…）
* `status`：処理状態（上記タグと一致させる）
* `ai_summary_level`：要約の深さ
* `signals`：["theory","systems","empirical"] のような属性（任意）

**運用のコツ**

* `methods/tasks/datasets` は “自由入力” にしないで、`_meta/tag-registry.md` のような辞書ノートで管理する
* 表記ゆれ（RAG / Retrieval-Augmented Generation）を吸収するため、内部キーを短く固定する（例：`retrieval` に統一）

---

## 6) Obsidianで回すための「ダッシュボード」最小セット

`05_Dashboards/` に以下だけ作ると運用が安定します。

1. `00-Queue.md`：未処理（inbox/queued）一覧
2. `01-ByCategory.md`：カテゴリ別の進捗（何本 summarized/verified か）
3. `02-TopSignals.md`：#flag/high-impact や引用数候補（将来の見直し枠）
4. `03-Synthesis-Backlog.md`：synthesis対象の束（テーマ別に集約）

Dataviewを使う場合、**status / primary / year** が揃っているだけでほぼ回せます。

---

## 7) 破綻しやすいポイントと回避策

* **タグが増えすぎる**
  → タグは「type/status/flag」だけ。詳細はプロパティへ。

* **カテゴリ横断（cross-list）で二重管理になる**
  → フォルダは primary のみ、cross-list は `categories` 配列で持つ。

* **AI要約が均質化して価値が落ちる**
  → 論文ノートに `Limitations / Risks` と `Action Items` を必須化し、人間側の判断点を残す。

* **数が多すぎて統合できない**
  → “全件精読”ではなく、`ai_summary_level` を導入して段階運用（brief→full→deep）にする。

---

承知しました。続きとして、**すぐ運用に入れるレベルの「テンプレ」「Dataview例」「取り込み〜要約の運用フロー」「語彙統制（辞書）と品質管理」**まで具体化します。

---

## 8) すぐ使えるテンプレ（99_Templates）

### 8.1 Paper Note（P-<arxiv_id>.md）

```markdown
---
type: paper
arxiv_id: "{{VALUE:arxiv_id}}"
title: "{{VALUE:title}}"
year: 2025
primary: "{{VALUE:primary}}"        # 例: cs.CL
categories: ["{{VALUE:primary}}"]   # cross-listは後で追加
authors: []                         # "Surname, Name" 推奨
published: "{{VALUE:published}}"    # YYYY-MM-DD
updated: "{{VALUE:updated}}"        # YYYY-MM-DD
doi: ""
pdf: "90_Attachments/pdf/2025/{{VALUE:arxiv_id}}.pdf"
code: ""
project_page: ""
status: inbox                       # inbox/queued/summarized/verified/synthesized/dropped
ai_summary_level: brief             # brief/full/deep
read_time_min: 0
score: 0                            # 0-5: 重要度
signals: []                         # ["theory","systems","empirical","benchmark","survey"]
methods: []                         # 語彙統制
tasks: []                           # 語彙統制
datasets: []                        # 語彙統制
claims: []                          # 主要主張の短文
risks: []                           # リスク/限界の短文
notes_owner: ""                     # 複数人運用なら
created: "{{DATE:YYYY-MM-DD}}"
---

# TL;DR（3行）
-

# Problem / Setting
-

# Key Contributions
-
-
-

# Method
-

# Experiments
- Dataset / Benchmark:
- Metrics:
- Baselines:
- Setup:

# Results（主要数値）
-

# Ablations / Analysis
-

# Limitations / Risks
-

# Relation to Prior Work
-

# My Notes（解釈・疑問・使い道）
-

# Links
- Topics:
- Methods:
- Datasets:
- Related Papers:

# Action Items
- [ ]
```

運用上の要点：

* **ファイル名は `P-<arxiv_id>` 固定**（キーとして扱う）
* **タグは基本不要**（type/status/flagだけに抑える設計なので、ここではYAMLで完結）

---

### 8.2 Topic Note（02_Topics/<topic>.md）

```markdown
---
type: topic
topic: "{{VALUE:topic}}"
aliases: []
scope: ""
keywords: []
created: "{{DATE:YYYY-MM-DD}}"
---

# Definition
-

# Why it matters
-

# Canonical Papers
-

# Typical Methods
-

# Benchmarks / Datasets
-

# Open Questions
-

# Linked Papers
```

---

### 8.3 Synthesis Note（04_Syntheses/2025/...）

```markdown
---
type: synthesis
period: "2025-Q1"
primary: "cs.CL"
created: "{{DATE:YYYY-MM-DD}}"
status: draft
---

# Executive Summary
-

# Theme 1:
## Representative Papers
-
## What changed vs prior quarter
-

# Theme 2:
...

# Technique Trends
-

# Benchmark / Evaluation Trends
-

# Practical Takeaways
-

# Next Reading List（優先度順）
1.
```

---

## 9) ダッシュボード（Dataview）例：最低限これだけで回る

前提：Dataviewを使う場合の例です（なくても運用できますが、件数が多いならほぼ必須になります）。

### 9.1 未処理キュー（05_Dashboards/00-Queue.md）

```dataview
TABLE arxiv_id, primary, published, ai_summary_level, score
FROM "01_Papers/2025"
WHERE status = "inbox" OR status = "queued"
SORT published DESC
LIMIT 200
```

### 9.2 進捗集計（カテゴリ別）（05_Dashboards/01-ByCategory.md）

```dataview
TABLE primary,
  length(rows) as total,
  sum(choice(status="summarized",1,0)) as summarized,
  sum(choice(status="verified",1,0)) as verified,
  sum(choice(status="synthesized",1,0)) as synthesized
FROM "01_Papers/2025"
GROUP BY primary
SORT total DESC
```

### 9.3 “重要候補”一覧（05_Dashboards/02-HighImpact.md）

```dataview
TABLE arxiv_id, primary, published, score, methods, tasks
FROM "01_Papers/2025"
WHERE score >= 4 AND status != "dropped"
SORT published DESC
```

---

## 10) 語彙統制（辞書）と「表記ゆれ検知」

### 10.1 registryノート（_meta/tag-registry.md）

* methods（許可語彙）
* tasks（許可語彙）
* datasets（許可語彙）
* signals（許可語彙）
  を一箇所にまとめ、**追加はここから**にします。

例（methodsの一部）：

* transformer
* diffusion
* retrieval
* rl
* gnn
* prompting
* alignment
* distillation
* quantization
* pruning
* speculative-decoding
* federated-learning
* privacy
* watermarking

### 10.2 “未知語彙”検知（methodsの表記ゆれを洗い出す）

```dataview
TABLE methods
FROM "01_Papers/2025"
FLATTEN methods as m
WHERE m != null
GROUP BY m
SORT length(rows) DESC
```

ここで出てきた語彙を registry と突き合わせ、**不適切な表記（例：RAG / rag / Retrieval-Augmented Generation）**を統一します。

---

## 11) 「全件AI要約」を破綻させない運用フロー（段階設計）

2025年CS全件は物量的に相当です。破綻しないために、要約を3段階にします。

### ステージA：Brief（機械で全件）

* 入力：タイトル + アブスト + メタデータ（可能なら導入の冒頭）
* 出力：TL;DR、寄与、想定タスク、想定手法、危険信号（過剰主張など）
* 所要：低コスト・高速
* status：`summarized`（ただし verified ではない）

### ステージB：Full（上位◯%だけ）

* 入力：PDF全文（または主要セクション抽出）
* 出力：Method/Experiments/Results を具体値込みで埋める
* status：`verified` に上げる候補

### ステージC：Deep（統合・再現性重視）

* 入力：PDF + 付録 + コード/実装
* 出力：再現性メモ、落とし穴、社内適用の判断材料
* status：`synthesized` に寄与

この段階を `ai_summary_level` と `status` で管理すると、**「全件確認」≒ Brief完了**として現実的に回せます。

---

## 12) 取り込み（Ingest）パイプラインの推奨（Obsidian外で自動化）

Obsidianは「保管と閲覧」に強い一方、**収集と更新は外部スクリプト**が堅実です。設計としては以下。

1. arXivメタデータ取得（ID、カテゴリ、日付、タイトル、著者、要旨）
2. `P-<id>.md` をテンプレから生成して `01_Papers/2025/<primary>/` に配置
3. PDFを `90_Attachments/pdf/2025/<id>.pdf` に保存
4. AI要約（まずBrief）→ Paper Noteに追記（TL;DR/Contrib/Methods/Tasks等）
5. `status` を `summarized` に更新
6. 重要度推定（簡易スコア）→ `score` を付ける（後で人間が修正）

補足：このとき **「更新の差分」**（arXivのv2/v3）も取れるなら `updated` を更新し、差分要約を `## Changelog` 的に残す設計も有効です。

---

## 13) 追加で入れると効くルール（運用規約）

* **1ノート1論文**（統合はSynthesisでやる）
* **論文ノート本文は“事実”と“解釈”を分ける**

  * 事実：Results/Setup/数値
  * 解釈：My Notes
* **疑わしい主張は `risks` に短文で残す**
* **外部リンクはYAMLに固定（code/project_page/doi）**
  本文に散らばると後で回収できません。

---
