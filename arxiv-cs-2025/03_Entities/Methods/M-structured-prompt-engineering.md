---
type: method
name: "Structured Prompt Engineering"
name_full: "Structured Prompt Engineering"
name_ja: "構造化プロンプトエンジニアリング"
category: llm-technique
status: active
created: "2025-12-27"
updated: "2025-12-27"
---

# Structured Prompt Engineering

## 概要

LLM（大規模言語モデル）の出力を特定のドメイン・タスクに最適化するため、体系的に設計されたプロンプト構造を用いる手法。汎用LLMを専門タスクに適応させ、一貫性のある実用的な出力を生成する。

## SPADEフレームワーク（6コンポーネント）

サイバー欺瞞向けの構造化PE（SPADE: Structured Prompting for Adaptive Deception Engineering）:

### 1. Identity/Persona/Role
- LLMに役割・ペルソナを指定
- 例: "Act as a cybersecurity expert..."

### 2. Goal/Task
- 達成すべき具体的タスクを明示
- 曖昧さを排除し、運用目標との整合性を確保

### 3. Threat Context (Meaningful Context)
- マルウェア固有の行動、観測されたTTP、環境情報を記述
- ドメイン知識の注入

### 4. Strategy Outline (Dos & Don'ts)
- 運用制約、推奨/禁止事項を指定
- リソース効率やセキュリティ要件の反映

### 5. Output Example/Guidance (Few-Shot Prompting)
- 理想的な出力例やテンプレートを提供
- 出力の一貫性向上

### 6. Output Instructions/Output Format
- 出力フォーマット（JSON, XML等）を指定
- メタデータ仕様の定義

## 効果

- **Relevance向上**: タスク・目標との整合性改善
- **Actionability向上**: 実装詳細の具体化
- **Feasibility向上**: 運用環境での実現可能性確保
- **Realism向上**: 生成物の現実性・説得力向上

## 適用例

### サイバーセキュリティ
- 適応的欺瞞戦術の生成（honeyfile, API hook, honeytoken）
- マルウェア対策のリアルタイム戦略設計

### 一般的なLLM活用
- 特定ドメインの文書生成
- コード生成・レビュー
- 技術文書の構造化

## 関連研究

- White et al. (2023): Prompt Pattern Catalog for ChatGPT
- Giray (2023): Prompt Engineering for Academic Writers

## Papers
- [[P-2501.00940_v1]]: SPADE - サイバー欺瞞向け構造化PE

## Links
- Topics: [[cyber-deception]], [[prompt-engineering]], [[LLM-security]]
- Related Methods: [[few-shot-prompting]], [[chain-of-thought]]
