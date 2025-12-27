---
type: topic
name: "Cyber Deception"
name_ja: "サイバー欺瞞"
aliases: ["Cyber Defense Deception", "Active Defense", "Deception Technology"]
category: cybersecurity
status: active
created: "2025-12-27"
updated: "2025-12-27"
---

# Cyber Deception

## 概要

攻撃者を欺き、誤誘導し、遅延させることでシステムを防御するセキュリティ技術。Honeypot、Honeytoken、Honeyfileなどの偽装資産を用いて、攻撃者の行動を監視・分析しながら実システムを保護する。

## 主要技術

### 静的欺瞞
- **Honeypot**: 攻撃者を誘引する偽装システム
- **Honeytoken**: 認証情報などの偽装データ
- **Honeyfile**: 監視付き偽装ファイル
- **Honeynet**: 複数のHoneypotで構成されるネットワーク

### 動的欺瞞
- **API Hooking**: 悪意あるAPI呼び出しを傍受し偽情報を返す
- **MITRE ATT&CK連携**: TTP分析に基づく適応的欺瞞戦略
- **LLM駆動欺瞞**: 生成AIによる動的・文脈適応的な欺瞞生成

## 技術的アプローチ

### 従来手法
- 手動設定による静的ルール
- 事前定義されたデコイ資産の配置
- 限定的な適応性

### GenAI駆動アプローチ
- 構造化プロンプトエンジニアリング（SPADE等）
- マルウェア行動分析に基づく動的戦術生成
- 多層的・適応的欺瞞戦略の自動化

## 評価指標

- **エンゲージメント率**: マルウェアが欺瞞資産と相互作用した割合
- **精度**: 欺瞞が成功裏に攻撃者を誤誘導した割合
- **反復回数**: 展開可能な出力までの調整回数
- **リアリズム**: 欺瞞資産の現実性（専門家評価）

## 関連フレームワーク

- **MITRE ATT&CK**: 攻撃者のTTP（戦術・技術・手順）の体系化
- **CHIMERA**: マルウェア欺瞞の自律計画・オーケストレーション
- **SODA**: サイバー欺瞞オーケストレーション・自動化システム
- **SPADE**: 構造化プロンプトによる適応的欺瞞エンジニアリング

## 関連論文

```dataview
TABLE title, year, score
FROM "01_Papers"
WHERE contains(tasks, "cyber-deception")
SORT score DESC
```

## Papers
- [[P-2501.00940_v1]]: SPADE - GenAI+構造化PEによる適応的サイバー欺瞞戦略

## Links
- Methods: [[honeypot]], [[API-hooking]], [[structured-prompt-engineering]]
- Related Topics: [[LLM-security]], [[malware-analysis]], [[prompt-engineering]]
