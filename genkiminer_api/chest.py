import requests


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjaGFpbiI6InRvbiIsImFjY291bnQiOjYzNDg4MjkwNDQsInNhbHQiOiJiMDVhMTgxYTc0ZDkzODdhNmIyYzYwMzA3ZWUzMTMzZCIsImlhdCI6MTczMTY1MTIzNiwiZXhwIjoxNzMyMjU2MDM2fQ.H1p9ukGe15aLa9172UTyX1CM7lUWseTNUfXXZtCP0XA",
    "callbackid": "655",
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
url = "https://api.genkiminer.fun/api/v1/player/getTick"
response = requests.get(url, headers=headers)

print(response.text)
print(response)