---
type: topic
name: "Radio Resource Management"
aliases: ["RRM", "無線リソース管理", "radio-resource-management"]
category: "wireless-networks"
created: "2025-12-30"
---

# Radio Resource Management (RRM)

## 概要
無線アクセスネットワーク（RAN）で、時間・周波数・空間リソース（RB/RBG、送信電力、スケジューリング等）を効率よく配分するための総称。5G/6Gにおけるスループット、遅延、信頼性のトレードオフを最適化する中核技術。

## 主要な構成要素
- スケジューリング: Inter-slice（スライス間）/Intra-slice（スライス内）
- リソースブロック割当: RB/RBGの時間周波数資源の配分
- パワーコントロール: 送信電力の最適化
- リンク適応: MCS選択、HARQ制御

## 課題
- SLA要件（スループット/遅延/損失）の同時満足
- 高需要時における優先スライス保護と公平性
- 異なるネットワークシナリオへの適応・汎化

## 関連研究
- [[P-2501.00950_v1]]: インテント駆動のRANスライシングに対するMARL/PPOベースのRRM

## 関連トピック
- [[network-slicing]]
- [[6G-networks]]

