---
type: entity
entity_type: dataset
name: "Briareo"
aliases: ["Briareo Hand Gesture Dataset"]
domain: "computer vision"
task: "gesture recognition"
size: "12 classes"
languages: []
license: "Research use"
url: ""
papers: ["[[P-2501.00935_v1]]"]
created: "2025-12-27"
---

# Briareo

## 概要
- 車内でのヒューマン・カー・インタラクション（HCI）向けハンドジェスチャーデータセット
- RGB、Depth、IR、3D関節位置を提供
- Manganaro et al. (ICIAP 2019) で公開

## 統計情報
| 項目 | 値 |
|------|-----|
| クラス数 | 12 |
| モダリティ | RGB, Depth, IR, 3D joints |

## 評価指標
- Top-1 Accuracy

## 使用論文
- [[P-2501.00935_v1]]: MsMHA-VTNで99.10%達成（Color+IR+Normals融合）

## 注意点
- NVGestureより小規模（12クラス）
- 高精度が出やすい（ベースライン手法でも90%以上）

## 参考文献
- Manganaro et al., "Hand gestures for the human-car interaction: The Briareo dataset," ICIAP 2019
