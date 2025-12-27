---
type: method
name: "Behavioral Analysis"
aliases: ["Behavior-based Detection", "Runtime Analysis", "Dynamic Analysis"]
category: "software-analysis"
created: "2025-12-27"
---

# Behavioral Analysis

## 概要
システムの静的構造ではなく、実行時の振る舞い（トレース、呼び出しパターン、状態遷移）を分析する手法。スマートコントラクト分析ではトランザクショントレースに基づくパターン検出に使用。

## 主要な特徴
- 実行時データ（トレース、ログ）に基づく分析
- 静的解析では検出困難なパターンを発見可能
- 「アクティブ」な対象のみ検出可能（実行履歴が必要）

## 適用例

### スマートコントラクトProxy検出
1. delegatecallトレースを抽出
2. 呼び出し元コントラクトを候補Proxyとして特定
3. Function Selector（calldata先頭4バイト）の一致でProxy確定
4. 検出性能: アクティブProxyで100% Precision/Recall

### 利点と制約
| 利点 | 制約 |
|------|------|
| 高精度検出 | 非アクティブ対象は検出不可 |
| スケーラブル（BigQuery等で効率化） | 実行データ収集が前提 |
| パターンの自動発見 | 過去データへの依存 |

## 関連手法
- **Static Analysis**: ソースコード・バイトコードの構造分析
- **Pattern Mining**: 繰り返しパターンの抽出
- **Trace Analysis**: 実行トレースの詳細分析

## 関連論文
- [[P-2501.00965_v1]]: Ethereumトランザクショントレースに基づくProxy検出
