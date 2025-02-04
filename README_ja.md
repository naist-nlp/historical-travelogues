# JHistTravel: 日本語歴史的紀行文アノテーションデータセット（Version 1.0）

## 概要

本データセットは、近世・近代の日本語歴史的紀行文に場所参照表現をアノテーションしたデータです。

## フォルダ構成

~~~~
data
+--- okuno_hosomichi
|    +--- json
|    +--- tsv
|    +--- xml
+--- tokkan_kikou
|    +--- json
|    +--- tsv
|    +--- xml
+--- src
~~~~

## データ統計

以下のコマンド（Python 3.8.0以上が必要）でも確認できます。
- `src/show_data_statistics.py -i data/okuno_hosomichi/json/okuno_hosomichi.json`
- `src/show_data_statistics.py -i tokkan_kikou/json/tokkan_kikou.json`

|                        |Hosomichi|Tokkan|
|--                      |--       |--    |
|Article                 |       49|     1|
|Sentence                |      525|   192|
|Chars                   |   10,791| 7,754|
|Mention (UNCERTAIN含む) |      556|   243|
|Mention (UNCERTAIN除外) |      450|   240|

## 場所参照表現のタイプ

場所参照表現（LREまたはメンション）のタイプとして以下を定義しています。
`NAME`と`NOM`のサブタイプを持つものは、固有名とその他の表現を区別しています。

|Tag                     |Description                        |
|--                      |--                                 |
|`LOC_NAME`/`LOC_NOM`    |地名・地形名                       |
|`FAC_NAME`/`FAC_NOM`    |施設名                             |
|`LINE_NAME`/`LINE_NOM`  |道路・水路・交通機関路線名         |
|`VEHICLE`               |乗り物名                           |
|`DEICTIC`               |上記いずれかを指す指示表現等       |
|`UNCERTAIN`             |LREの可能性があるが、定かでないもの|

## データフォーマット

### TSV

- 1行1文のタブ区切りテキストで、以下の列からなります。
  - 1列目: 記事ID
  - 2列目: 文ID
  - 3列目: テキスト本文
  - 4列目: メンション情報（メンションID,開始インデックス:終了インデックス,タイプ,テキスト）

~~~~
1	002	舟の上に生涯をうかべ馬の口とらへて老をむかふるものは日日旅にして旅をすみかとす	M001,0:1,VEHICLE,舟
~~~~
### JSON

- 記事ID（例：`1`）に対してarticle（記事）が紐づいており、
  articleは`sentences`、`mentions`要素を持ちます。
    ~~~~
    {
      "1": {
        "sentences": {
        ...
        },
        "mentions": {
        ...
        },
      ...
    }
    ~~~~
- `sentences`以下の各sentenceは次のようになっています。
  場所参照表現（メンション）以外の情報は、attributes属性で保持されています。
    ~~~~
        "sentences": {
          "001": {
            "text": "月日は百代の過客にしてゆきかふ年も又旅人なり",
            "mention_ids": []
          },
          "002": {
            "text": "舟の上に生涯をうかべ馬の口とらへて老をむかふるものは日日旅にして旅をすみかとす",
            "mention_ids": [
              "M001"
            ],
            "attributes": [
              {
                "type": "odoriji",
                "span": [
                  27,
                  28
                ],
                "text": "日",
                "originalText": "〳〵"
              }
            ]
          },
          ...
          "007": {
            "text": "おもて八句を庵の柱にかけおき",
            "mention_ids": [
              "M010"
            ]
          }
        },
    ~~~~
- `mentions`以下の各mentionは次のようになっています。
    ~~~~
        "mentions": {
          "M001": {
            "sentence_id": "002",
            "span": [
              0,
              1
            ],
            "text": "舟",
            "entity_type": "VEHICLE"
          },
          ...
          "M010": {
            "sentence_id": "007",
            "span": [
              6,
              7
            ],
            "text": "庵",
            "entity_type": "FAC_NOM"
          }
        }
    ~~~~

### XML

以下の構造で、記事（`<article>`）、文（`<s>`）が保持され、
メンション・属性情報は文内部のタグで表されています。

~~~~
<text><article><s>...</s></article>...</text>
~~~~

## ライセンス

本データを利用する際、データごとのライセンスに従ってください。

- 「おくのほそ道」データ（okuno_hosomichi）
  - ライセンス: CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>
  - 本文データ出典: <https://ja.wikisource.org/wiki/%E3%81%8A%E3%81%8F%E3%81%AE%E3%81%BB%E3%81%9D%E9%81%93>
- 「突貫紀行」データ（tokkan_kikou）
  - ライセンス: CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>
  - 本文データ出典: <https://www.aozora.gr.jp/cards/000051/files/830_14079.html>

## 更新履歴

- 2025/02/04: Version 1.0 公開

## 引用

本データを用いた研究を発表される場合、以下いずれかを引用ください。

~~~~
@inproceedings{katayama-etal-2024-evaluating,
    title = "Evaluating Language Models in Location Referring Expression Extraction from Early Modern and Contemporary {J}apanese Texts",
    author = "Katayama, Ayuki and Sakai, Yusuke and Higashiyama, Shohei and Ouchi, Hiroki and Takeuchi, Ayano and Bando, Ryo and Hashimoto, Yuta and Ogiso, Toshinobu and Watanabe, Taro",
    booktitle = "Proceedings of the 4th International Conference on Natural Language Processing for Digital Humanities",
    month = nov,
    year = "2024",
    address = "Miami, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.nlp4dh-1.33/",
    doi = "10.18653/v1/2024.nlp4dh-1.33",
    pages = "331--338",
~~~~

~~~~
@inproceedings{katayama-etal-2025-kinsei,
    title = "近世・近代・現代日本語テキストに対する場所参照表現抽出",
    author = "片山, 歩希 and 東山, 翔平 and 大内, 啓樹 and 坂井, 優介 and 竹内, 綾乃 and 坂東, 諒 and 橋本, 雄太 and 小木曽, 智信 and 渡辺, 太郎"
    booktitle = "言語処理学会第31回年次大会発表論文集",
    month = mar,
    year = "2025",
~~~~
