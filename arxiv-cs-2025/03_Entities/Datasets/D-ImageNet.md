---
type: entity
entity_type: dataset
name: "ImageNet"
aliases: ["ILSVRC", "ImageNet Large Scale Visual Recognition Challenge"]
domain: "computer vision"
task: "image classification"
size: "14+ million images, 1000 classes (ILSVRC)"
languages: []
license: "Non-commercial research"
url: "http://www.image-net.org"
papers: ["[[P-2501.00754_v1]]"]
created: "2025-12-27"
---

# ImageNet

## 概要
- 大規模画像分類ベンチマークの標準データセット
- WordNetの階層構造に基づく1000以上のカテゴリ
- 深層学習ブレークスルー（AlexNet, 2012）の基盤

## 統計情報
| 項目 | 値 |
|------|-----|
| 総画像数 | 14+ million |
| ILSVRCクラス数 | 1000 |
| 訓練画像 | ~1.2 million (ILSVRC) |
| 検証画像 | 50,000 (ILSVRC) |
| テスト画像 | 100,000 (ILSVRC) |

## 評価指標
- Top-1 Accuracy
- Top-5 Accuracy

## 使用論文
- [[P-2501.00754_v1]]: 猫vs犬の2クラス分類サブセットで量子ラベルエンコーディング実験

## 注意点
- 商用利用は制限あり
- データセットにはバイアス・ラベルノイズの報告あり
- 2021年以降はILSVRC大会は終了

## 入手方法
- 公式サイト: http://www.image-net.org
- 学術利用のためのアクセス申請が必要
