import requests
import time

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjaGFpbiI6InRvbiIsImFjY291bnQiOjc5NDQwNDgyNjMsInNhbHQiOiJlMzIwNjUzNzZmNDcxNTE3NTU4NTdiNWRmMmNkN2RiNCIsImlhdCI6MTczMTY2NDAwNywiZXhwIjoxNzMyMjY4ODA3fQ.vN8MIqnCgNzpaPq3y7zyhcFsVD3Tyk17yU_t_UMTSSI",
    "callbackid": "469",
    "content-type": "application/x-www-form-urlencoded",
    "dnt": "1",
    "origin": "https://game.genkiminer.fun",
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
for i in range(10):
    try:
        url = "https://api.genkiminer.fun/api/v1/shop/createOrder"
        data = {
            "payType": "1",
            "shopItemId": "100"
        }
        response = requests.post(url, headers=headers, data=data)

        print(response.text)
        print(response)

        order_id = response.json()["data"]["id"]



        url = "https://api.genkiminer.fun/api/v1/player/getTick"
        response = requests.get(url, headers=headers)

        print(response.text)
        print(response)


        time.sleep(15)

        url = "https://api.genkiminer.fun/api/v1/shop/checkOrderReward"
        data = {
            "orderId": order_id
        }
        response = requests.post(url, headers=headers, data=data)

        print(response.text)
        print(response)
    except:
        print("Error")