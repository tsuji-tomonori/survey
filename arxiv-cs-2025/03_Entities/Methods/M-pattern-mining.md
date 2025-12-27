---
type: method
name: "Pattern Mining"
aliases: ["Frequent Pattern Mining", "Sequential Pattern Mining", "Design Pattern Detection"]
category: "data-mining"
created: "2025-12-27"
---

# Pattern Mining

## 概要
大規模データから繰り返し出現するパターン（頻出アイテムセット、シーケンス、構造）を抽出するデータマイニング手法。ソフトウェア工学では設計パターン検出、コード重複検出、異常検出に応用。

## 主要な特徴
- 大規模データからのパターン自動発見
- 頻度・サポートに基づくフィルタリング
- 階層的・逐次的パターンの抽出

## 手法分類

### 頻出パターンマイニング
- **Apriori**: アイテムセットの頻度に基づく
- **FP-Growth**: 接頭辞木による効率化
- **ECLAT**: 垂直データ形式

### シーケンスパターンマイニング
- **GSP**: 汎化シーケンスパターン
- **PrefixSpan**: 接頭辞投影
- **SPADE**: 垂直形式シーケンス

## ソフトウェア工学への応用

### スマートコントラクト作成パターン
- コントラクト作成トレースから作成パターンを抽出
- 12種の作成パターンを特定（On-chain 11種、Off-chain 1種）
- パターン: EOA > Factory > Proxy（最多: 91.39%）

### 設計パターン検出
- バイトコード・ソースコードからのパターン認識
- 参照実装との比較（ERC-1167, ERC-1822等）

## 関連手法
- **Behavioral Analysis**: 実行時振る舞い分析
- **Clustering**: 類似オブジェクトのグループ化
- **Anomaly Detection**: 逸脱パターンの検出

## 関連論文
- [[P-2501.00965_v1]]: Ethereumコントラクト作成パターンの体系的分類
