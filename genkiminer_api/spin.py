import requests
import time

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjaGFpbiI6InRvbiIsImFjY291bnQiOjc5NDQwNDgyNjMsInNhbHQiOiJlNTUwMGU2ZTgyMTE5YzAxYTRhNzZjOWUwZWNjMzhkYSIsImlhdCI6MTczMTY2MzkzNCwiZXhwIjoxNzMyMjY4NzM0fQ.TdmnQk_jAepOdcqMyhZPXQ4JE2SWgtaReSjgZW2TLdc",
    "cache-control": "no-cache",
    "callbackid": "151",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://game.genkiminer.fun",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://game.genkiminer.fun/",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}
url = "https://api.genkiminer.fun/api/v1/roulette/start"
data = {
    "opType": "0"
}

# 循环直到获取有效响应
while True:
    response = requests.post(url, headers=headers, data=data)

    try:
        json_response = response.json()
        print(json_response)  # 打印返回的 JSON

        # 检查返回的状态
        if json_response.get('status') == 30033:  # 当状态是 30033 时，退出循环
            print("状态为 30033, 退出循环。")
            break
        else:
            print(f"状态为 {json_response.get('status')}, 正在重新请求...")

    except ValueError:
        print("响应不是有效的 JSON 格式。")

    # 可以设置一个延时，避免频繁请求
    time.sleep(2)  # 可根据需要调整时间

while True:
    try:
        # 第一个请求
        url = "https://api.genkiminer.fun/api/v1/player/getTick"
        response = requests.get(url, headers=headers)

        # 检查响应状态
        if response.status_code != 200:
            print(f"请求错误: 状态码 {response.status_code}.")
            break

        print(response.text)  # 打印返回的内容
        print(response)  # 打印完整的响应对象

        # 第二个请求
        url = "https://api.genkiminer.fun/api/v1/roulette/start"
        data = {
            "opType": "2"
        }
        response = requests.post(url, headers=headers, data=data)

        # 检查响应状态
        if response.status_code != 200:
            print(f"请求错误: 状态码 {response.status_code}.")
            break

        json_response = response.json()  # 解析返回的 JSON
        print(json_response)  # 打印返回的 JSON

        # 检查返回状态
        if json_response.get('status') == 30033:  # 当状态是 30033 时，退出循环
            print("状态为 30033, 退出循环。")
            break

        print(response.text)  # 打印返回的内容
        print(response)  # 打印完整的响应对象

    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"发生错误: {e}")
        break

    # 可设置一个延时，避免频繁请求
    time.sleep(2)  # 可根据需要调整时间







# headers = {
#     "accept": "application/json, text/plain, */*",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
#     "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjaGFpbiI6InRvbiIsImFjY291bnQiOjYzNDg4MjkwNDQsInNhbHQiOiI1MjRkMWZhZWUzY2YxMmM0NjVlZjQwNGU3MWQ5NjhjYyIsImlhdCI6MTczMTY1ODg2NCwiZXhwIjoxNzMyMjYzNjY0fQ.jNHXXD9P-aAr4MRcIx8IRqgz75R-k4A4QdP7DF71PD4",
#     "callbackid": "299",
#     "content-type": "application/x-www-form-urlencoded",
#     "dnt": "1",
#     "origin": "https://game.genkiminer.fun",
#     "priority": "u=1, i",
#     "referer": "https://game.genkiminer.fun/",
#     "^sec-ch-ua": "^\\^Google",
#     "sec-ch-ua-mobile": "?0",
#     "^sec-ch-ua-platform": "^\\^Windows^^^",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
# }
# url = "https://api.genkiminer.fun/api/v1/player/itemData"
# params = {
#     "playerGuid": "16520001025641"
# }
# response = requests.get(url, headers=headers, params=params)
#
# print(response.text)
# print(response)