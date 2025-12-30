---
description: データセットエンティティ更新コマンド（codex）
argument-hint: [データセット名]
allowed-tools: Read, Write, Edit, Glob
---

# データセットエンティティ更新コマンド

## 実行手順

### Step 1: 既存エンティティの確認
`arxiv-cs-2025/03_Entities/Datasets/` を確認。

### Step 2: 新規作成または更新

新規作成テンプレートや更新手順はClaude版と同様。主要セクション:
- 概要
- 統計情報
- データ形式
- 評価指標
- 使用論文
- 注意点
- 入手方法

更新時は `papers` 配列の更新を実施。

## 保存先
`arxiv-cs-2025/03_Entities/Datasets/D-{データセット名}.md`

## 使用例
`/update-dataset ImageNet`

