---
type: topic
topic: "Human-Robot Interaction"
aliases: ["HRI", "human-robot interface", "ヒューマンロボットインタラクション", "人間ロボット協調"]
scope: "application"
keywords: ["interaction", "intent recognition", "gesture", "voice command", "multimodal"]
parent_topic: ""
child_topics: ["gesture-based-hri", "voice-based-hri", "multimodal-hri"]
papers: ["[[P-2501.00785_v3]]"]
created: "2025-12-27"
---

# Human-Robot Interaction

## 定義
- 人間とロボット間のコミュニケーション・協調に関する研究分野
- 人間の意図をロボットが理解し、適切なアクションを実行する
- 入力モダリティ: 音声、ジェスチャー、視線、姿勢、脳波など

## なぜ重要か
- 高齢化社会でのサービスロボット需要増加
- 非専門家がロボットを直感的に操作できる必要性
- 人間とロボットの安全な協働作業の実現

## 主要な問題設定
- 意図認識（Intent Recognition）: 人間の意図をセンサー入力から推定
- アクション生成: 意図からロボット制御コマンドへの変換
- 曖昧性解消: 不完全な入力からの意図推定
- 安全性: 人間への危害回避

## 代表的な手法
- ジェスチャーベース: Leap Motion、Kinect等で手・体の動きを認識
- 音声ベース: 音声認識＋NLPでコマンド解釈
- VLMベース: 視覚言語モデルで環境理解＋対話
- マルチモーダル融合: 複数モダリティを統合

## 標準的なベンチマーク
- 独自タスク設計が多い（pick-and-place、pour等の操作タスク）
- ユーザースタディ（インタラクション時間、成功率、主観評価）

## 研究の流れ
### 黎明期
- ルールベースのコマンド解釈
- 単一モダリティ（ジェスチャーまたは音声）

### 発展期
- 深層学習による認識精度向上
- マルチモーダル統合の試み

### 現在のトレンド
- LLM/VLMによる高度な意図理解・アクション生成
- ゼロショット・少数ショット対応
- 高齢者・障害者向けアクセシビリティ

## オープンな課題
- LLMのハルシネーション対策
- 多言語・多文化対応
- 極端環境（低照度、騒音）でのロバスト性
- 医療・介護現場での臨床検証

## 関連論文
- [[P-2501.00785_v3]]: NMM-HRI（音声＋指差し姿勢＋LLM）

## 関連トピック
- [[multimodal-learning]]
- [[LLM-for-robotics]]
- [[gesture-recognition]]
