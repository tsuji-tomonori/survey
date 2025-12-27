---
type: method
name: "Shim Layer"
aliases: ["シム層", "Interposition Layer", "LD_PRELOAD"]
category: "systems"
created: "2025-12-27"
---

# Shim Layer

## 概要
アプリケーションとOSの間に挿入される軽量な中間層。libcコールをインターセプトし、透過的に機能を追加・変更する。

## 主要な実装手法
- **LD_PRELOAD**: 動的リンク時にライブラリを先読み、最小オーバーヘッド（~2μs/syscall）
- **eBPF**: カーネル内でのフック、高機能だが~10倍のオーバーヘッド
- **FUSE**: ユーザ空間ファイルシステム、~1.8倍のオーバーヘッド
- **WASM (WASI)**: WebAssemblyシステムインターフェース、~2.5倍のオーバーヘッド

## 利点
- アプリケーション変更不要
- カーネル変更不要
- 実行時に動的に適用可能
- モジュール化・交換が容易

## 制限事項
- 静的リンクアプリには適用不可（LD_PRELOAD）
- libc非使用言語（Go、Java）には適用困難
- mmap等の直接メモリマップは追跡困難

## 関連論文
- [[P-2501.00977_v2]]: SSDデータ配置最適化のためのシム層（Valet）

## 参考文献
- syscall_intercept: https://github.com/pmem/syscall_intercept
- zIO (OSDI'22): Zero-Copy IOのためのLD_PRELOAD活用
