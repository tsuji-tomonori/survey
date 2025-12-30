#!/bin/bash
# codex版: 論文を指定範囲で順番に処理するスクリプト

START=${1:-12}
END=${2:-100}

echo "[codex] Processing papers from $START to $END"

for i in $(seq $START $END); do
    echo "=========================================="
    echo "[codex] Processing paper $i / $END"
    echo "=========================================="

    # /read を実行
    echo ">>> [codex] Running /read $i"
    codex exec --full-auto -C . "/read $i"
    if [ $? -ne 0 ]; then
        echo "Error: /read $i failed"
        exit 1
    fi

    # /check を実行
    echo ">>> [codex] Running /check $i"
    codex exec --full-auto -C . "/check $i"
    if [ $? -ne 0 ]; then
        echo "Error: /check $i failed"
        exit 1
    fi

    # /git:commit を実行
    echo ">>> [codex] Running /git:commit"
    codex exec --full-auto -C . "/git:commit"
    if [ $? -ne 0 ]; then
        echo "Error: /git:commit failed"
        exit 1
    fi

    echo "[codex] Paper $i completed successfully"
    echo ""
done

echo "[codex] All papers processed successfully!"
