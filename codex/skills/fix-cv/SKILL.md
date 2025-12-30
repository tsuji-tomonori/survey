---
name: fix-cv
description: codex用Skill（内容は .claude/skills/fix-cv/SKILL.md に準拠）
---

# CV特有エラー修正Skill（codex）

このSkillは `.claude/skills/fix-cv/SKILL.md` の内容に準拠して運用します。

## 追加チェックポイント（2025-12-30追加）
- トポロジー保存損失の定義不足: 「simple voxel」「supervoxel」「critical component」を簡潔に定義する。定義が無い場合は用語追加。
- トポロジー評価の抜け漏れ: Betti number error, ERL/Normalized ERL を成績一覧に含め、指標の向き（大小どちらが良いか）を明記。
- 計算量の根拠明記: O(n)/O(n log n)/O(n²) など計算量の差分はアルゴリズム根拠（BFS, persistent homology 等）と合わせて記述。
- リンク整合性: Methods 参照は `[[M-...]]` 形式に統一（例: `[[M-supervoxel-loss]]`）。
- 参照論文: [[P-2501.01022_v3]]
