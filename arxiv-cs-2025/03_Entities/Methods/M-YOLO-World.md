---
type: entity
entity_type: method
name: "YOLO-World"
aliases: ["YOLO World", "Open-Vocabulary YOLO"]
category: "object-detection"
papers: ["[[P-2501.00785_v3]]"]
created: "2025-12-27"
---

# YOLO-World

## 定義
- オープン語彙（Open-Vocabulary）物体検出を実現するYOLO系モデル
- テキストプロンプトで任意のクラスを指定して検出可能
- リアルタイム性を維持しつつ柔軟な物体検出を実現

## 主要コンポーネント
- Vision-Language Model: 画像とテキストの特徴空間を統合
- YOLO Backbone: リアルタイム検出のための効率的なアーキテクチャ
- Text Encoder: クラス名やプロンプトをエンコード

## 適用分野
- Human-Robot Interaction: 任意の日用品検出
- ロボティクス: 環境認識
- 汎用物体検出

## 代表的な論文
- Cheng et al., "YOLO-World: Real-Time Open-Vocabulary Object Detection", CVPR 2024
- [[P-2501.00785_v3]]: HRIシステムでの日用品検出に使用

## 派生・改良
- Fine-tuningによる特定ドメイン（医療機器等）への適応

## 関連手法
- [[YOLO]]: ベースとなる検出アーキテクチャ
- [[CLIP]]: Vision-Languageモデルの先駆け
- [[Grounding-DINO]]: 別のオープン語彙検出手法

## 実装リソース
- 公式実装: https://github.com/AILab-CVC/YOLO-World
