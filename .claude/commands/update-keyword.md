---
description: 重要キーワードのメモを作成/更新し、対応するtopic-* Skillにも登録
argument-hint: [キーワード名]
allowed-tools: Read, Write, Edit, Glob
---

# キーワードメモ更新コマンド

キーワード `$ARGUMENTS` のメモを作成/更新し、topic-* Skillにも登録します。

## 実行手順

### Step 1: 既存メモの確認

`arxiv-cs-2025/02_Topics/` に `$ARGUMENTS.md` が存在するか確認。

### Step 2: ドメイン判定

キーワードの所属ドメインを判定:
- NLP関連 → `topic-nlp`
- CV関連 → `topic-cv`
- ML全般 → `topic-ml`
- 分野横断 → `topic-common`

### Step 3: メモの作成/更新

**新規作成の場合**:

```markdown
---
type: keyword
keyword: "{$ARGUMENTS}"
aliases: []
domain: "{判定されたドメイン}"
definition: ""
first_paper: ""
fact_checked: false
fact_check_date: ""
created: "{今日の日付}"
---

# {$ARGUMENTS}

## 定義
- （論文から抽出した定義）

## 数式（該当する場合）
$$
（数式があれば）
$$

## 直感的な説明
- （平易な言葉での説明）

## 使用される文脈
- （どのような場面で使われるか）

## 具体例
- （具体的な適用例）

## 関連概念
- 上位概念:
- 下位概念:
- 類似概念:
- 対立概念:

## 歴史・発展
- （概念の発展経緯）

## 主要論文
- [[P-{arxiv_id}]]（発見元論文）

## 実装リソース
- （公開コード、ライブラリ等）

## 注意点・よくある誤解
- （間違えやすいポイント）

## ファクトチェックログ
| 日付 | 確認内容 | ソース | 結果 |
|------|----------|--------|------|
| | | | |
```

**更新の場合**:
- 「主要論文」セクションに新しい論文を追加
- 必要に応じて定義や説明を拡充

### Step 4: topic-* Skillへの登録

対応する `.claude/skills/topic-{domain}/SKILL.md` に追記:

```markdown
#### {$ARGUMENTS}
- 定義: {簡潔な定義}
- 関連メモ: [[{$ARGUMENTS}]]
- 初出論文: [[P-{arxiv_id}]]
- ファクトチェック: 未確認
```

### Step 5: ファクトチェック（オプション）

新規キーワードの場合:
1. 論文本文と定義の照合
2. 既存メモとの矛盾確認
3. 確認完了後、`fact_checked: true` と日付を更新

## 保存先
- メモ: `arxiv-cs-2025/02_Topics/{$ARGUMENTS}.md`
- Skill: `.claude/skills/topic-{domain}/SKILL.md`

## 使用例

```
/update-keyword gradient-compression
/update-keyword federated-averaging
/update-keyword attention-mechanism
```
