---
type: topic
name: "Neuron Reconstruction"
aliases: ["ニューロン再構成", "神経回路再構成", "connectomics"]
domain: ["neuroscience", "computer-vision"]
created: "2025-12-30"
---

# Neuron Reconstruction

## 概要
電子顕微鏡や光学顕微鏡ボリュームからニューロン形状・樹状突起・軸索を三次元的に再構成するタスク。細長い木構造を正しく分割・結合することが鍵。

## 主な課題
- 分割（split）と結合（merge）の抑制（連結性の保存）
- 超大規模3Dボリュームでの計算効率とメモリ効率
- 弱ラベル・不均一な画質・ノイズ耐性

## 評価指標
- ERL / Normalized ERL（連続性）
- Edge Accuracy（グラフ一致）
- Betti number error, VOI, ARI

## 代表的アプローチ
- トポロジー指向損失: [[M-supervoxel-loss]], clDice, [[M-topology-aware-loss]]
- ポストプロセス: watershed, graph-based merge/split修正

## データセット
- [[D-EXASPIM]]（光シート顕微鏡、3D）

## 関連論文
- [[P-2501.01022_v3]]: Supervoxel-based loss により連結性を保存しつつ高速学習

## 関連トピック
- [[topology-aware-learning]]
- [[instance-segmentation]]

