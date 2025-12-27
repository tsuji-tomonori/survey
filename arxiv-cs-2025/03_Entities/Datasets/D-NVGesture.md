---
type: entity
entity_type: dataset
name: "NVGesture"
aliases: ["NVidia Dynamic Hand Gesture Dataset"]
domain: "computer vision"
task: "gesture recognition"
size: "25 classes, 1532 videos"
languages: []
license: "Research use"
url: "https://research.nvidia.com/publication/2016-06_online-detection-and-classification-dynamic-hand-gestures-recurrent-3d"
papers: ["[[P-2501.00935_v1]]"]
created: "2025-12-27"
---

# NVGesture

## 概要
- NVIDIAが公開した運転シナリオにおける動的ハンドジェスチャー認識データセット
- RGB、Depth、IRの3モダリティを提供
- 車内での非接触操作を想定

## 統計情報
| 項目 | 値 |
|------|-----|
| クラス数 | 25 |
| 総動画数 | 1532 |
| 被験者数 | 20 |
| モダリティ | RGB, Depth, IR |

## 評価指標
- Top-1 Accuracy

## 使用論文
- [[P-2501.00935_v1]]: MsMHA-VTNで88.22%達成（5モダリティ融合）

## 注意点
- Human baseline: 88.40%（Color modality）
- 運転シナリオ特化のため、一般的なジェスチャー認識への汎化は要検証

## 入手方法
- NVIDIA Research公式サイトからダウンロード申請
