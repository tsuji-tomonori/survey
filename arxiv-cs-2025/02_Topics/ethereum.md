---
type: topic
name: "Ethereum"
name_ja: "イーサリアム"
aliases: ["ETH", "Ethereum Blockchain", "Ethereum Network"]
category: blockchain
status: active
created: "2025-12-27"
updated: "2025-12-27"
---

# Ethereum

## 概要

スマートコントラクトとDApp（分散型アプリケーション）のプラットフォームとして最も広く使用されるブロックチェーン。2015年にVitalik Buterinらにより開発。Turing完全なEVM（Ethereum Virtual Machine）上でコントラクトを実行。

## 技術的特徴

### EVM (Ethereum Virtual Machine)
- スタックベースの仮想マシン
- ガス制による計算リソース制御
- 決定論的実行の保証

### アカウントモデル
- **EOA**: 秘密鍵で制御、トランザクション発行可能
- **Contract Account**: コードで制御、トランザクション受信時に実行

### トランザクション
- **内部トレース**: コントラクト間呼び出しの履歴
- **delegatecall**: 呼び出し元コンテキストでの実行
- **Function Selector**: calldata先頭4バイトで関数特定

## データ分析基盤

### Google BigQuery
- `crypto_ethereum`データセットで全履歴分析可能
- ブロック、トランザクション、トレース、ログを格納
- 大規模分析に適した無料枠あり

### Etherscan
- ブロックエクスプローラ
- Proxy Verification機能（API制限あり）
- コントラクト検証・ソースコード公開

## 研究トピック

- スマートコントラクトのセキュリティ分析
- 設計パターンの実証研究
- DeFiプロトコルの脆弱性検出
- ガス最適化
- アップグレード可能性のガバナンス

## 関連論文

```dataview
TABLE title, year, score
FROM "01_Papers"
WHERE contains(file.tags, "#ethereum") OR contains(datasets, "ethereum")
SORT score DESC
```

## Papers
- [[P-2501.00965_v1]]: Proxyパターンの普及率・作成パターン・種別の大規模分析

## Links
- Methods: [[bigquery-analysis]], [[behavioral-analysis]]
- Related Topics: [[smart-contracts]], [[design-patterns]], [[blockchain]]
