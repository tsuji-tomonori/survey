---
description: 手法（Method）エンティティを作成または更新
argument-hint: [手法名]
allowed-tools: Read, Write, Edit, Glob
---

# 手法エンティティ更新コマンド

手法名 `$ARGUMENTS` のMethodエンティティを作成/更新します。

## 実行手順

### Step 1: 既存エンティティの確認
`arxiv-cs-2025/03_Entities/Methods/` に `M-{手法名}.md` が存在するか確認。

### Step 2: 新規作成または更新

**新規作成の場合**: 以下のテンプレートで作成

```markdown
---
type: entity
entity_type: method
name: "{手法名}"
aliases: []
category: ""  # architecture / optimization / training / inference / evaluation
papers: []
created: "{今日の日付}"
---

# {手法名}

## 定義
- （手法の定義を1-2段落で）

## 主要コンポーネント
- （構成要素を箇条書き）

## 適用分野
- （どのタスク/領域で使われるか）

## 代表的な論文
- （この手法を提案/発展させた論文へのリンク）

## 派生・改良
- （この手法の派生版）

## 関連手法
- （比較対象となる手法へのリンク）

## 実装リソース
- （公開コード、ライブラリ等）
```

**更新の場合**:
- `papers` 配列に新しい論文を追加
- 必要に応じて「派生・改良」セクションを更新

## 保存先
`arxiv-cs-2025/03_Entities/Methods/M-{手法名}.md`

## 使用例
`/update-method transformer` → Transformerの手法ノートを作成/更新
`/update-method retrieval-augmented-generation` → RAGの手法ノートを作成/更新
