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

## 追加チェックポイント（2025-12-30追加）
- バイオメトリクス評価の網羅性: Accuracy だけでなく FAR/FRR/EER、ROC/DET 曲線、しきい値選定を記載。
- 攻撃シナリオの明確化: mimic/replay（写真・動画）/deepfake など攻撃種別・条件と成功率をセットで記載。
- 連続認証のリアルタイム性: 推論レイテンシ、デバイス（CPU/GPU/エッジ）での処理時間・消費電力の記載。
- 長期安定性: セッション跨ぎ（日跨ぎ）での性能変動、テンプレートエイジング評価の有無を確認。
- 参照論文: [[P-2501.01032_v1]]
