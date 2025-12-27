---
type: entity
entity_type: dataset
name: "Ethereum BigQuery Dataset"
aliases: ["crypto_ethereum", "Google BigQuery Ethereum", "Ethereum Public Dataset"]
domain: "blockchain"
task: "blockchain analysis"
size: "50M+ contracts, 1.6B+ transactions (as of Sept 2022)"
languages: []
license: "Public (Google BigQuery free tier)"
url: "https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=crypto_ethereum"
papers: ["[[P-2501.00965_v1]]"]
created: "2025-12-27"
---

# Ethereum BigQuery Dataset

## 概要
- Google BigQueryで公開されているEthereumブロックチェーンの全履歴データセット
- 2015年8月（Ethereumメインネット開始）から継続的に更新
- 大規模なブロックチェーン分析に無料枠で利用可能

## 統計情報（2022年9月時点）
| 項目 | 値 |
|------|-----|
| スマートコントラクト数 | 50,845,833 |
| トランザクション数 | 1,695,517,186 |
| 内部トレース数 | 5,503,071,306 |
| 期間 | 2015年8月〜継続更新 |

## テーブル構成
- `blocks`: ブロック情報
- `transactions`: トランザクション詳細
- `traces`: 内部トランザクショントレース
- `contracts`: コントラクトメタデータ
- `logs`: イベントログ
- `token_transfers`: トークン転送履歴

## 分析用途

### Proxy検出
- `traces`テーブルからdelegatecallトレースを抽出
- Function Selector（calldata先頭4バイト）による照合
- 行動ベース検出が15分以内に完了

### 使用コンテキスト特定
- deployer address + bytecode + logic contractでクラスタリング
- 連結成分により使用コンテキストを特定

## アクセス方法
1. Google Cloud Consoleにアクセス
2. BigQuery → 「bigquery-public-data」プロジェクト
3. 「crypto_ethereum」データセットを選択
4. 無料枠: 月1TBクエリまで

## 注意点
- リアルタイムデータではない（遅延あり）
- 大規模クエリはコストに注意
- データの信頼性は十分だが、Ethereumノードからの直接取得も可能

## 使用論文
- [[P-2501.00965_v1]]: 50M+コントラクト・16億トランザクションを分析しProxyパターンを調査
