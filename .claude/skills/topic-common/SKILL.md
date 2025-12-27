---
name: topic-common
description: 分野横断的な重要概念・キーワードの辞書。メモへのリンクとファクトチェック状態を管理
---

# 共通トピック・キーワード辞書

分野横断的に重要な概念・キーワードを蓄積し、対応するメモへのリンクを管理します。

## 使用方法

1. `/check` 実行時に新しいキーワードを発見したら追記
2. 対応するトピックメモを作成/更新
3. ファクトチェック状態を記録

## キーワード辞書

### 学習パラダイム

#### self-supervised-learning
- 定義: ラベルなしデータから自己生成した疑似ラベルで学習する手法
- 関連メモ: [[self-supervised-learning]]
- 初出論文: -
- ファクトチェック: 未確認

#### contrastive-learning
- 定義: 類似サンプルを近づけ、異なるサンプルを遠ざける学習
- 関連メモ: [[contrastive-learning]]
- 初出論文: -
- ファクトチェック: 未確認

#### transfer-learning
- 定義: あるタスクで学習した知識を別タスクに転用する手法
- 関連メモ: [[transfer-learning]]
- 初出論文: -
- ファクトチェック: 未確認

### 効率化手法

#### knowledge-distillation
- 定義: 大きなモデル（教師）の知識を小さなモデル（生徒）に転移
- 関連メモ: [[knowledge-distillation]]
- 初出論文: -
- ファクトチェック: 未確認

#### pruning
- 定義: モデルの不要なパラメータを削除して効率化
- 関連メモ: [[pruning]]
- 初出論文: -
- ファクトチェック: 未確認

#### quantization
- 定義: パラメータの精度を下げて計算効率化（FP32→INT8等）
- 関連メモ: [[quantization]]
- 初出論文: -
- ファクトチェック: 未確認

### 生理計測・センシング

#### heart-rate-variability
- 定義: 心拍間隔（RR間隔）の時間的変動。自律神経活動の非侵襲的指標として使用
- 関連メモ: [[wearable-mental-health]]
- 初出論文: [[P-2501.01471_v2]]
- ファクトチェック: 確認済み（2025-12-27）
- 主要特徴量: RMSSD（時間領域）、HF（周波数領域）、SD1（非線形）

#### social-anxiety-disorder
- 定義: 社会的状況での過度の恐怖・不安を特徴とする精神疾患。SPINスコア等で評価
- 関連メモ: [[wearable-mental-health]]
- 初出論文: [[P-2501.01471_v2]]
- ファクトチェック: 確認済み（2025-12-27）

#### galvanic-skin-response
- 定義: 皮膚電気反応（GSR）。発汗による皮膚の電気伝導度変化を測定し、自律神経系の活性状態を推定
- 関連メモ: [[physiological-computing]]
- 初出論文: [[P-2501.00825_v1]]
- ファクトチェック: 確認済み（2025-12-27）
- 別名: EDA（Electrodermal Activity）、皮膚コンダクタンス

### 計算数学・アルゴリズム

#### collatz-conjecture
- 定義: 任意の正整数nに対し、偶数なら2で割り、奇数なら3n+1する操作を繰り返すと必ず1に到達するという予想。1937年提唱、未証明
- 関連メモ: [[algorithm-optimization]]
- 初出論文: [[P-2501.04032_v2]]
- ファクトチェック: 確認済み（2025-12-27）
- 関連用語: 停止時間（stopping time）、全停止時間（total stopping time）、Collatzツリー

#### bitwise-operations
- 定義: ビット単位の論理演算（AND, OR, XOR, NOT, シフト等）を用いたアルゴリズム最適化技術
- 関連メモ: [[algorithm-optimization]]
- 初出論文: [[P-2501.04032_v2]]
- ファクトチェック: 確認済み（2025-12-27）
- 典型例: n ∧ -n（最下位の1ビット取得）、n & (n-1)（最下位の1ビットをクリア）

### 心理学・人間特性

#### big-five-personality
- 定義: 性格心理学の5因子モデル。外向性（Extraversion）、協調性（Agreeableness）、誠実性（Conscientiousness）、情緒安定性（Emotional Stability/Neuroticism）、開放性（Openness）の5次元で性格を記述
- 関連メモ: [[personality-psychology]]
- 初出論文: [[P-2501.00825_v1]]
- ファクトチェック: 確認済み（2025-12-27）
- 評価尺度: IPIP（International Personality Item Pool）Big Five、NEO-PI-R等

### 評価・分析

#### out-of-bag-error
- 定義: Random Forestにおける汎化誤差推定手法。ブートストラップサンプリングで選ばれなかったデータ（約37%）を用いて予測誤差を計算
- 関連メモ: [[random-forest]]
- 初出論文: [[P-2501.00825_v1]]
- ファクトチェック: 確認済み（2025-12-27）
- 利点: 交差検証なしで汎化性能を推定可能

#### boruta-feature-selection
- 定義: Random Forestベースの特徴選択アルゴリズム。シャドウ特徴（元特徴をシャッフル）との比較で重要な特徴を統計的に選択
- 関連メモ: [[feature-selection]]
- 初出論文: [[P-2501.00825_v1]]
- ファクトチェック: 確認済み（2025-12-27）

#### ablation-study
- 定義: モデルの各コンポーネントの寄与を個別に評価する実験
- 関連メモ: [[ablation-study]]
- 初出論文: -
- ファクトチェック: 未確認

#### scaling-law
- 定義: モデルサイズ・データ量・計算量と性能の関係を記述する法則
- 関連メモ: [[scaling-law]]
- 初出論文: -
- ファクトチェック: 未確認

### AIガバナンス・政策

#### ai-incident-reporting
- 定義: AIシステムに起因する事故・問題を体系的に収集・分析・共有する仕組み。航空業界のASRS（Aviation Safety Reporting System）をモデルとする
- 関連メモ: [[AI-governance]]
- 初出論文: [[P-2501.14778_v1]]
- ファクトチェック: 確認済み（2025-12-27）
- 主要データベース: AIID（AI Incident Database）、AIAAIC Repository

#### aiid
- 定義: AI Incident Database。Partnership on AIが運営するオープンアクセスのAI事故データベース。McGregor (2021)により創設
- 関連メモ: [[AI-governance]]
- 初出論文: [[P-2501.14778_v1]]
- ファクトチェック: 確認済み（2025-12-27）
- URL: https://incidentdatabase.ai/

#### aiaaic
- 定義: AI, Algorithmic, and Automation Incidents and Controversies Repository。AIおよびアルゴリズムに関連する事故・論争を収集するデータベース
- 関連メモ: [[AI-governance]]
- 初出論文: [[P-2501.14778_v1]]
- ファクトチェック: 確認済み（2025-12-27）

#### trustworthy-ai
- 定義: 信頼性のあるAI。OECD AI原則に基づく4要素：公平性（Fairness）、透明性（Transparency）、堅牢性（Robustness）、説明責任（Accountability）
- 関連メモ: [[AI-governance]]
- 初出論文: [[P-2501.14778_v1]]
- ファクトチェック: 確認済み（2025-12-27）
- 関連規制: EU AI Act、OECD AI Principles

### サイバーセキュリティ

#### cyber-deception
- 定義: 攻撃者を欺き、誤誘導し、遅延させることでシステムを防御するセキュリティ技術。Honeypot、Honeytoken、Honeyfileなどの偽装資産を使用
- 関連メモ: [[cyber-deception]]
- 初出論文: [[P-2501.00940_v1]]
- ファクトチェック: 確認済み（2025-12-27）
- 関連技術: Honeypot, Honeytoken, API Hooking, MITRE ATT&CK

#### structured-prompt-engineering
- 定義: LLMに対して構造化されたプロンプト（Identity, Goal, Context, Strategy, Example, Output Formatの6要素等）を用いてドメイン特化タスクを実行させる手法
- 関連メモ: [[cyber-deception]]
- 初出論文: [[P-2501.00940_v1]]
- ファクトチェック: 確認済み（2025-12-27）
- 関連フレームワーク: SPADE（Structured Prompt-based Adaptive Deception Engineering）

#### mitre-attack
- 定義: MITRE ATT&CK（Adversarial Tactics, Techniques, and Common Knowledge）。攻撃者のTTP（戦術・技術・手順）を体系化したナレッジベース
- 関連メモ: [[cyber-deception]]
- 初出論文: [[P-2501.00940_v1]]
- ファクトチェック: 確認済み（2025-12-27）
- URL: https://attack.mitre.org/

---

## 新規キーワード追加テンプレート

```markdown
#### {keyword}
- 定義: {簡潔な定義}
- 関連メモ: [[{topic_name}]]
- 初出論文: [[P-{arxiv_id}]]
- ファクトチェック: 未確認 / 確認済み（{日付}）
```

## ファクトチェック手順

1. 論文本文と定義の照合
2. 既存メモとの矛盾確認
3. 必要に応じてWeb検索で最新情報確認
4. 確認後、ステータスを「確認済み（日付）」に更新
