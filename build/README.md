# build — 巻二「データ通信技術」の編集手順

`index.html` は単一ファイルで完結します（ビルド不要・オフライン動作）。
ただし **巻二（NET配列・60日分・約1MB）だけ**は、編集しやすいよう
`build/net/week1.js`〜`week9.js` に分けて置いてあります。

## 編集の流れ

```bash
# 1. 該当する週のファイルを直接編集する
#    例: Day 29 を直したい → build/net/week5.js（第5週 = Day 29〜35）

# 2. index.html へ注入する
python3 build/assemble.py
```

`assemble.py` は `index.html` 内の
`<!-- NET:START -->` 〜 `<!-- NET:END -->` を丸ごと差し替えます。
何度実行しても結果は同じです（冪等）。

## 週とDayの対応

| ファイル | 週 | Day |
|---|---|---|
| week1.js | 第1週 通信のいろは | 1–7 |
| week2.js | 第2週 信号を運ぶ技術 | 8–14 |
| week3.js | 第3週 LANとイーサネット | 15–21 |
| week4.js | 第4週 無線通信 | 22–28 |
| week5.js | 第5週 TCP/IPとインターネット | 29–35 |
| week6.js | 第6週 トランスポートとアプリ層 | 36–42 |
| week7.js | 第7週 通信セキュリティ | 43–49 |
| week8.js | 第8週 現代の通信インフラ | 50–56 |
| week9.js | 総仕上げ | 57–60 |

## 巻一・別冊を直したいとき

巻一（DAYS）と別冊（DEEP）は `index.html` 内に直接書かれています。
`DAYS.push({` / `DEEP.push({` を検索して、その場で編集してください。
`assemble.py` はこれらに触れません。

## 1日ぶんのデータ構造

```js
NET.push({
  day: 29,                  // 通し番号
  week: 5,                  // 週番号（1〜9）
  title: "…",
  goals: ["…"],             // 到達点。4つが目安
  sections: [               // 本文。4〜5節
    { heading:"…", html:"<p>…</p>",
      code:{ lang:"text", title:"…", body:"…" },  // 任意
      tryIt:true }                                 // html/js のみ実行可
  ],
  exercise: { title, html, starter?, hintHtml, solutionHtml, solutionCode },
  quiz: [{ q, choices:[4つ], answer:0-3, explain }],
  takeaways: ["…"],         // 5つが目安
  aiPrompt: "…"
});
```

### 本文で使える書式

| 書き方 | 見え方 |
|---|---|
| `<div class="analogy">…</div>` | 「たとえ話」ラベル付きの傍注 |
| `<div class="callout note">…</div>` | 「NOTE 覚え書き」 |
| `<div class="callout tip">…</div>` | 「TIP こつ」 |
| `<div class="callout warn">…</div>` | 「WARN 注意」 |
| `<table>…</table>` | 罫線表（横スクロール対応） |
| `<code>…</code>` | インラインコード |

傍注の先頭に絵文字を置いても、表示時に自動で取り除かれます
（ラベルはCSSが描くため）。

## デザイン

Hallmarkスキルで設計。記録は `.hallmark/log.json`。
配色・書体・余白はすべて `index.html` 冒頭の `<style>` 内の
CSSカスタムプロパティに集約されています。巻ごとの刷り色は
`body[data-vol="1"|"2"]` で切り替わります。

## プレビュー

ルートの `.claude/launch.json` に `vibe-coding-tutorial`（port 8881）を登録済み。
