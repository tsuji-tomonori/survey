---
type: topic
topic: "Event Camera"
aliases: ["neuromorphic camera", "dynamic vision sensor", "DVS", "イベントカメラ", "ニューロモーフィックカメラ"]
scope: "sensor"
keywords: ["event-based vision", "asynchronous sensing", "brightness change", "neuromorphic"]
parent_topic: ""
child_topics: ["event-representation", "event-based-3d-reconstruction"]
papers: ["[[P-2501.00741_v4]]"]
created: "2025-12-26"
---

# Event Camera

## 定義
- 輝度変化に非同期で応答するバイオインスパイアドセンサー
- 各ピクセルが独立・非同期に動作し、閾値を超える輝度変化時にのみイベントを生成
- 出力: イベントストリーム（座標、タイムスタンプ、極性）

## なぜ重要か
- 高速動作でもモーションブラーなし（マイクロ秒単位の時間分解能）
- 高ダイナミックレンジ（120dB以上）
- 低消費電力
- 極端環境（高速動作、低照度、高輝度）での3D再構成・認識に有利

## 主要な問題設定
- イベント表現: 非同期イベントストリームをどう処理するか
- 深度推定・3D再構成: 単眼/ステレオからの空間情報復元
- オプティカルフロー: イベントからの動き推定
- オブジェクト認識・追跡

## 代表的な手法
- Event Frame系: イベントをフレーム化して処理
- [[M-sobel-event-frame]]: エッジ強調イベント表現
- E2VID: イベントから強度画像を再構成
- EVO, EMVS: 物理ベース3D再構成

## 標準的なベンチマーク
- [[D-SynthEVox3D]]: ボクセル3D再構成
- MVSEC, DSEC: 実環境イベントデータ

## 研究の流れ
### 黎明期
- DVS (Dynamic Vision Sensor) の開発
- 物理・幾何ベースの処理手法

### 発展期
- 深層学習の導入（E2VID, イベントベース認識）
- イベント表現の多様化

### 現在のトレンド
- End-to-End学習による物理的事前知識の排除
- マルチモーダル融合（RGB + Event）
- 実環境への応用拡大

## オープンな課題
- 実環境データセットの不足
- 極端条件での定量評価
- 計算効率の向上

## 関連論文
- [[P-2501.00741_v4]]: End-to-End 3D再構成

## 関連トピック
- [[3d-reconstruction]]
- [[neuromorphic-computing]]
