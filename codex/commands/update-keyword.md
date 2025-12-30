---
description: 重要キーワード辞書の更新（codex）
argument-hint: [キーワード]
allowed-tools: Read, Write, Edit, Glob
---

# キーワード更新コマンド

対応する `02_Topics/{topic}.md` と `codex/skills/topic-{domain}/SKILL.md` を更新。

## 実行手順
- 既存ノートの有無を確認
- 新規なら `/update-topic` で作成
- 既存なら papers 配列と辞書項目を更新

## 辞書項目テンプレ
```markdown
### {キーワード}
- 定義: ...
- 関連メモ: [[{トピック名}]]
- 初出論文: [[P-{arxiv_id}]]
- ファクトチェック状態: 未確認 / 確認済み（{日付}）
```

