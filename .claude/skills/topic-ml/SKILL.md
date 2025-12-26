---
name: topic-ml
description: ML全般の重要概念・キーワード辞書。メモへのリンクとファクトチェック状態を管理
---

# ML全般トピック・キーワード辞書

機械学習全般の重要な概念・キーワードを蓄積します。

## キーワード辞書

### 最適化

#### adam
- 定義: 適応的学習率を持つ確率的勾配降下法の一種
- 関連メモ: [[adam]]
- 初出論文: -
- ファクトチェック: 未確認

#### gradient-descent
- 定義: 損失関数の勾配方向にパラメータを更新する最適化手法
- 関連メモ: [[gradient-descent]]
- 初出論文: -
- ファクトチェック: 未確認

#### learning-rate-schedule
- 定義: 学習率を訓練中に変化させる戦略
- 関連メモ: [[learning-rate-schedule]]
- 初出論文: -
- ファクトチェック: 未確認

### 正則化

#### dropout
- 定義: 学習時にランダムにユニットを無効化する正則化手法
- 関連メモ: [[dropout]]
- 初出論文: -
- ファクトチェック: 未確認

#### batch-normalization
- 定義: ミニバッチ内で活性化を正規化する手法
- 関連メモ: [[batch-normalization]]
- 初出論文: -
- ファクトチェック: 未確認

#### weight-decay
- 定義: パラメータのL2ノルムにペナルティを課す正則化
- 関連メモ: [[weight-decay]]
- 初出論文: -
- ファクトチェック: 未確認

### 分散学習

#### federated-learning
- 定義: データを集約せずに分散したデバイス上で学習を行う手法
- 関連メモ: [[federated-learning]]
- 初出論文: FedAvg (McMahan et al., 2017)
- ファクトチェック: 確認済み（2025-12-26）

#### gradient-sparsification
- 定義: 勾配の上位γ%の要素のみを送信することで通信量を削減する手法
- 関連メモ: [[gradient-sparsification]]
- 初出論文: Deep Gradient Compression (Lin et al., 2017)
- ファクトチェック: 確認済み（2025-12-26）
- 参照論文: [[P-2501.00732_v1]]

#### error-feedback
- 定義: 勾配圧縮でフィルタリングされた情報を蓄積し、次ラウンドで補償する技術
- 関連メモ: [[error-feedback]]
- 初出論文: EF21 (Richtárik et al., 2021)
- ファクトチェック: 確認済み（2025-12-26）
- 参照論文: [[P-2501.00732_v1]]

#### gradient-tracking
- 定義: ローカル勾配方向とグローバル勾配方向の差分を追跡する技術
- 関連メモ: [[gradient-tracking]]
- 初出論文: -
- ファクトチェック: 未確認
- 参照論文: [[P-2501.00732_v1]]

#### personalized-aggregation
- 定義: クライアント間の類似性（勾配相関等）に基づいて集約重みを決定する手法
- 関連メモ: [[personalized-aggregation]]
- 初出論文: -
- ファクトチェック: 未確認
- 参照論文: [[P-2501.00732_v1]]（k-relevant, δ-threshold, all-correlated）

#### data-parallel
- 定義: データを分割して複数デバイスで並列に学習する手法
- 関連メモ: [[data-parallel]]
- 初出論文: -
- ファクトチェック: 未確認

#### model-parallel
- 定義: モデルを分割して複数デバイスに配置する並列化手法
- 関連メモ: [[model-parallel]]
- 初出論文: -
- ファクトチェック: 未確認

### 評価

#### cross-validation
- 定義: データを分割して複数回評価を行い、汎化性能を推定する手法
- 関連メモ: [[cross-validation]]
- 初出論文: -
- ファクトチェック: 未確認

#### overfitting
- 定義: 訓練データに過適合し、未知データへの汎化性能が低下する現象
- 関連メモ: [[overfitting]]
- 初出論文: -
- ファクトチェック: 未確認

---

## 関連fix Skill
- [[fix-ml/SKILL.md]]
