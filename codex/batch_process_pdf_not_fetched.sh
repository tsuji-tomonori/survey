#!/bin/bash
# PDF未取得の論文を順番に処理するスクリプト
# pdf_not_fetched.tsv から行番号を読み込んで処理

TSV_FILE="${1:-pdf_not_fetched.tsv}"
START_INDEX=${2:-1}  # 何番目から開始するか（1始まり）

if [ ! -f "$TSV_FILE" ]; then
    echo "Error: $TSV_FILE not found"
    exit 1
fi

# TSVファイルから行番号を抽出（ヘッダーをスキップ）
LINE_NUMBERS=($(tail -n +2 "$TSV_FILE" | cut -f2))
TOTAL=${#LINE_NUMBERS[@]}

echo "[codex] Total papers to process: $TOTAL"
echo "[codex] Starting from index: $START_INDEX"
echo ""

for ((idx=START_INDEX-1; idx<TOTAL; idx++)); do
    LINE_NO=${LINE_NUMBERS[$idx]}
    CURRENT=$((idx + 1))

    echo "==========================================="
    echo "[codex] Processing paper $CURRENT / $TOTAL (line: $LINE_NO)"
    echo "==========================================="

    # /read を実行
    echo ">>> [codex] Running /read $LINE_NO"
    codex exec --full-auto -C . "/read $LINE_NO"
    if [ $? -ne 0 ]; then
        echo "Error: /read $LINE_NO failed"
        echo "To resume, run: $0 $TSV_FILE $CURRENT"
        exit 1
    fi

    # /check を実行
    echo ">>> [codex] Running /check $LINE_NO"
    codex exec --full-auto -C . "/check $LINE_NO"
    if [ $? -ne 0 ]; then
        echo "Error: /check $LINE_NO failed"
        echo "To resume, run: $0 $TSV_FILE $CURRENT"
        exit 1
    fi

    # /git:commit を実行
    echo ">>> [codex] Running /git:commit"
    codex exec --full-auto -C . "/git:commit"
    if [ $? -ne 0 ]; then
        echo "Error: /git:commit failed"
        echo "To resume, run: $0 $TSV_FILE $CURRENT"
        exit 1
    fi

    echo "[codex] Paper $CURRENT (line: $LINE_NO) completed successfully"
    echo ""
done

echo "[codex] All $TOTAL papers processed successfully!"
