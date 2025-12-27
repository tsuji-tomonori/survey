---
type: topic
name: "Smart Contracts"
name_ja: "スマートコントラクト"
aliases: ["Solidity Contracts", "Blockchain Contracts", "DApp Contracts"]
category: blockchain
status: active
created: "2025-12-27"
updated: "2025-12-27"
---

# Smart Contracts

## 概要

ブロックチェーン上で実行される自己実行型プログラム。条件が満たされると自動的に契約条項を履行し、中央管理者なしで信頼性のある取引を実現する。Ethereumが最も普及したプラットフォーム。

## 主要概念

### 基本構造
- **EOA (Externally Owned Account)**: 秘密鍵で制御されるユーザーアカウント
- **Contract Account**: コードで制御されるコントラクト
- **Bytecode**: EVMで実行されるコンパイル済みコード
- **ABI (Application Binary Interface)**: コントラクトの外部インターフェース定義

### 設計パターン
- **Proxy Pattern**: アップグレード可能性・ガス節約のための委譲パターン
  - Forwarder Proxy: 呼び出し転送のみ
  - Upgradeability Proxy: ロジック更新可能
- **Factory Pattern**: コントラクトを動的に生成
- **Ownable Pattern**: アクセス制御

### 呼び出し機構
- **call**: 外部コントラクト呼び出し
- **delegatecall**: 呼び出し元のコンテキストで実行（Proxyの基盤）
- **staticcall**: 状態変更不可の読み取り専用呼び出し

## 主要標準（ERC）

| 標準 | 目的 |
|------|------|
| ERC-20 | Fungible Token |
| ERC-721 | Non-Fungible Token (NFT) |
| ERC-1167 | Minimal Proxy (Clone) |
| ERC-1822 | Universal Upgradeable Proxy Standard (UUPS) |
| ERC-1967 | Standard Proxy Storage Slots |

## セキュリティ考慮事項

- **再入攻撃 (Reentrancy)**: 外部呼び出し後の状態更新漏れ
- **整数オーバーフロー**: Solidity 0.8以前で注意
- **アクセス制御不備**: 関数の可視性設定ミス
- **Proxyの透明性問題**: ロジックコントラクトのアドレス非公開

## 関連論文

```dataview
TABLE title, year, score
FROM "01_Papers"
WHERE contains(file.tags, "#smart-contracts") OR contains(tasks, "smart-contracts")
SORT score DESC
```

## Papers
- [[P-2501.00965_v1]]: Ethereumにおけるプロキシパターンの大規模実証研究

## Links
- Methods: [[behavioral-analysis]], [[pattern-mining]], [[static-analysis]]
- Related Topics: [[ethereum]], [[design-patterns]], [[software-maintenance]]
