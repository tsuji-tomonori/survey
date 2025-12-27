---
type: dataset
name: "SAD-HRV-India"
aliases: ["Social Anxiety HRV Dataset India"]
domain: ["mental-health", "physiological-sensing", "hci"]
modality: ["ecg", "survey"]
size: "51 participants (99 recruited, 48 excluded due to noise)"
availability: "public"
url: "https://osf.io/phze7/"
created: "2025-12-27"
---

# SAD-HRV-India Dataset

## Overview
インドIISER Bhopalで収集された社会不安障害（SAD）研究用のECG・HRVデータセット。スピーチタスクによる不安誘発実験の4フェーズ（ベースライン・予期・活動・反省）データを含む。Global South（LMIC）における初のSAD-HRV公開データセット。

## Data Description
- **参加者**: 51人（SAD 31人、non-SAD 20人）
- **センサー**: Shimmer ECG（臨床グレード、1024Hz）
- **フェーズ**: Baseline (2分) → Anticipation (45秒) → Speech (2.5分) → Reflection (45秒)
- **アノテーション**: SPINスコア、PAL（知覚不安レベル）、人口統計情報

## Key Features
- 時間領域HRV: MeanNN, SDNN, RMSSD, MedianNN, Prc20NN, pNN20, HTI, TINN
- 周波数領域HRV: HF, HFn, LnHF
- 非線形HRV: S, SD1, SD2, SD1SD2, DFAα1, ApEn
- HR（心拍数）

## Papers
- [[P-2501.01471_v2]] - 原著論文

## Notes
- 48/99人がノイズ・アーティファクトでデータ除外（主に活動フェーズ）
- 非臨床サンプル（大学生）、SPINスコア閾値20でSAD/non-SAD分類
