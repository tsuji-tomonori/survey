---
name: fix-common
description: codex用Skill（内容は .claude/skills/fix-common/SKILL.md に準拠）
---

# 共通エラー修正Skill（codex）

このSkillは `.claude/skills/fix-common/SKILL.md` の内容に準拠して運用します。

## 追加チェックポイント（2025-12-30追加）
- メタデータのNull正規化: YAMLにおいて`doi`や`journal_ref`など未設定フィールドは空文字に統一し、`"None"`や`null`文字列を残さない。該当時は修正し、チェックログに記録。参照論文: [[P-2501.07202_v1]]
- Results記載の厳格化: 主要結果は「絶対値＋差分＋条件（同パラメータ規模/同データ量/同評価設定）」をセットで記載する。
- Method記載の徹底: 推論手順（デコード/検索戦略、概算計算量/レイテンシ）を明記する。
- Problem/Settingの4点セット: 入力/出力・目的・評価指標・実運用上の制約を最初に揃える。
