---
description: 手法（Method）エンティティを作成または更新（codex）
argument-hint: [手法名]
allowed-tools: Read, Write, Edit, Glob
---

# 手法エンティティ更新コマンド

手法名 `$ARGUMENTS` のMethodエンティティを作成/更新します。

## 実行手順

### Step 1: 既存エンティティの確認
`arxiv-cs-2025/03_Entities/Methods/` に `M-{手法名}.md` が存在するか確認。

### Step 2: 新規作成または更新
- 新規はテンプレートに従い作成
- 更新は `papers` 配列等を追記

## 保存先
`arxiv-cs-2025/03_Entities/Methods/M-{手法名}.md`

## 使用例
`/update-method transformer`

