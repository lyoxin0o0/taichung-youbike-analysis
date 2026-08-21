# 🚲 臺中 YouBike 2.0 即時供需分析

使用 Python 串接臺中市 YouBike 2.0 即時公開資料 API，整理場站資訊並持續累積歷史資料，作為後續供需分析與資料視覺化使用。

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas\&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-F39C12)

## 📌 專案功能

* 取得臺中市 YouBike 2.0 即時資料
* JSON 轉換為 Pandas DataFrame
* 將 API 英文欄位轉為中文
* 整理日期、車輛數與場站資料
* 將每次抓取結果追加至 `ubike_history.csv`
* 記錄資料抓取時間
* 保留歷史資料供後續分析使用

## 🔄 資料流程

```text
YouBike API
    ↓
requests 取得 JSON
    ↓
Pandas DataFrame
    ↓
資料整理 / 欄位中文化
    ↓
加入抓取時間
    ↓
ubike_history.csv
```

## 📂 專案結構

```text
taichung-youbike-analysis/
│
├── data/
│   └── ubike_history.csv
│
├── ubike_parser.py
├── README.md
├── pyproject.toml
└── uv.lock
```

## 📊 主要資料欄位

| 欄位      | 說明               |
| ------- | ---------------- |
| 場站名稱    | YouBike 場站名稱     |
| 行政區     | 場站所在行政區          |
| 總停車格數   | 場站總容量            |
| 可借車輛數   | 目前可借車輛           |
| 可還空位數   | 目前可還車位           |
| 資料更新時間  | API 資料更新時間       |
| 抓取時間    | Python 實際取得資料的時間 |
| 緯度 / 經度 | 後續地圖分析使用         |

## 🛠️ 使用技術

`Python` `Requests` `Pandas` `CSV` `Git` `GitHub`

## 🚧 後續規劃

* [x] 即時資料取得
* [x] CSV 歷史資料累積
* [x] 更新時間紀錄
* [ ] 缺車 / 滿站分析
* [ ] 行政區供需分析
* [ ] 尖峰時段分析
* [ ] Matplotlib 視覺化
* [ ] Power BI Dashboard

## 💡 專案目標

透過累積不同時間點的 YouBike 資料，分析哪些場站容易缺車或沒有空位，以及不同時段與行政區的供需變化。
