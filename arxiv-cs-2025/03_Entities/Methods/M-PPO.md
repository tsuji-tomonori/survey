---
type: method
name: "PPO (Proximal Policy Optimization)"
aliases: ["Proximal Policy Optimization", "近傍方策最適化"]
category: "reinforcement-learning"
created: "2025-12-27"
---

# PPO (Proximal Policy Optimization)

## 概要
信頼領域手法の安定性と実装の簡潔さを両立した方策勾配法。クリップ目的関数により大きな方策更新を制限し、学習の安定性を確保。

## 主要な特徴
- クリップ目的関数: `min(r(θ)A, clip(r(θ), 1-ε, 1+ε)A)`
- Actor-Criticアーキテクチャ
- 連続・離散行動空間の両方に対応
- 並列環境でのサンプル収集が容易

## ハイパーパラメータ
- クリップ範囲 ε (典型的に0.1-0.3)
- エントロピー係数
- GAE λ (一般化優位関数推定)

## 関連論文
- [[P-2501.00950_v1]]: Inter-slice/Intra-sliceスケジューラの学習にPPOを使用

## 参考文献
- Schulman et al., "Proximal Policy Optimization Algorithms", arXiv:1707.06347, 2017
