---
description: 著者（Author）エンティティを作成または更新
argument-hint: [著者名]
allowed-tools: Read, Write, Edit, Glob
---

# 著者エンティティ更新コマンド

著者名 `$ARGUMENTS` のAuthorエンティティを作成/更新します。

## 実行手順

### Step 1: 既存エンティティの確認
`arxiv-cs-2025/03_Entities/Authors/` に `A-{著者名}.md` が存在するか確認。

### Step 2: 新規作成または更新

**新規作成の場合**: 以下のテンプレートで作成

```markdown
---
type: entity
entity_type: author
name: "{著者名}"
aliases: []
affiliation: ""
homepage: ""
google_scholar: ""
semantic_scholar: ""
twitter: ""
papers: []
created: "{今日の日付}"
---

# {著者名}

## 所属
- （現在の所属機関）

## 研究分野
- （主な研究領域）

## 代表的な業績
- （重要な論文、プロジェクト）

## 論文リスト
- （この著者の論文へのリンク）

## 共著者ネットワーク
- （よく共著する研究者）

## 備考
- （その他の情報）
```

**更新の場合**:
- `papers` 配列に新しい論文を追加
- 「論文リスト」セクションに追記

## 保存先
`arxiv-cs-2025/03_Entities/Authors/A-{著者名}.md`

## 使用例
`/update-author Yoshua-Bengio` → Yoshua Bengioの著者ノートを作成/更新
