---
type: method
name: "Siamese Network"
name_full: "Siamese Neural Network"
name_ja: "シャムネットワーク"
category: neural-network
status: active
created: "2025-12-27"
updated: "2025-12-27"
---

# Siamese Network

## 概要

2つの入力を同一構造のネットワーク（重み共有）に通し、出力された特徴ベクトル間の距離を計算することで類似度を測定するアーキテクチャ。One-shot/Few-shot学習、顔認証、署名検証などペア比較タスクに広く使用される。

## アーキテクチャ

```
入力1 → [CNN/Encoder] → 特徴ベクトル1 ─┐
                                      ├→ 距離計算 → 類似度スコア
入力2 → [CNN/Encoder] → 特徴ベクトル2 ─┘
         (重み共有)
```

## 損失関数

### Contrastive Loss
$$L = (1-Y) \cdot \frac{1}{2} D^2 + Y \cdot \frac{1}{2} \max(0, m - D)^2$$

- $Y$: ラベル（同一クラス: 0, 異なるクラス: 1）
- $D$: 特徴ベクトル間のユークリッド距離
- $m$: マージン

### Triplet Loss
$$L = \max(0, D(a, p) - D(a, n) + m)$$

- $a$: アンカー
- $p$: ポジティブ（同一クラス）
- $n$: ネガティブ（異なるクラス）

## 利点
- **少ないデータ**: 各クラス数サンプルでも学習可能
- **新クラス追加容易**: 再学習不要で新しいクラスを追加可能
- **解釈性**: 特徴空間での距離として類似度を直接解釈

## 使用例

### 顔認証
- FaceNet: Triplet Lossで顔埋め込みを学習
- DeepFace: Siamese構造で顔照合

### 生体認証
- DynamicLip: 唇の動的特徴でユーザー認証

### One-shot Learning
- Matching Networks
- Prototypical Networks

## Papers
- [[P-2501.01032_v1]]: 唇動態に基づく連続認証でContrastive Loss使用

## Links
- Topics: [[metric-learning]], [[few-shot-learning]]
- Related Methods: [[triplet-loss]], [[contrastive-learning]]
