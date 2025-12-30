---
type: topic
name: "Lip Biometrics"
aliases: ["唇バイオメトリクス", "口唇認証", "lip-based authentication"]
domain: ["biometrics", "computer-vision"]
created: "2025-12-30"
---

# Lip Biometrics

## 概要
唇の形状・テクスチャ・運動（articulator dynamics）を用いて個人識別や検証を行うバイオメトリクス。顔全体よりもプライバシー配慮がしやすく、連続認証に適する。

## 特徴量
- 静的: 面積・周長・厚さ・境界形状など。
- テクスチャ: GLCM 等の統計特徴、フィルタバンク応答。
- 動的: 調音器官の時系列運動、ランドマーク相関、リップ溝の動きベクトル。

## 評価指標
- Accuracy/Precision/Recall/F1 に加え、FAR/FRR/EER、ROC/DET 曲線、しきい値選定。
- 攻撃成功率（mimic/replay/deepfake）を条件付きで報告。

## 典型的な攻撃
- 模倣（mimic）、写真・動画によるリプレイ、リップシンク deepfake。

## 関連論文
- [[P-2501.01032_v1]]: 形状非依存の調音ダイナミクスで 99% 超の精度と低い攻撃成功率。

## 関連トピック
- [[continuous-authentication]]

