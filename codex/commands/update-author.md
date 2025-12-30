---
description: 著者（Author）エンティティを作成または更新
argument-hint: [著者名]
allowed-tools: Read, Write, Edit, Glob
---

# 著者エンティティ更新コマンド（codex）

著者名 `$ARGUMENTS` のAuthorエンティティを作成/更新します。

## 実行手順

### Step 1: 既存エンティティの確認
`arxiv-cs-2025/03_Entities/Authors/` に `A-{著者名}.md` が存在するか確認。

### Step 2: 新規作成または更新

新規作成の場合のテンプレートや更新方針は、他エンティティ（Methods/Datasets）に準拠。

## 保存先
`arxiv-cs-2025/03_Entities/Authors/A-{著者名}.md`

## 使用例
`/update-author John-Doe`

