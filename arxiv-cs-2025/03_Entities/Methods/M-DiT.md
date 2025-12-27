---
type: method
name: "DiT"
name_full: "Diffusion Transformer"
name_ja: "拡散Transformer"
category: architecture
status: active
created: "2025-12-27"
updated: "2025-12-27"
---

# DiT (Diffusion Transformer)

## 概要

Peebles & Xie (ICCV 2023) が提案した、Diffusion Modelのバックボーンとして設計されたTransformerアーキテクチャ。U-Netの代替として高いスケーラビリティを示す。

## 特徴

### アーキテクチャ
- Vanilla Transformer Encoderに類似した構造
- 条件情報（拡散ステップ等）をadaLN-Zeroで注入
- 隠れ状態を6チャンクに分割し、段階的に条件埋め込みを導入

### 条件注入 (adaLN-Zero)
1. Layer Norm 1 → Cond Injection 1, 2
2. Multi-Head Attention
3. Layer Norm 2 → Cond Injection 3, 4
4. Feed Forward

### 利点
- **高スループット**: Multi-head attentionの並列処理
- **スケーラビリティ**: パラメータ増加に伴う性能向上
- **柔軟な条件付け**: 拡散ステップ、クラスラベル等

## 使用例

### 画像生成
- DiT-XL/2 (Peebles & Xie 2023): ImageNetで256x256画像生成SOTA

### 時系列生成
- PaD-TS (AAAI 2025): Temporal/Cross-dim dual-channelの最終層

## 参考文献
- Peebles, W., & Xie, S. (2023). Scalable Diffusion Models with Transformers. ICCV 2023.

## Papers
- [[P-2501.00910_v1]]: 時系列生成でDiTブロックを使用

## Links
- Topics: [[diffusion-models]], [[time-series-generation]]
- Related Methods: [[DDPM]], [[Transformer]]
