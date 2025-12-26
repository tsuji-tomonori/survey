---
type: entity
entity_type: method
name: "Sobel Event Frame"
aliases: ["Sobel EvtFrm", "SEF"]
category: "event-representation"
papers: ["[[P-2501.00741_v4]]"]
created: "2025-12-26"
---

# Sobel Event Frame

## 定義
- Event Frame（イベントストリームをフレーム化した表現）にSobelフィルタを適用し、エッジ特徴を強調するイベント表現手法
- 畳み込み式: O(x,y,t) = Σ E(x+w, y+h, t) · S(w,h)
- 勾配強度を[0,255]に正規化して可視化・入力

## 主要コンポーネント
- Event Frame: イベントストリームを固定時間窓でフレーム化（5つのモード: Pos/Neg/Last/Any/Sep）
- Sobel Operator: 3×3カーネルでx/y方向の勾配を計算
- 正規化: 勾配強度をグレースケール範囲に変換

## 適用分野
- イベントカメラベース3D再構成
- 潜在的応用: オブジェクト認識、追跡、動作認識

## 代表的な論文
- [[P-2501.00741_v4]]: Sobel Event Frameを提案、E2Vに対して31.6%改善

## 派生・改良
- 他のエッジ検出フィルタ（Canny, Laplacian等）への拡張可能性

## 関連手法
- [[event-frame]]: ベースとなるイベント表現
- [[sobel-filter]]: 画像処理における古典的エッジ検出
- [[efficient-channel-attention]]: 本手法と組み合わせて使用

## 実装リソース
- コード公開状況: 不明（論文時点）
