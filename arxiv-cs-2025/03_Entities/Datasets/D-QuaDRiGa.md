---
type: entity
entity_type: dataset
name: "QuaDRiGa"
aliases: ["Quadriga", "QuaDRiGa-synthetic"]
domain: "wireless networks"
task: "wireless channel modeling / RAN simulation"
size: "synthetic, simulator-generated channels"
languages: []
license: "varies (research use)"
url: "https://quadriga-channel-model.de/"
papers: ["[[P-2501.00950_v1]]"]
created: "2025-12-30"
---

# QuaDRiGa

## 概要
幾何学ベースの無線チャネル生成ツール。3GPP 38.901等の標準モデルに準拠した屋外/屋内のLOS/NLOSシナリオを合成し、RANの評価・シミュレーションに用いられる。

## 用途
- 無線スケジューリングやRRMのアルゴリズム評価
- 5G/6GシナリオにおけるSNR・スペクトル効率の解析

## 使用論文
- [[P-2501.00950_v1]]: RANスライシング向けインテント駆動スケジューラの評価で合成チャネルを生成

## 注意点
- シミュレーション依存のため、実機・実環境との差異には留意
- モデル・パラメータの妥当性により結果が変動

