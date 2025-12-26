---
type: entity
entity_type: dataset
name: "SynthEVox3D"
aliases: ["Synthetic Event Camera Voxel 3D Reconstruction Dataset", "SynthEVox3D-Tiny"]
domain: "3D reconstruction"
task: "voxel-based 3D reconstruction"
size: "39,739 samples (Full) / 1,040 samples (Tiny)"
languages: []
license: ""
url: ""
papers: ["[[P-2501.00741_v4]]"]
created: "2025-12-26"
---

# SynthEVox3D

## 概要
- イベントカメラデータからのボクセル3D再構成用合成データセット
- ShapeNetの3Dモデルからイベントストリームを生成
- 唯一のボクセルラベル付きイベントベース3D再構成データセット

## 統計情報
| 項目 | 値 |
|------|-----|
| サイズ | 39,739 samples (Full) / 1,040 samples (Tiny) |
| カテゴリ数 | 13 |
| 解像度 | 512×512 pixels |
| 時間長 | 0.5秒/サンプル |
| ボクセル解像度 | 32×32×32 |

## カテゴリ
Airplane, Bench, Cabinet, Car, Chair, Displayer, Lamp, Speaker, Rifle, Sofa, Table, Telephone, Watercraft

## データ形式
- 入力: イベントストリーム（座標、タイムスタンプ、極性）
- ラベル: 32×32×32ボクセルグリッド
- 生成方法: 全角度スキャン（0.5秒）

## 評価指標
- mIoU (Mean Intersection over Union)
- F-Score

## 使用論文
- [[P-2501.00741_v4]]: E2Vベースライン、Sobel Event Frame提案手法

## 注意点
- 合成データのみ（実環境イベントカメラデータなし）
- ShapeNet由来のため実世界物体との差異あり

## 入手方法
- Chen et al., 2023 (E2V論文) で提案
- 公開状況: 要確認
