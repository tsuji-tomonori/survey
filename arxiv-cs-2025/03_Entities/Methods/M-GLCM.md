---
type: method
name: "GLCM"
name_full: "Gray-Level Co-occurrence Matrix"
name_ja: "グレーレベル同時生起行列"
category: feature-extraction
status: active
created: "2025-12-27"
updated: "2025-12-27"
---

# GLCM (Gray-Level Co-occurrence Matrix)

## 概要

画像のテクスチャ特徴を抽出するための統計的手法。隣接ピクセル間のグレーレベル値の空間的な関係を行列として表現し、そこから各種テクスチャ特徴量を計算する。

## 定義

GLCM $P(i,j|d,\theta)$: 距離 $d$、方向 $\theta$ で隣接するピクセルペアのうち、一方がグレーレベル $i$、他方が $j$ であるペアの出現頻度。

一般的な方向:
- 0° (水平): $(1, 0)$
- 45° (対角): $(1, 1)$
- 90° (垂直): $(0, 1)$
- 135° (反対角): $(-1, 1)$

## 代表的なテクスチャ特徴量

### ASM (Angular Second Moment / Energy)
$$ASM = \sum_i \sum_j P(i,j)^2$$
テクスチャの均一性を測定。

### Contrast
$$Contrast = \sum_i \sum_j (i-j)^2 P(i,j)$$
局所的なコントラストの強さを測定。

### Correlation
$$Correlation = \sum_i \sum_j \frac{(i-\mu_i)(j-\mu_j)P(i,j)}{\sigma_i \sigma_j}$$
隣接ピクセル間の線形依存度を測定。

### IDM (Inverse Difference Moment / Homogeneity)
$$IDM = \sum_i \sum_j \frac{P(i,j)}{1+(i-j)^2}$$
局所的な均質性を測定。

### Entropy
$$Entropy = -\sum_i \sum_j P(i,j) \log P(i,j)$$
テクスチャのランダム性/複雑さを測定。

## 利点
- **解釈性**: 各特徴量が物理的意味を持つ
- **計算効率**: 比較的軽量な計算
- **汎用性**: 医療画像、リモートセンシング、生体認証等で広く使用

## 制限
- **方向・距離依存**: パラメータ選択が結果に影響
- **回転不変性なし**: 回転に対して不変ではない
- **スケール感度**: 画像サイズや解像度に敏感

## 使用例

### 医療画像解析
- CT/MRI画像のテクスチャ解析
- 病変検出・分類

### 生体認証
- DynamicLip: 唇テクスチャの特徴抽出（6領域×8方向）

### リモートセンシング
- 土地被覆分類

## 参考文献
- Haralick, R.M., et al. (1973). Textural features for image classification. IEEE Trans. SMC.

## Papers
- [[P-2501.01032_v1]]: 唇領域のテクスチャ特徴抽出にGLCM使用

## Links
- Topics: [[texture-analysis]], [[image-feature-extraction]]
- Related Methods: [[LBP]], [[Gabor-filter]]
