---
type: topic
name: "Design Patterns"
name_ja: "設計パターン"
aliases: ["Software Design Patterns", "Architectural Patterns", "GoF Patterns"]
category: software-engineering
status: active
created: "2025-12-27"
updated: "2025-12-27"
---

# Design Patterns

## 概要

ソフトウェア設計における再利用可能な解決策のカタログ。GoF（Gang of Four）パターンを起源とし、様々なドメイン（Web、モバイル、ブロックチェーン等）で特化パターンが発展。

## 分類

### 生成パターン (Creational)
- **Factory**: オブジェクト生成の抽象化
- **Singleton**: 単一インスタンスの保証
- **Builder**: 複雑なオブジェクトの段階的構築

### 構造パターン (Structural)
- **Proxy**: 代理オブジェクトによるアクセス制御
- **Adapter**: インターフェース変換
- **Decorator**: 動的な機能追加
- **Facade**: サブシステムの統一インターフェース

### 振る舞いパターン (Behavioral)
- **Observer**: 状態変更の通知
- **Strategy**: アルゴリズムの差し替え
- **Command**: 操作のオブジェクト化

## ブロックチェーン特有パターン

### Proxyパターン
スマートコントラクトにおける2つの主要用途:
1. **Forwarder**: 呼び出し転送によるガス節約（例: ERC-1167）
2. **Upgradeability**: ロジック更新可能性の実現（例: ERC-1822, ERC-1967）

### 作成パターン
- **On-chain**: Factory経由でのコントラクト生成（99.3%）
- **Off-chain**: EOAからの直接デプロイ（0.7%）

## 実証研究

- Proxyパターンの普及率: Ethereumコントラクトの14.2%
- ERC-1167（Minimal Proxy）が最多（29.4%）
- 透明性問題: 97%のDAppがlogicアドレス非公開

## 関連論文

```dataview
TABLE title, year, score
FROM "01_Papers"
WHERE contains(file.tags, "#design-patterns") OR contains(methods, "pattern-mining")
SORT score DESC
```

## Papers
- [[P-2501.00965_v1]]: Ethereum Proxyパターンの12種作成パターン・種別分類

## Links
- Methods: [[pattern-mining]], [[behavioral-analysis]]
- Related Topics: [[smart-contracts]], [[software-maintenance]], [[software-architecture]]
