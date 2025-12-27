---
type: dataset
name: "EXASPIM"
full_name: "Expansion-Assisted Selective Plane Illumination Microscopy Dataset"
domain: ["neuroscience", "medical-imaging"]
modality: "3D light sheet microscopy"
task: ["instance-segmentation", "neuron-reconstruction"]
size: "37 images"
public: true
url: "s3://aind-msma-morphology-data/EXASPIM25"
created: "2025-12-27"
---

# EXASPIM Dataset

## 概要
Allen Institute が公開した 3D 光シート顕微鏡によるマウス脳画像データセット。ニューロン再構成・インスタンスセグメンテーション評価用。

## 仕様
- **画像数**: 37枚（学習）+ 4枚（テスト）
- **解像度**: 256×256×256 〜 1024×1024×1024
- **ボクセルサイズ**: 約 1 µm³
- **アノテーション**: インスタンスセグメンテーション + スケルトン

## 特徴
- 疎な（sparse）ニューロン画像
- 3D での骨格ベースメトリクス評価に適合
- EXASPIM 技術（expansion microscopy + selective plane illumination）で取得

## 評価指標
- Dice, ARI, VOI, Betti number error
- Splits/Neuron, Edge Accuracy, Normalized ERL（骨格ベース）

## アクセス
- S3: `s3://aind-msma-morphology-data/EXASPIM25`

## 関連論文
- [[P-2501.01022_v3]]: 提案・使用（AAAI 2025）
- Glaser et al. 2024: EXASPIM 技術論文
