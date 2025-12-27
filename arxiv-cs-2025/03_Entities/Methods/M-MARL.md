---
type: method
name: "MARL (Multi-Agent Reinforcement Learning)"
aliases: ["Multi-Agent RL", "マルチエージェント強化学習"]
category: "reinforcement-learning"
created: "2025-12-27"
---

# MARL (Multi-Agent Reinforcement Learning)

## 概要
複数のエージェントが同一環境で同時に学習・行動する強化学習フレームワーク。エージェント間の協調・競争・独立行動を扱う。

## 主要な特徴
- 各エージェントが部分観測（POMDP）に基づき行動
- パラメータ共有による同種エージェントの効率的学習
- 協調型（cooperative）、競争型（competitive）、混合型（mixed）の設定

## 代表的な手法
- Independent Learners
- Centralized Training with Decentralized Execution (CTDE)
- Parameter Sharing
- Communication-based methods

## 関連論文
- [[P-2501.00950_v1]]: RANスライシングでのIntra-sliceスケジューラにパラメータ共有MARLを適用

## 関連手法
- [[M-PPO]]: MARLでよく使用されるポリシー最適化手法
