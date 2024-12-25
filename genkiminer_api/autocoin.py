import requests


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjaGFpbiI6InRvbiIsImFjY291bnQiOjczMTUxNjg1MTcsInNhbHQiOiI5YmFhNDg5ZjRjNzhkY2RmOWJlNzMwNGY0MzAwYWUwZSIsImlhdCI6MTczMTc0MTEyNiwiZXhwIjoxNzMyMzQ1OTI2fQ.QzdOMNjUeQ-gQQQSxHs20GMiOWZ_6S9jPLM_ACW6Q-w",
    "content-type": "application/x-www-form-urlencoded",
    "dnt": "1",
    "origin": "https://game.genkiminer.fun",
    "priority": "u=1, i",
    "referer": "https://game.genkiminer.fun/",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

# url = "https://report.genkiminer.fun/api/report/analytics"
# data = {
#     "data%5B0%5D%5Bguid%5D": "16520001089402",
#     "data%5B0%5D%5BgameId%5D": "10000",
#     "data%5B0%5D%5BchannelId%5D": "",
#     "data%5B0%5D%5BgameVersion%5D": "1.0.0",
#     "data%5B0%5D%5BeventId%5D": "UI_Show",
#     "data%5B0%5D%5BdeviceId%5D": "",
#     "data%5B0%5D%5Bp1%5D": "0",
#     "data%5B0%5D%5Bp2%5D": "0",
#     "data%5B0%5D%5Bp3%5D": "0",
#     "data%5B0%5D%5Bp4%5D": "0",
#     "data%5B0%5D%5Bp5%5D": "0",
#     "data%5B0%5D%5Bs1%5D": "UIAutoReward",
#     "data%5B0%5D%5Bs2%5D": "",
#     "data%5B0%5D%5Bs3%5D": "",
#     "data%5B1%5D%5Bguid%5D": "16520001089402",
#     "data%5B1%5D%5BgameId%5D": "10000",
#     "data%5B1%5D%5BchannelId%5D": "",
#     "data%5B1%5D%5BgameVersion%5D": "1.0.0",
#     "data%5B1%5D%5BeventId%5D": "Game_ShowOffLineReward",
#     "data%5B1%5D%5BdeviceId%5D": "",
#     "data%5B1%5D%5Bp1%5D": "0",
#     "data%5B1%5D%5Bp2%5D": "0",
#     "data%5B1%5D%5Bp3%5D": "0",
#     "data%5B1%5D%5Bp4%5D": "0",
#     "data%5B1%5D%5Bp5%5D": "0",
#     "data%5B1%5D%5Bs1%5D": "[{\"itemId\":20001,\"count\":28}]",
#     "data%5B1%5D%5Bs2%5D": "[{\"itemId\":20001,\"count\":56}]",
#     "data%5B1%5D%5Bs3%5D": ""
# }
# response = requests.post(url, headers=headers, data=data)
#
# print(response.text)
# print(response)
# url = "https://api.genkiminer.fun/api/v1/player/itemData"
# response = requests.get(url, headers=headers)
#
# print(response.text)
# print(response)

url = "https://api.genkiminer.fun/api/v1/player/getAutoCoinReward"
data = {
    "isDouble": "0"
}
response = requests.post(url, headers=headers, data=data)



print(response.text)
print(response)

url = "https://report.genkiminer.fun/api/report/analytics"
data = {
    "data%5B0%5D%5Bguid%5D": "16520001089402",
    "data%5B0%5D%5BgameId%5D": "10000",
    "data%5B0%5D%5BchannelId%5D": "",
    "data%5B0%5D%5BgameVersion%5D": "1.0.0",
    "data%5B0%5D%5BeventId%5D": "Game_GetOffLineReward",
    "data%5B0%5D%5BdeviceId%5D": "",
    "data%5B0%5D%5Bp1%5D": "1",
    "data%5B0%5D%5Bp2%5D": "0",
    "data%5B0%5D%5Bp3%5D": "0",
    "data%5B0%5D%5Bp4%5D": "0",
    "data%5B0%5D%5Bp5%5D": "0",
    "data%5B0%5D%5Bs1%5D": "",
    "data%5B0%5D%5Bs2%5D": "",
    "data%5B0%5D%5Bs3%5D": ""
}

response = requests.post(url, headers=headers)

print(response.text)
print(response)
url = "https://api.genkiminer.fun/api/v1/player/itemData"
response = requests.get(url, headers=headers)

print(response.text)
print(response)
# headers = {
#     "accept": "application/json, text/plain, */*",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
#     "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjaGFpbiI6InRvbiIsImFjY291bnQiOjczMTUxNjg1MTcsInNhbHQiOiI5YmFhNDg5ZjRjNzhkY2RmOWJlNzMwNGY0MzAwYWUwZSIsImlhdCI6MTczMTc0MTEyNiwiZXhwIjoxNzMyMzQ1OTI2fQ.QzdOMNjUeQ-gQQQSxHs20GMiOWZ_6S9jPLM_ACW6Q-w",
#     "callbackid": "25",
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
#     "playerGuid": "16520001089402"
# }
# response = requests.get(url, headers=headers, params=params)
#
# print(response.text)
# print(response)