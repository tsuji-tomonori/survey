---
type: method
name: "Hierarchical Linear Modeling"
aliases: ["HLM", "Multilevel Modeling", "Mixed-Effects Modeling"]
category: ["statistical-analysis", "regression"]
created: "2025-12-27"
---

# Hierarchical Linear Modeling (HLM)

## Overview
階層線形モデリング（HLM）は、ネスト構造・クラスター構造・階層構造を持つデータを分析するための統計モデル。固定効果と変量効果の両方を推定し、グループ内・グループ間の複雑な関係を捉える。

## Key Concepts
- **固定効果（Fixed Effects）**: 予測変数と応答変数の平均的な関係（全グループで一定と仮定）
- **変量効果（Random Effects）**: グループ間の変動を捉え、関係がグループ間で異なることを許容
- **ネスト構造**: 例：参加者→セッション→測定値

## Applications
- 縦断研究（繰り返し測定データ）
- クラスターサンプリング
- 心理・医学研究（個人差を考慮した分析）

## Implementation
- R: `lme4`パッケージ（`lmer()`関数）
- Python: `statsmodels.formula.api.mixedlm()`

## Papers
- [[P-2501.01471_v2]] - SAD検出におけるHRV分析に使用
