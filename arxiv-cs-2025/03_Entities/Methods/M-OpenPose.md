---
type: entity
entity_type: method
name: "OpenPose"
aliases: ["Open Pose", "CMU OpenPose"]
category: "pose-estimation"
papers: ["[[P-2501.00785_v3]]"]
created: "2025-12-27"
---

# OpenPose

## 定義
- リアルタイムマルチパーソン2D姿勢推定手法
- Part Affinity Fields (PAFs) を用いて複数人の関節を同時検出・接続
- Cao et al., CVPR 2017で提案

## 主要コンポーネント
- Multi-stage CNN: 関節ヒートマップとPAFsを段階的に推定
- Part Affinity Fields: 関節間の接続関係を表現するベクトル場
- Bipartite Matching: 検出された関節を人物ごとにグルーピング

## 適用分野
- Human-Robot Interaction: 指差し姿勢検出、ジェスチャー認識
- 動作認識
- スポーツ分析
- AR/VR

## 代表的な論文
- Cao et al., "Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields", CVPR 2017
- [[P-2501.00785_v3]]: HRIでの指差し姿勢検出に使用（深度情報と組み合わせて3D化）

## 派生・改良
- OpenPose 1.7: 手・顔のキーポイント追加
- MediaPipe Pose: 軽量版
- HRNet系: 精度向上版

## 関連手法
- [[PoseNet]]: 単一人物姿勢推定
- [[MediaPipe]]: 軽量リアルタイム推定
- [[HRNet]]: 高解像度特徴維持

## 実装リソース
- 公式実装: https://github.com/CMU-Perceptual-Computing-Lab/openpose
