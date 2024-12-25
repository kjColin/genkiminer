import requests

# 31.49 265.96
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjaGFpbiI6InRvbiIsImFjY291bnQiOjc2MzQzNzkyMDEsInNhbHQiOiIwNzBmOWNiYjI5MThhMmE5N2E5MjgzZTRkNWU4MzU5ZSIsImlhdCI6MTczMTg5Nzc0MCwiZXhwIjoxNzMyNTAyNTQwfQ.Vcab8j8iEkzPuN3ALK_Xur02P7fQMofuPhqua_yG5t0",
    "cache-control": "no-cache",
    "callbackid": "279",
    "content-type": "application/x-www-form-urlencoded",
    "dnt": "1",
    "origin": "https://game.genkiminer.fun",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://game.genkiminer.fun/",
    "^sec-ch-ua": "^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "^sec-ch-ua-platform": "^\\^Windows^^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
url = "https://api.genkiminer.fun/api/v1/mine/dig"
import requests
import time

player_guid = "16520001096421"  # 替换为你的 playerGuid
initial_tile_index = ("15305")  # 初始的 tileIndex

current_tile_index = initial_tile_index  # 初始化为起始的 tileIndex

while True:
    # 请求数据
    data = {
        # "playerGuid": player_guid,
        "tileIndex": current_tile_index
    }
    response = requests.post(url, headers=headers, data=data)

    # 输出服务器返回的信息
    print(f"Response Text: {response.text}")
    print(f"Response Status Code: {response.status_code}")

    # 检查响应状态
    if response.status_code != 200:
        print("Request failed. Stopping the loop.")
        break

    # 解析响应 JSON 数据
    try:
        response_json = response.json()
        if response_json.get("status") != 10000:
            print("Invalid status in response. Stopping the loop.")
            break

        # 获取下一个 tileIndex
        refresh_data = response_json["data"]["refreshData"]
        index_list = refresh_data["indexList"]

        # 找到当前 tileIndex 的位置
        try:
            current_index = index_list.index(int(current_tile_index))
            # 循环到下一个索引
            next_index = (current_index + 1) % len(index_list)
            current_tile_index = str(index_list[next_index])
        except ValueError:
            print("Current tileIndex not found in indexList. Stopping the loop.")
            break

    except Exception as e:
        print(f"Error parsing response JSON: {e}")
        break

    # 控制循环间隔时间，避免过多请求
    time.sleep(2)
