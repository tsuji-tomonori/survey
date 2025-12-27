---
type: topic
name: "Wearable Mental Health Sensing"
aliases: ["ウェアラブルメンタルヘルス", "生理センシングによるメンタルヘルス検出"]
parent_topics: ["human-computer-interaction", "ubiquitous-computing", "digital-health"]
related_topics: ["anxiety-detection", "stress-detection", "hrv-analysis"]
created: "2025-12-27"
---

# Wearable Mental Health Sensing

## Overview
ウェアラブルデバイス（スマートウォッチ、胸部センサー等）から取得した生理信号（HR, HRV, EDA等）を用いて、不安・ストレス・うつ等のメンタルヘルス状態を検出・モニタリングする研究分野。

## Key Signals
- **心拍関連**: HR（心拍数）、HRV（心拍変動）- ECG/PPGから取得
- **電気皮膚活動**: EDA（皮膚コンダクタンス）
- **行動データ**: 加速度、睡眠パターン、スマートフォン利用

## HRV Features for Anxiety
- 時間領域: RMSSD, SDNN, pNN50
- 周波数領域: HF（高周波）、LF/HF比
- 非線形: SD1, SD2, ApEn, DFAα1

## Challenges
- 日常環境でのノイズ・アーティファクト
- 個人差・文化差への対応
- 臨床診断との乖離

## Papers
- [[P-2501.01471_v2]] - インドでのSAD検出（ECG/HRV）

## Related Venues
- ACM IMWUT/UbiComp
- ACM CHI
- ACM COMPASS
