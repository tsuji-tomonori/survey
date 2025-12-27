---
type: topic
name: "Diffusion Models"
name_ja: "拡散モデル"
aliases: ["DM", "DDPM", "Score-based models", "Denoising Diffusion"]
category: generative-model
status: active
created: "2025-12-27"
updated: "2025-12-27"
---

# Diffusion Models

## 概要

データに段階的にノイズを加える順過程と、ノイズを除去して元データを復元する逆過程を学習する生成モデル。画像・動画・音声・時系列など多様なドメインでSOTAを達成。

## 基本原理

### 順過程 (Forward Process)
$$q(x^t|x^{t-1}) = \mathcal{N}(\sqrt{1-\beta^t}x^{t-1}, \beta^t I)$$

### 逆過程 (Reverse Process)
$$p_\theta(x^{t-1}|x^t) = \mathcal{N}(\mu_\theta, \Sigma_\theta)$$

### 訓練目標
$$\mathcal{L}_0(\theta) = \mathbb{E}_{t,x^0}[\|x^0 - x^0(\theta)\|^2]$$

## 主要手法

### 画像生成
- DDPM (Ho et al. 2020)
- Improved DDPM (Nichol & Dhariwal 2021)
- DiT (Peebles & Xie 2023): Transformerバックボーン

### テキスト→画像
- DALL-E 2, Stable Diffusion, GLIDE

### 時系列
- Diffusion-TS (ICLR 2024): trend + Fourier
- PaD-TS (AAAI 2025): 母集団レベル特性保存

## GANs/VAEsとの比較

| 観点 | Diffusion | GANs | VAEs |
|------|-----------|------|------|
| 訓練安定性 | 高 | 低（mode collapse） | 中 |
| 生成品質 | 高 | 高 | 中 |
| 多様性 | 高 | 低（mode collapse） | 中 |
| 推論速度 | 低（反復） | 高 | 高 |

## 関連論文

```dataview
TABLE title, year, score
FROM "01_Papers"
WHERE contains(methods, "diffusion-model")
SORT score DESC
```

## Papers
- [[P-2501.00910_v1]]: PaD-TS - 時系列生成での母集団レベル特性保存

## Links
- Methods: [[DDPM]], [[DiT]], [[Score-matching]]
- Related Topics: [[generative-models]], [[time-series-generation]]
