---
type: topic
name: "Instance Segmentation"
aliases: ["インスタンスセグメンテーション"]
domain: ["computer-vision", "medical-imaging"]
created: "2025-12-27"
---

# Instance Segmentation

## 概要
画像内の各オブジェクトを個別に識別・セグメンテーションするタスク。セマンティックセグメンテーション（クラスごとの分類）と異なり、同一クラスの複数インスタンスを区別する。

## 主要な課題
- **トポロジー保存**: 細長い構造（ニューロン、血管）での分割・結合エラー
- **オクルージョン**: 重なり合うオブジェクトの分離
- **スケール変動**: 様々なサイズのオブジェクトの検出

## 主要手法
- Mask R-CNN: 検出 + セグメンテーションの2段階
- YOLACT: 1段階のリアルタイム手法
- トポロジー保存損失: [[M-supervoxel-loss]], clDice, TopoLoss

## 応用分野
- **神経科学**: ニューロン再構成、コネクトミクス
- **医用画像**: 血管セグメンテーション、細胞計数
- **自動運転**: 歩行者・車両検出
- **インフラ**: ひび割れ検出

## 評価指標
- mAP (mean Average Precision)
- Dice, ARI, VOI
- トポロジー指標: Betti number error, ERL

## 関連論文
- [[P-2501.01022_v3]]: Supervoxel-based topology-aware loss（AAAI 2025）

## 関連トピック
- [[semantic-segmentation]]
- [[object-detection]]
- [[neuron-reconstruction]]
