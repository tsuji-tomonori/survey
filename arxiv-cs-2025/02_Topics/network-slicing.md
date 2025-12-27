---
type: topic
name: "Network Slicing"
aliases: ["ネットワークスライシング", "RAN Slicing", "5G Slicing"]
category: "wireless-networks"
created: "2025-12-27"
---

# Network Slicing

## 概要
単一の物理ネットワークインフラ上に、異なる要件を持つ複数の論理ネットワーク（スライス）を仮想的に構築する技術。5G/6Gの核心技術の一つ。

## 主要な概念
- **eMBB (enhanced Mobile Broadband)**: 高スループット重視
- **URLLC (Ultra-Reliable Low-Latency Communications)**: 低遅延・高信頼性重視
- **mMTC (massive Machine-Type Communications)**: 大量接続重視
- **SLA (Service Level Agreement)**: 各スライスの要件定義
- **Intent-based networking**: 高レベル意図からの自動設定

## 技術的課題
- リソース配分最適化（Inter-slice/Intra-slice scheduling）
- 動的なスライス要件への適応
- 複数スライス間の干渉管理
- SLA違反の最小化

## 関連研究
- [[P-2501.00950_v1]]: MARLベースのインテント駆動RANスライシングスケジューラ

## 関連トピック
- [[radio-resource-management]]
- [[6G-networks]]
