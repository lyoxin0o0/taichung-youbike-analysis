import requests
import pandas as pd
import os

# 台中市 YouBike API
url = "https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download?rid=9468c0d0-e1ed-4ecc-a86f-ab5a9fd590ff"

# 取得資料
response = requests.get(url=url,verify=False)

# 如果請求失敗就報錯
response.raise_for_status()

# JSON 轉成 Python 資料
data = response.json()

# 轉成 DataFrame
df = pd.DataFrame(data)


# =========================
# 1. 英文欄位改成中文
# =========================

columns_name = {
    "scity": "縣市名稱",
    "scityen": "英文縣市名稱",
    "sno": "場站代號",
    "sna": "場站中文名稱",
    "snaen": "英文場站名稱",
    "sarea": "場站所屬行政區",
    "sareaen": "英文行政區名稱",
    "ar": "中文地址",
    "aren": "英文地址",
    "tot": "場站總停車格數",
    "sbi": "目前可借車輛數",
    "bemp": "目前可還空位數",
    "mday": "資料更新時間",
    "lat": "緯度",
    "lng": "經度",
    "act": "場站營運狀態",
    "sbi_detail": "各車種可借數量明細"
}

df.rename(columns=columns_name, inplace=True)


# =========================
# 2. 只留下需要的欄位
# =========================

df = df[
    [
        "場站代號",
        "場站中文名稱",
        "場站所屬行政區",
        "中文地址",
        "場站總停車格數",
        "目前可借車輛數",
        "目前可還空位數",
        "資料更新時間",
        "緯度",
        "經度",
        "場站營運狀態",
        "各車種可借數量明細"
    ]
]


# =========================
# 3. 整理資料型態
# =========================

# 時間格式
df["資料更新時間"] = pd.to_datetime(
    df["資料更新時間"],
    format="%Y%m%d%H%M%S"
)

# 數字欄位轉成數字
df["場站總停車格數"] = pd.to_numeric(
    df["場站總停車格數"]
)

df["目前可借車輛數"] = pd.to_numeric(
    df["目前可借車輛數"]
)

df["目前可還空位數"] = pd.to_numeric(
    df["目前可還空位數"]
)

df["緯度"] = pd.to_numeric(
    df["緯度"]
)

df["經度"] = pd.to_numeric(
    df["經度"]
)


# =========================
# 4. 輸出 CSV
# =========================

filename = "ubike.csv"

df.to_csv(
    filename,
    index=False,
    encoding="utf-8-sig"
)


# =========================
# 5. 顯示結果
# =========================

print("YouBike 資料下載完成！")
print("資料筆數：", len(df))
print("CSV位置：", os.path.abspath(filename))

print()
print(df.head())