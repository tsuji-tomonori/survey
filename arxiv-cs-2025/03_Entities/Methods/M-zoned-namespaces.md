---
type: method
name: "Zoned Namespaces (ZNS)"
aliases: ["ZNS", "ZNS SSD", "Zoned Storage"]
category: "storage-interface"
created: "2025-12-27"
---

# Zoned Namespaces (ZNS)

## 概要
NVMe規格で定義されたホスト管理型SSDインターフェース。デバイスをゾーンに分割し、各ゾーンは追記のみ許可。ガベージコレクションの責任をホストに移譲。

## 主要な特徴
- ゾーン単位（数百MB〜GB）での追記書き込み
- ゾーン内はシーケンシャル書き込みのみ
- ゾーンリセット（全消去）によるGC
- ホストがゾーン選択・管理を担当
- デバイスオーバープロビジョニング削減

## 対応状況
- ファイルシステム: F2FS、BTRFS（限定的）
- アプリケーション固有: ZenFS（RocksDB）
- カーネル: Linux 5.9以降でサポート

## 技術的課題
- オープンゾーン数制限（典型的に14程度）
- ランダム書き込み非対応（従来ゾーンで対応）
- アプリ/FSの大幅な変更が必要

## 関連論文
- [[P-2501.00977_v2]]: ZNS向けシム層（valet-mapper）でホスト管理を実現

## 参考文献
- Bjørling et al., "ZNS: Avoiding the block interface tax for flash-based SSDs", USENIX ATC'21
