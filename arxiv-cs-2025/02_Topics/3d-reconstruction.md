---
type: topic
topic: "3D Reconstruction"
aliases: ["3D再構成", "three-dimensional reconstruction"]
scope: "task"
keywords: ["depth estimation", "voxel", "mesh", "point cloud", "multi-view stereo"]
parent_topic: ""
child_topics: ["event-based-3d-reconstruction", "neural-radiance-fields"]
papers: ["[[P-2501.00741_v4]]"]
created: "2025-12-26"
---

# 3D Reconstruction

## 定義
- 2D画像やセンサーデータから3D形状・シーンを復元するタスク
- 出力形式: ボクセル、メッシュ、点群、NeRF等

## なぜ重要か
- VR/AR、ロボティクス、自動運転での空間理解に不可欠
- デジタルツイン、3Dコンテンツ生成の基盤技術

## 主要な問題設定
- 単眼 vs ステレオ vs マルチビュー
- 密 vs 疎再構成
- 静的シーン vs 動的シーン
- センサー種類: RGB, RGB-D, LiDAR, Event Camera

## 代表的な手法
- 従来手法: Structure-from-Motion (SfM), Multi-View Stereo (MVS)
- 深層学習: 3D-R2N2, Pix2Vox++, EVolT
- NeRF系: Neural Radiance Fields
- イベントベース: E2V, [[M-sobel-event-frame]]

## 標準的なベンチマーク
- ShapeNet: 3Dモデルデータベース
- [[D-SynthEVox3D]]: イベントベースボクセル再構成

## 研究の流れ
### 黎明期
- 幾何学的手法（SfM, MVS）

### 発展期
- CNNベースのボクセル/点群予測
- Encoder-Decoder構造の確立

### 現在のトレンド
- NeRF/3DGSによる暗黙的表現
- イベントカメラ等の新センサー活用
- 大規模事前学習モデルの活用

## オープンな課題
- リアルタイム処理
- 極端環境（高速動作、低照度）での堅牢性
- 未知物体への汎化

## 関連論文
- [[P-2501.00741_v4]]: イベントカメラからのEnd-to-End 3D再構成

## 関連トピック
- [[event-camera]]
- [[neural-radiance-fields]]
- [[depth-estimation]]
