"""
web_api_weather.py
"""
import json
import requests

# JSONデータをリクエストする際のベースURL
base_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city={city}'

# 調べたい都市のID
city_id = '440020'

# APIのURL
url = base_url.format(city=city_id)

# APIへリクエストを送信
res = requests.get(url)

# アクセスチェック
res.raise_for_status()

# レスポンスのJSONデータをPythonオブジェクトへ変換
data = json.loads(res.text)

# 必要な情報を抽出
print("**** Weather Information@Oita ****")
print("[TIME]")
print(data["description"]["publicTime"])
print("[INFOMATION]")
print(data["description"]["text"])
print("[FORECASTS]")
for i in range(3):
    print("DATE:{} / {}".format(data["forecasts"][i]["date"], data["forecasts"][i]["telop"]))
