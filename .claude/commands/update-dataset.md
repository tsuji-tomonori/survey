---
description: データセット（Dataset）エンティティを作成または更新
argument-hint: [データセット名]
allowed-tools: Read, Write, Edit, Glob
---

# データセットエンティティ更新コマンド

データセット名 `$ARGUMENTS` のDatasetエンティティを作成/更新します。

## 実行手順

### Step 1: 既存エンティティの確認
`arxiv-cs-2025/03_Entities/Datasets/` に `D-{データセット名}.md` が存在するか確認。

### Step 2: 新規作成または更新

**新規作成の場合**: 以下のテンプレートで作成

```markdown
---
type: entity
entity_type: dataset
name: "{データセット名}"
aliases: []
domain: ""  # NLP / CV / multimodal / tabular / etc
task: ""  # classification / generation / QA / etc
size: ""  # サンプル数やトークン数
languages: []
license: ""
url: ""
papers: []
created: "{今日の日付}"
---

# {データセット名}

## 概要
- （データセットの説明を1-2段落で）

## 統計情報
| 項目 | 値 |
|------|-----|
| サイズ | |
| 言語 | |
| ドメイン | |
| タスク | |

## データ形式
- （入力/出力の形式、アノテーション内容）

## 評価指標
- （このデータセットで一般的に使われる指標）

## 使用論文
- （このデータセットを使用した論文へのリンク）

## 注意点
- （データリークの可能性、バイアス、ライセンス制約等）

## 入手方法
- （ダウンロードリンク、アクセス方法）
```

**更新の場合**:
- `papers` 配列に新しい論文を追加
- 必要に応じて「使用論文」セクションを更新

## 保存先
`arxiv-cs-2025/03_Entities/Datasets/D-{データセット名}.md`

## 使用例
`/update-dataset ImageNet` → ImageNetのデータセットノートを作成/更新
`/update-dataset GLUE` → GLUEのデータセットノートを作成/更新
