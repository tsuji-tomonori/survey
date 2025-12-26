---
description: JSONLファイルから指定行の論文を読み込み、PDFダウンロード＆Obsidianメモを日本語で作成し、関連エンティティも更新
argument-hint: [行番号]
allowed-tools: Read, Bash, Write, Edit, Glob
---

# arXiv論文読み込みコマンド

指定された行番号 `$ARGUMENTS` の論文を処理します。

## 実行手順

### Step 1: Pythonスクリプトで基本処理
以下のコマンドを実行してPDFダウンロードと基本メモを作成:
```bash
source .venv/bin/activate && python scripts/read_paper.py $ARGUMENTS
```

出力されるJSON情報を記録（note_path, pdf_path, arxiv_id, title, primary_category）

### Step 2: 読む前のゲート（論文タイプ判定）

PDFを読み込む前に、タイトル・カテゴリから論文タイプを推定:
- **method paper**: 新手法提案 → Method, Ablation重視
- **benchmark**: 実験比較 → Setup, Baselines重視
- **survey**: 俯瞰 → Related work, 分類重視
- **systems**: 実装・最適化 → 設計, スケーラビリティ重視
- **application**: 応用事例 → ドメイン適合, 実用性重視

### Step 3: PDFを読み込んで日本語で要約

作成されたPDFファイルを読み込み（Readツール）、以下の順序で確認:

1. **Abstract + Figure 1 + Conclusions** で全体像把握
2. **Setting / Data / Evaluation** で前提と妥当性確認
3. **Main results table** で数字確認
4. **Methodのコア** で新規性確認
5. **Ablations / Limitations** で信用度評価
6. **Related work** で位置づけ確認

### Step 4: メモファイルを日本語で更新

メモファイルをEditツールで更新。各セクションの記載ガイド:

#### TL;DR（3行）
論文の核心を3行で。「何を」「どうやって」「どうなった」

#### Problem / Setting（最重要）
以下を必ず明確化:
- **入力/出力**: 何を与えて何を返すか
- **目的**: 最適化するもの
- **評価**: どの指標で良いとするか
- **制約**: 計算資源、データ入手性、推論時制約
- **比較対象**: ライバル、系譜

#### Key Contributions
証拠付きの差分として記載:
```
- [提案内容]: [既存手法との差分] → [根拠となる実験]
```
避けるべき: 「性能が向上した」だけ、"SOTA" のそのまま転写

#### Method
再現可能な最小単位で記載:
- 前処理/入出力表現
- モデル/アルゴリズムのコア（数式の要点）
- 学習手順（データ、損失、ハイパラ）
- **推論手順**（デコード/検索、計算量）← 見落としがち

#### Experiments
公正性チェック含めて記載:
- Dataset / Benchmark: 版、フィルタ、分割
- Metrics: 目的との一致性
- Baselines: 最強ベースラインの有無
- Setup: モデルサイズ、学習時間、データ量

#### Results（主要数値）
**必須**: 数字＋意味＋条件をセットで
```
[指標]で[ベースライン]に対して[差分]: 条件
例: "GLUE平均で +1.2、同パラメータ規模、同データ量条件"
```
- 絶対値と差分の両方
- 可能なら分散/信頼区間

#### Ablations / Analysis
- どのコンポーネントが効いたか
- どの条件で効かないか（失敗例）
- スケール則の傾向

#### Limitations / Risks（地雷マップ）
以下を厳しくチェック:
- **再現性**: コード有無、詳細記載、データ公開
- **外的妥当性**: 特定ベンチのみ成立？
- **計算コスト**: 現実的か
- **評価の穴**: ベースライン不備、データリーク

#### プロパティ更新
- `methods`: 統一語彙で（transformer, retrieval, diffusion等）
- `tasks`: 統一語彙で（classification, generation, QA等）
- `datasets`: 使用データセット
- `claims`: 主張を短文で（定量的に）
- `risks`: 反証・制約を短文で
- `status`: `summarized` に更新
- `score`: 重要度を0-5で評価

### Step 5: 品質チェックリスト確認

以下を確認してからstatusを更新:
- [ ] タスク設定（入力/出力/評価/制約）が明確
- [ ] 既存手法との差分が1文で書ける
- [ ] 主要結果は "絶対値＋差分＋条件" が揃っている
- [ ] ベースラインの公正性を確認した
- [ ] 再現に必要な情報の有無を判断した
- [ ] 限界/リスクを「使うときの地雷」として書いた

全て確認できたら `status: verified` に更新可能

### Step 6: 関連エンティティの更新

論文メモ作成後、以下のエンティティも更新:

#### Methods（新規手法が登場した場合）
`arxiv-cs-2025/03_Entities/Methods/M-{method_name}.md` を確認し、
- 存在しない: 新規作成（`/update-method` 参照）
- 存在する: papers配列に論文を追加

#### Datasets（新規/使用データセットがある場合）
`arxiv-cs-2025/03_Entities/Datasets/D-{dataset_name}.md` を確認し、
- 存在しない: 新規作成（`/update-dataset` 参照）
- 存在する: papers配列に論文を追加

#### Topics（関連トピックがある場合）
`arxiv-cs-2025/02_Topics/{topic_name}.md` を確認し、
- 存在しない: 主要トピックなら新規作成（`/update-topic` 参照）
- 存在する: papers配列に論文を追加

#### 論文メモのLinksセクション
作成/更新したエンティティへのリンクを追加:
```markdown
# Links
- Topics: [[federated-learning]], [[wireless-traffic-prediction]]
- Methods: [[gradient-compression]], [[federated-averaging]]
- Datasets: [[traffic-dataset]]
- Related Papers:
```

## 出力フォーマット（テンプレート）

```markdown
---
type: paper
arxiv_id: "{arxiv_id}"
title: "{title}"
year: 2025
primary: "{primary_category}"
categories: {categories配列}
authors: {authors配列}
published: "{published}"
updated: "{updated}"
doi: "{doi}"
pdf: "90_Attachments/pdf/2025/{arxiv_id}.pdf"
status: summarized
ai_summary_level: full
score: 0
signals: []
methods: []
tasks: []
datasets: []
claims: []
risks: []
created: "{今日の日付}"
---

# TL;DR（3行）
-

# Problem / Setting
- 入力/出力:
- 目的:
- 評価指標:
- 制約:
- 比較対象:

# Key Contributions
- [提案1]: [差分] → [根拠]
- [提案2]: [差分] → [根拠]

# Method
- 前処理:
- コアアルゴリズム:
- 学習手順:
- 推論手順:

# Experiments
- Dataset / Benchmark:
- Metrics:
- Baselines:
- Setup:

# Results（主要数値）
- [指標]で[ベースライン]に対して[差分]: 条件

# Ablations / Analysis
- 効いたコンポーネント:
- 効かない条件:

# Limitations / Risks
- 再現性:
- 外的妥当性:
- 計算コスト:
- 評価の穴:

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

## 実行例

`/read 1` → 1行目の論文を処理、メモ作成、関連エンティティ更新
`/read 5` → 5行目の論文を処理
