#!/bin/bash
# 論文を2から100まで順番に処理するスクリプト

START=${1:-12}
END=${2:-100}

echo "Processing papers from $START to $END"

for i in $(seq $START $END); do
    echo "=========================================="
    echo "Processing paper $i / $END"
    echo "=========================================="

    # /read を実行
    echo ">>> Running /read $i"
    claude -p "/read $i"
    if [ $? -ne 0 ]; then
        echo "Error: /read $i failed"
        exit 1
    fi

    # /check を実行
    echo ">>> Running /check $i"
    claude -p "/check $i"
    if [ $? -ne 0 ]; then
        echo "Error: /check $i failed"
        exit 1
    fi

    # /git:commit を実行
    echo ">>> Running /git:commit"
    claude -p "/git:commit"
    if [ $? -ne 0 ]; then
        echo "Error: /git:commit failed"
        exit 1
    fi

    echo "Paper $i completed successfully"
    echo ""
done

echo "All papers processed successfully!"
