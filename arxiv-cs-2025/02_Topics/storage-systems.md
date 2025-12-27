---
type: topic
name: "Storage Systems"
aliases: ["ストレージシステム", "SSD Optimization", "Flash Storage"]
category: "systems"
created: "2025-12-27"
---

# Storage Systems

## 概要
データの永続的な保存と効率的なアクセスを実現するシステム。近年はNAND-flash SSDの特性（消去単位の大きさ、書き換え制限、ガベージコレクション）を考慮した設計が重要。

## 主要な概念
- **Write Amplification**: 実際の書き込み量/論理的な書き込み量、SSD寿命に直結
- **Garbage Collection (GC)**: 無効データを回収し空き領域を確保、性能低下の主因
- **Log-Structured Systems**: 追記のみで更新を行う設計、SSDと相性が良い
- **ZNS (Zoned Namespaces)**: ホスト管理型SSDインターフェース、ゾーン単位で追記
- **FDP (Flexible Data Placement)**: 配置ヒントベースのSSDインターフェース

## 技術的課題
- ホスト-デバイス間の配置協調（アプリ知識 vs デバイス知識）
- マルチテナント環境での性能分離
- インターフェース変遷への対応（Multi-stream→Open-channel→ZNS→FDP）
- Log-on-log問題（アプリ/FS/デバイス各層でのログ重複）

## 関連研究
- [[P-2501.00977_v2]]: シム層によるアプリ透過的なZNS/FDP活用（Valet）

## 関連トピック
- [[log-structured-systems]]
- [[cloud-storage]]
