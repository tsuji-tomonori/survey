---
type: topic
name: "Software Maintenance"
name_ja: "ソフトウェア保守"
aliases: ["Software Evolution", "Code Maintenance", "System Maintenance"]
category: software-engineering
status: active
created: "2025-12-27"
updated: "2025-12-27"
---

# Software Maintenance

## 概要

デプロイ後のソフトウェアの修正・更新・最適化を扱う分野。バグ修正、機能追加、パフォーマンス改善、環境適応を含む。スマートコントラクトでは「不変性」との両立が課題。

## 保守の分類

### Lientz & Swansonの分類
- **Corrective**: バグ修正
- **Adaptive**: 環境変化への適応
- **Perfective**: 機能強化・改善
- **Preventive**: 将来の問題予防

### ブロックチェーンにおける課題
- **不変性**: デプロイ済みコードは変更不可
- **Proxyパターン**: アップグレード可能性の実現手段
- **ガバナンス**: 誰がアップグレード権限を持つか

## アップグレードパターン

### Upgradeability Proxy
- ストレージとロジックの分離
- delegatecallによる実行委譲
- ERC-1822 (UUPS), ERC-1967標準

### Forwarder Proxy
- 呼び出し転送のみ（ロジック固定）
- ガス節約目的
- ERC-1167 (Minimal Proxy)

## 研究課題

- 透明性: logicコントラクトアドレスの公開率（わずか2.9%）
- 監査困難性: 非公開ロジックの検証
- ガバナンスリスク: 中央集権的アップグレード権限

## 関連論文

```dataview
TABLE title, year, score
FROM "01_Papers"
WHERE contains(file.tags, "#software-maintenance") OR contains(tasks, "software-evolution")
SORT score DESC
```

## Papers
- [[P-2501.00965_v1]]: Proxyパターンによるアップグレード可能性の実態調査

## Links
- Methods: [[empirical-study]], [[behavioral-analysis]]
- Related Topics: [[smart-contracts]], [[design-patterns]], [[software-engineering]]
