---
description: 論文メモの品質チェック・修正を行い、学んだ知見をSkillsに反映。重要概念はメモとSkillsに記録
argument-hint: [行番号]
allowed-tools: Read, Write, Edit, Glob, Bash
---

# 論文メモ品質チェックコマンド

`/read $ARGUMENTS` で作成されたメモの品質チェック・修正を行い、学んだ知見をSkillsに蓄積します。

## 実行手順

### Step 1: 対象論文メモの特定と読み込み

JSONLから論文情報を取得し、対応するメモファイルを特定:
```bash
source .venv/bin/activate && python -c "
import json
with open('arxiv_cs_peerreview_proxy_2025_daily.jsonl') as f:
    for i, line in enumerate(f, 1):
        if i == $ARGUMENTS:
            data = json.loads(line)
            print(f\"arxiv_id: {data['arxiv_id']}\")
            print(f\"primary: {data['primary_category']}\")
            break
"
```

メモファイルパス: `arxiv-cs-2025/01_Papers/2025/{primary}/P-{arxiv_id}.md`

### Step 2: 品質チェック（誤り・抜け漏れ確認）

以下の観点でメモを精査:

#### 2.1 致命的な抜け漏れチェック
- [ ] **Problem/Setting**: 入力/出力/評価/制約が全て明記されているか
- [ ] **Key Contributions**: 「何が新しいか」が具体的か（"性能向上"だけになっていないか）
- [ ] **Method**: 推論手順が記載されているか（見落としがち）
- [ ] **Results**: 数値が「絶対値＋差分＋条件」のセットになっているか
- [ ] **Limitations/Risks**: 地雷マップとして機能するか

#### 2.2 表現の分かりにくさチェック
- [ ] 専門用語に説明なく使っていないか
- [ ] 文が長すぎないか（1文1概念）
- [ ] 因果関係が明確か（AだからB、AによってB）
- [ ] 曖昧な表現がないか（「など」「いくつかの」→具体化）

#### 2.3 論文タイプ固有チェック
- **method paper**: Ablationが十分か、どのコンポーネントが効いているか明記
- **benchmark**: ベースライン選定の妥当性、公正性の評価
- **survey**: 分類軸の明確さ、カバレッジの評価
- **systems**: スケーラビリティ、レイテンシ、スループットの数値

### Step 3: 修正の実施

問題があれば、Editツールでメモファイルを修正。

修正時の記録（メモ末尾に追記）:
```markdown
# Check Log
- [日付] [修正内容の要約]
```

### Step 4: 再発防止のSkills更新（fix-*）

#### 4.1 ドメイン/内容に応じたSkillファイルを特定

既存のfix-* Skillsを確認:
```bash
ls -la .claude/skills/fix-*/
```

該当するドメインのSkillがあれば更新、なければ新規作成。

#### 4.2 Skill更新/作成の判断基準

| 修正内容 | 対応するSkill |
|----------|--------------|
| NLP特有の抜け漏れ | `fix-nlp/SKILL.md` |
| CV特有の抜け漏れ | `fix-cv/SKILL.md` |
| 連合学習特有 | `fix-federated-learning/SKILL.md` |
| 実験設定の問題 | `fix-experiments/SKILL.md` |
| 数値記載の問題 | `fix-results/SKILL.md` |
| 手法説明の問題 | `fix-method-description/SKILL.md` |

#### 4.3 Skill更新内容

既存Skillに追記する場合:
```markdown
## 追加チェックポイント（{日付}追加）
- {問題の概要}: {具体的なチェック項目}
- 参照論文: [[P-{arxiv_id}]]
```

新規Skill作成の場合: `.claude/skills/fix-{domain}/SKILL.md` を作成

### Step 5: 重要概念・キーワードの抽出と記録（topic-*）

#### 5.1 重要概念の特定

論文から以下を抽出:
- **新規概念**: 論文で初めて登場した用語・手法
- **重要キーワード**: 理解に必須の専門用語
- **関連概念**: 既存知識との接続点

#### 5.2 概念メモの作成/更新

`arxiv-cs-2025/02_Topics/` に概念メモを作成:
- 新規: `/update-topic {概念名}` で作成
- 既存: 論文リンクを追加

#### 5.3 topic-* Skillの更新

`.claude/skills/topic-{domain}/SKILL.md` に記録:

```markdown
## キーワード辞書

### {キーワード}
- 定義: {簡潔な定義}
- 関連メモ: [[{トピック名}]]
- 初出論文: [[P-{arxiv_id}]]
- ファクトチェック状態: 未確認 / 確認済み（{日付}）
```

#### 5.4 ファクトチェック

新しいキーワードについて:
1. 定義が正確か確認（論文本文と照合）
2. 既存の概念メモと矛盾がないか確認
3. 必要に応じてWebSearchで最新情報を確認

### Step 6: 最終確認とステータス更新

全てのチェックと修正が完了したら:

1. メモファイルの `status` を更新:
   - 軽微な修正のみ: `summarized` → `verified`
   - 大幅な修正あり: `summarized` のまま（再度 `/check` 推奨）

2. 更新されたSkillsの一覧を出力

## 出力サマリー

チェック完了後、以下を報告:

```
## Check Results for P-{arxiv_id}

### 修正内容
- {修正1}
- {修正2}

### 更新されたSkills
- fix-{domain}/SKILL.md: {追加内容の要約}
- topic-{domain}/SKILL.md: {追加キーワード}

### 新規作成されたメモ
- 02_Topics/{topic_name}.md

### ステータス
- 修正前: {status}
- 修正後: {status}
```

## 使用例

```
/read 1
/check 1
```

論文1を読み込み→チェック→修正→Skills更新の流れ
