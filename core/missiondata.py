import requests

from core.headers import headers



def get_info(token, proxies=None):
    url = "https://api.genkiminer.fun/api/v1/mission/missionData"

    try:
        response = requests.get(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        print(response.json())
    except Exception as e:
        print(f"Error: {e}")
        return None

