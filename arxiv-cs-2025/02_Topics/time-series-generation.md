---
type: topic
name: "Time Series Generation"
name_ja: "時系列生成"
aliases: ["TS generation", "synthetic time series", "時系列データ生成"]
category: ml-application
status: active
created: "2025-12-27"
updated: "2025-12-27"
---

# Time Series Generation

## 概要

時系列データを生成する技術。データ拡張、プライバシー保護、欠損値補完などの目的で使用される。

## 主要アプローチ

### GAN-based
- TimeGAN (NeurIPS 2019): RNNベース、stepwise supervised loss
- C-RNN-GAN: 連続値時系列生成

### VAE-based
- TimeVAE: convolution + trend/seasonal分解
- KoVAE: Koopmanベースの事前分布

### Diffusion-based
- Diffusion-TS (ICLR 2024): trend + Fourier分解、SOTA
- PaD-TS (AAAI 2025): 母集団レベル特性保存

## 評価指標

### 個別レベル
- **Discriminative Accuracy (DA)**: real/syntheticの識別精度
- **Predictive score**: 合成データで訓練したモデルの予測性能

### 母集団レベル
- **VDS (Value Distribution Shift)**: 値分布のKLダイバージェンス
- **FDDS (Functional Dependency Distribution Shift)**: 次元間相関分布のシフト

## 応用分野
- ヘルスケア（プライバシー保護データ共有）
- エネルギー（需要予測用データ拡張）
- 金融（リスクシナリオ生成）

## 関連論文

```dataview
TABLE title, year, score
FROM "01_Papers"
WHERE contains(tasks, "time-series-generation")
SORT score DESC
```

## Papers
- [[P-2501.00910_v1]]: PaD-TS - 母集団レベル特性保存型Diffusion

## Links
- Methods: [[DDPM]], [[DiT]], [[GAN]], [[VAE]]
- Related Topics: [[synthetic-data]], [[data-augmentation]]
