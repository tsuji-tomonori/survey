---
type: meta
purpose: 語彙統制レジストリ
created: 2025-12-26
---

# 語彙統制レジストリ

プロパティで使用する語彙を統一するための辞書。

## methods（手法）

### アーキテクチャ
- transformer
- cnn
- rnn
- lstm
- gnn
- mlp
- autoencoder
- vae
- gan
- diffusion

### 学習手法
- supervised
- self-supervised
- contrastive
- distillation
- federated
- rl
- rlhf
- dpo
- ppo

### 効率化
- quantization
- pruning
- sparsity
- lora
- adapter
- prefix-tuning
- prompt-tuning

### 推論・生成
- retrieval
- rag
- cot
- tot
- speculative-decoding
- beam-search
- sampling

### その他
- alignment
- watermarking
- privacy
- differential-privacy
- ensemble

## tasks（タスク）

### NLP
- classification
- generation
- summarization
- translation
- qa
- dialogue
- ner
- pos-tagging
- parsing
- sentiment

### CV
- image-classification
- object-detection
- segmentation
- image-generation
- video-understanding

### マルチモーダル
- vqa
- image-captioning
- text-to-image
- text-to-video
- multimodal-understanding

### その他
- code-generation
- math-reasoning
- recommendation
- forecasting
- anomaly-detection

## signals（論文属性）

- theory
- empirical
- systems
- benchmark
- survey
- application
- position

## status（処理状態）

- inbox: 未処理
- queued: 処理待ち
- summarized: AI要約済み
- verified: 人間確認済み
- synthesized: 統合ノートに反映済み
- dropped: 対象外として除外

## 使用ルール

1. **表記ゆれの吸収**: 常に小文字、ハイフン区切り
   - NG: `RAG`, `Retrieval-Augmented Generation`
   - OK: `retrieval`, `rag`

2. **新規語彙の追加**: このファイルに追記してから使用

3. **エイリアス**: 必要に応じて aliases として管理
