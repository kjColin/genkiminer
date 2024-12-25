import requests

from smart_airdrop_claimer import base
from core.headers import headers

import requests


def coin(token, proxies=None):
    url = "https://api.genkiminer.fun/api/v1/player/getAutoCoinReward"
    data = {"isDouble": "0"}
    try:
        # 生成请求头
        headers_data = headers(token=token)

        # 发起 POST 请求
        response = requests.post(
            url=url, headers=headers_data, data=data, proxies=proxies, timeout=20
        )
        response.raise_for_status()  # 检查 HTTP 错误

        # 解析响应
        response_data = response.json()
        base.log(f"{base.white}Response: {base.green}{response_data}")
        return response_data

    except requests.exceptions.RequestException as req_err:
        base.log(f"{base.white}Request Error: {base.red}{req_err}")
    except ValueError as val_err:
        base.log(f"{base.white}JSON Parse Error: {base.red}{val_err}")
    except Exception as e:
        base.log(f"{base.white}Unexpected Error: {base.red}{e}")

    return None

