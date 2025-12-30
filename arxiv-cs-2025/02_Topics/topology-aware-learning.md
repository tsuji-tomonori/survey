---
type: topic
name: "Topology-aware Learning"
aliases: ["トポロジー保存学習", "connectivity-preserving learning", "topology-preserving"]
domain: ["computer-vision", "medical-imaging", "neuroscience"]
created: "2025-12-30"
---

# Topology-aware Learning

## 概要
セグメンテーションやグラフ構造の学習において、対象の連結性やトポロジー（分割・結合、穴、ベティ数）が保存されるように制約や損失を導入する枠組み。

## 代表的アプローチ
- Persistent Homology系: [[M-topology-aware-loss]]（Betti数に基づく損失、計算コストが高い）
- Skeleton/連結性系: clDice（soft skeletonによる連結性維持）
- Supervoxel系: [[M-supervoxel-loss]]（critical component検出によりO(n)で連結性を保つ）

## 評価指標
- Betti number error: トポロジーの差異（小さいほど良い）
- ERL / Normalized ERL: スケルトンの連続性（大きいほど良い）
- VOI, ARI, Dice: 画素・ボクセルレベルの一致度

## 応用領域
- ニューロン・血管など細長い構造のインスタンスセグメンテーション
- クラック検出、道路ネットワーク抽出

## 関連論文
- [[P-2501.01022_v3]]: Supervoxel-based topology-aware loss（AAAI 2025）

## 関連トピック
- [[instance-segmentation]]
- [[neuron-reconstruction]]

