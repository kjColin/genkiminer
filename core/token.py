import requests

from core.headers import headers

session = requests.Session()


def get_token(data, proxies=None):
    url = "https://api.genkiminer.fun/api/v1/walletLogin/linkLogin2"
    data = {
        "initData": data}
    try:
        response = session.post(
            url=url, headers=headers(), data=data, proxies=proxies, timeout=20
        )
        token = response.json()['data']['loginToken']
        return token
    except:
        return None

