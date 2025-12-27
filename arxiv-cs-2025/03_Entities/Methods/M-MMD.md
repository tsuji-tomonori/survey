---
type: method
name: "MMD"
name_full: "Maximum Mean Discrepancy"
name_ja: "最大平均不一致度"
category: metric
status: active
created: "2025-12-27"
updated: "2025-12-27"
---

# MMD (Maximum Mean Discrepancy)

## 概要

カーネル二標本検定に基づく分布間距離の指標。任意のパラメトリック形式の分布に対応可能で、深層学習での分布マッチングに広く使用される。

## 定義

2つの分布 P, Q のMMD距離:

$$\text{MMD}^2(P, Q) = \mathbb{E}_{x,x' \sim P}[k(x,x')] - 2\mathbb{E}_{x \sim P, y \sim Q}[k(x,y)] + \mathbb{E}_{y,y' \sim Q}[k(y,y')]$$

ここで $k(\cdot, \cdot)$ はカーネル関数（通常RBFカーネル）。

## RBFカーネルでの計算

$$\text{MMD}_W(Q||P) = \sum_{w_i \in W} \mathbb{E}_{Q,Q}[\text{RBF}_{w_i}(Q,Q)] - 2\sum_{w_i \in W}\mathbb{E}_{Q,P}[\text{RBF}_{w_i}(Q,P)] + \sum_{w_i \in W}\mathbb{E}_{P,P}[\text{RBF}_{w_i}(P,P)]$$

複数のウィンドウサイズ $W$ でRBFカーネルを使用することで、様々なスケールの分布差を捉える。

## 利点
- **ノンパラメトリック**: 分布の形状を仮定しない
- **計算効率**: サンプルベースで効率的に推定可能
- **微分可能**: ニューラルネットワークの損失関数として使用可能

## 使用例

### 画像生成
- InfoVAE: 潜在空間での分布マッチング
- MMD-GAN: 敵対的訓練の代替

### 時系列生成
- PaD-TS (AAAI 2025): 母集団レベル特性（CC分布）のマッチング

### ドメイン適応
- DAN, JAN: ソース・ターゲットドメイン間の特徴分布マッチング

## 参考文献
- Gretton, A., et al. (2012). A kernel two-sample test. JMLR.

## Papers
- [[P-2501.00910_v1]]: 時系列生成での機能依存分布マッチング

## Links
- Topics: [[distribution-matching]], [[kernel-methods]]
- Related Methods: [[Wasserstein-distance]], [[KL-divergence]]
