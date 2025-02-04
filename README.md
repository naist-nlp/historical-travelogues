# JHistTravel: Japanese Historical Travelogue Annotation Dataset (Version 1.0)

## Overview

This dataset consists of early modern and modern Japanese historical travelogues annotated with location referring expressions (LREs).

## Folder Structure

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

## Data Statistics

You can check the following commands (Python 3.8.0 or later required):
- `src/show_data_statistics.py -i data/okuno_hosomichi/json/okuno_hosomichi.json`
- `src/show_data_statistics.py -i tokkan_kikou/json/tokkan_kikou.json`

|                              |Hosomichi|Tokkan|
|--                            |--:      |--:   |
|Article                       |       49|     1|
|Sentence                      |      525|   192|
|Chars                         |   10,791| 7,754|
|Mention (including UNCERTAIN) |      556|   243|
|Mention (excluding UNCERTAIN) |      450|   240|

## Types of LREs

The following types are defined for location referring expressions (LREs or mentions). Those labeled `NAME` and `NOM` are distinguished as proper nouns and other expressions, respectively.

|Tag                     |Description                              |
|--                      |--                                       |
|`LOC_NAME`/`LOC_NOM`    |Location                                 |
|`FAC_NAME`/`FAC_NOM`    |Facility                                 |
|`LINE_NAME`/`LINE_NOM`  |Road, waterway, public transport route   |
|`VEHICLE`               |Vehicle                                  |
|`DEICTIC`               |Expressions referring to any of the above|
|`UNCERTAIN`             |Possibly an LRE but uncertain            |

## Data Format

### TSV

- A tab-separated text file with one sentence per line, comprising the following columns:
  - Column 1: Article ID
  - Column 2: Sentence ID
  - Column 3: Text body
  - Column 4: Mention information (mention ID, start_index:end_index, type, text)

~~~~
1	002	舟の上に生涯をうかべ馬の口とらへて老をむかふるものは日日旅にして旅をすみかとす	M001,0:1,VEHICLE,舟
~~~~
### JSON

- Each article (e.g., `1`) is associated with an `article`, which contains `sentences` and `mentions` elements:
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
- Each sentence under `sentences` is structured as follows. Information other than LREs (mentions) is stored in the `attributes` attribute:
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
- Each mention under `mentions` is structured as follows:
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

Articles (`<article>`) and sentences (`<s>`) are stored in the following structure,
with mention and attribute information indicated as tags within each sentence.

~~~~
<text><article><s>...</s></article>...</text>
~~~~

## License

When using this data, please follow the license for each dataset.

- "Okuno Hosomichi" data (okuno_hosomichi)
  - License: CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>
  - Data source: <https://ja.wikisource.org/wiki/%E3%81%8A%E3%81%8F%E3%81%AE%E3%81%BB%E3%81%9D%E9%81%93>
- "Tokkan Kikou" data (tokkan_kikou)
  - License: CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>
  - Data source: <https://www.aozora.gr.jp/cards/000051/files/830_14079.html>

## Update History

- 2025/02/04: Version 1.0 published

## Citation

If you publish research using this data, please cite one of the following:

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
    title = "Location Referring Expression Extraction for Early Modern, Modern, and Contemporary Japanese Texts [In Japanese]",
    author = "Katayama, Ayuki and Sakai, Yusuke and Higashiyama, Shohei and Ouchi, Hiroki and Takeuchi, Ayano and Bando, Ryo and Hashimoto, Yuta and Ogiso, Toshinobu and Watanabe, Taro",
    booktitle = "Proceedings of the 31st Annual Meeting of the Association for Natural Language Processing",
    month = mar,
    year = "2025",
~~~~
