---
name: fix-common
description: codex用Skill（内容は .claude/skills/fix-common/SKILL.md に準拠）
---

# 共通エラー修正Skill（codex）

このSkillは `.claude/skills/fix-common/SKILL.md` の内容に準拠して運用します。

## 追加チェックポイント（2025-12-30追加）
- メタデータのNull正規化: YAMLにおいて`doi`や`journal_ref`など未設定フィールドは空文字に統一し、`"None"`や`null`文字列を残さない。該当時は修正し、チェックログに記録。参照論文: [[P-2501.07202_v1]]
