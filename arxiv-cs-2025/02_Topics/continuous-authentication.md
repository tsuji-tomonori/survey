---
type: topic
name: "Continuous Authentication"
aliases: ["連続認証", "継続認証"]
domain: ["security", "biometrics"]
created: "2025-12-30"
---

# Continuous Authentication

## 概要
ログイン後もユーザーの正当性を継続的に監視し、なりすましを早期検出する認証方式。デバイス常時利用やハンズフリー環境に適合。

## センサー/シグナル
- 行動（キーストローク、マウス）、生体（顔、声、唇）、生理（心拍）、コンテキスト（位置、端末）。

## 評価
- EER/FAR/FRR、ROC/DET、Time-to-detect、レイテンシ/電力。

## 実運用の論点
- しきい値適応、ドリフト/テンプレートエイジング、オンデバイス処理とプライバシー。

## 関連論文
- [[P-2501.01032_v1]]: 唇の調音ダイナミクスに基づく形状非依存の連続認証。

## 関連トピック
- [[lip-biometrics]]

