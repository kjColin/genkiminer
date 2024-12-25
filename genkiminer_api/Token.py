import requests
import json
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "authorization": "",  # 去掉多余的分号
    "cache-control": "no-cache",
    "callbackid": "3",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://game.genkiminer.fun",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://game.genkiminer.fun/",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}
url = "https://api.genkiminer.fun/api/v1/walletLogin/linkLogin2"
data = {
    "initData": "query_id=AAGHjoBZAwAAAIeOgFk5y82x&user=%7B%22id%22%3A7944048263%2C%22first_name%22%3A%22Prima%20Moulton%22%2C%22last_name%22%3A%22%22%2C%22language_code%22%3A%22zh-hans%22%2C%22allows_write_to_pm%22%3Atrue%2C%22photo_url%22%3A%22https%3A%5C%2F%5C%2Ft.me%5C%2Fi%5C%2Fuserpic%5C%2F320%5C%2FcSHOx-GmD61OSYvQEknAxcseVn02ZCnP4mlOfsT7ZDwc5wkAGajAalYvZ0vvEbE5.svg%22%7D&auth_date=1731663883&hash=cccbfa50e801b24902e5d7c7c44b0c12b2ca48e1ab0f47f416be084cfa8341c3"
}
response = requests.post(url, headers=headers, data=data)

print(response.json())
print(response)

Token = response.json()['data']['loginToken']
print(Token)
# {'status': 10000, 'msg': 'ok', 'data': {'guid': '16520001025641', 'accountName': 6348829044, 'curEquipGuid': 16860300907256, 'checkin_data': 0, 'checkin_reward_data': 0, 'last_checkin_date': 0, 'totalPoint': 2002, 'claimableRankReward': 0, 'firstTimeLoginDone': 201, 'offLineReward': {'rewardList': [], 'leaveTime': 0}, 'autoCoinGetTime': 1731672416, 'guiderProcess': 255, 'gemClaimProcess': 0, 'isFirstLogin': True, 'items': {'20007': {'guid': 20007, 'playerId': '16520001025641', 'itemId': 20007, 'bagType': 0, 'count': 0, 'createdAt': '', 'updatedAt': ''}, '15220102286568': {'guid': 15220102286568, 'count': 2002, 'playerId': '16520001025641', 'itemId': 20000, 'bagType': 0}, '15220102286569': {'guid': 15220102286569, 'count': 3100, 'playerId': '16520001025641', 'itemId': 20001, 'bagType': 0}, '15220102286950': {'guid': 15220102286950, 'count': 200, 'playerId': '16520001025641', 'itemId': 20005, 'bagType': 0}}, 'missions': {}, 'equips': {'16860300907256': {'guid': 16860300907256, 'playerId': '16520001025641', 'equipId': 1, 'curDur': 100, 'maxDur': 100, 'toolLv': 1, 'gradeLv': 0, 'goldBoostValue': '1', 'gemBoostValue': '1', 'cdValue': '0', 'durIncrBeginTime': 1731653249, 'offlineGoldBoostValue': 5, 'keysBoostValue': '1', 'repairCostReduce': '0'}}, 'channel': '', 'loginToken': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjaGFpbiI6InRvbiIsImFjY291bnQiOjYzNDg4MjkwNDQsInNhbHQiOiI2MGNkNGYzMDg2ODc2NmUxMGYzYzk2ODdkNTliODI4MSIsImlhdCI6MTczMTY1MzI3NCwiZXhwIjoxNzMyMjU4MDc0fQ.1uOM5tO9PnBmKIjllKvdtZ3ACobkzKiD8NEv13IlcaI'}}
