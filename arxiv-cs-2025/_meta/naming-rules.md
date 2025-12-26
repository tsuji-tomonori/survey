---
type: meta
purpose: 命名規則
created: 2025-12-26
---

# 命名規則

## ファイル名

### 論文ノート
- パターン: `P-{arxiv_id}.md`
- 例: `P-2501.00732_v1.md`
- 保存先: `01_Papers/2025/{primary_category}/`

### 手法エンティティ
- パターン: `M-{method_name}.md`
- 例: `M-transformer.md`, `M-gradient-compression.md`
- 保存先: `03_Entities/Methods/`

### データセットエンティティ
- パターン: `D-{dataset_name}.md`
- 例: `D-ImageNet.md`, `D-GLUE.md`
- 保存先: `03_Entities/Datasets/`

### 著者エンティティ
- パターン: `A-{author_name}.md`
- 例: `A-Yoshua-Bengio.md`
- 保存先: `03_Entities/Authors/`

### トピックノート
- パターン: `{topic_name}.md`
- 例: `federated-learning.md`
- 保存先: `02_Topics/`

### 統合ノート
- パターン: `{period}.md`
- 例: `2025-Q1.md`, `2025-01.md`
- 保存先: `04_Syntheses/2025/{category}/`

### PDF
- パターン: `{arxiv_id}.pdf`
- 例: `2501.00732_v1.pdf`
- 保存先: `90_Attachments/pdf/2025/`

## arXiv ID の扱い

- バージョン番号は `v` を `_v` に変換
  - 元: `2501.00732v1`
  - 変換後: `2501.00732_v1`
- 理由: ファイルシステムでの扱いやすさ

## 手法名・トピック名

- 小文字、ハイフン区切り
- 例: `federated-learning`, `gradient-compression`
- 頭字語は小文字: `rag`, `llm`, `vae`

## 日付

- ISO 8601形式: `YYYY-MM-DD`
- 例: `2025-01-01`
