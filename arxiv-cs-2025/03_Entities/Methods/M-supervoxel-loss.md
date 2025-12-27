---
type: method
name: "Supervoxel-based Loss Function"
aliases: ["supervoxel loss", "critical component loss", "connectivity-preserving loss"]
category: "loss-function"
domain: ["computer-vision", "medical-imaging", "neuroscience"]
created: "2025-12-27"
---

# Supervoxel-based Loss Function

## 概要
デジタルトポロジーの「simple voxel」概念を連結ボクセル集合（supervoxel）に拡張し、セグメンテーションの連結性を保存する損失関数。

## 核心アイデア
- **Critical component**: 連結成分の追加/削除がトポロジー（連結成分数）を変える supervoxel
- **Negatively critical**: 偽陰性マスク中の成分で、除去すると ground truth の連結性が変わる
- **Positively critical**: 偽陽性マスク中の成分で、除去すると予測の連結性が変わる

## 数式
```
L(y,ŷ) = (1-α)L₀(y,ŷ) + αβΣL₀(y_C,ŷ_C) + α(1-β)ΣL₀(y_C,ŷ_C)
```
- L₀: 基本損失（cross-entropy, Dice等）
- α: ボクセルレベル vs 構造レベルの重み
- β: split vs merge エラーの重み

## 計算量
- O(n) の線形時間（BFS + ハッシュテーブル）
- 既存手法（TopoLoss: O(n log n), DMT: O(n²)）より高速

## 制約
- 木構造オブジェクトに限定（ニューロン、血管等）
- ループや穴を持つ構造には線形時間保証なし

## 実装
- GitHub: https://github.com/AllenNeuralDynamics/supervoxel-loss

## 関連論文
- [[P-2501.01022_v3]]: 提案論文（AAAI 2025）

## 関連手法
- [[M-topology-aware-loss]]: persistent homology ベース
- clDice: soft skeleton ベース
- MALIS: affinity maximin
