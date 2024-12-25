import requests

from smart_airdrop_claimer import base
from core.headers import headers
import time


def spin(token, proxies=None):
    # 循环直到获取有效响应
    while True:
        url = "https://api.genkiminer.fun/api/v1/roulette/start"
        data = {
            "opType": "0"
        }

        response = requests.post(url, headers=headers(token), data=data)

        try:
            json_response = response.json()

            # 打印返回的 JSON
            base.log(f"{base.white}Response: {json_response}")

            # 检查返回的状态
            if json_response.get('status') == 30033:  # 当状态是 30033 时，退出循环
                base.log(f"{base.white}Status: {base.green}30033, {base.yellow}Exiting loop.")
                break
            else:
                base.log(f"{base.white}Status: {base.red}{json_response.get('status')}, {base.yellow}Retrying...")

        except ValueError:
            base.log(f"{base.white}Error: {base.red}Response is not valid JSON.")

        # 设置延时，避免频繁请求
        time.sleep(2)

    while True:
        try:
            # 第一个请求
            url = "https://api.genkiminer.fun/api/v1/player/getTick"
            response = requests.get(url, headers=headers(token))

            # 检查响应状态
            if response.status_code != 200:
                base.log(f"{base.white}Request Error: {base.red}Status Code {response.status_code}.")
                break

            # 打印返回的内容
            base.log(f"{base.white}Response: {base.green}{response.text}")
            time.sleep(15)  # 可根据需要调整时间

            # 第二个请求
            url = "https://api.genkiminer.fun/api/v1/roulette/start"
            data = {
                "opType": "2"
            }
            response = requests.post(url, headers=headers(token), data=data)

            # 检查响应状态
            if response.status_code != 200:
                base.log(f"{base.white}Request Error: {base.red}Status Code {response.status_code}.")
                break

            json_response = response.json()  # 解析返回的 JSON
            base.log(f"{base.white}Response: {base.green}{json_response}")

            # 检查返回状态
            if json_response.get('status') == 30033:  # 当状态是 30033 时，退出循环
                base.log(f"{base.white}Status: {base.green}30033, {base.yellow}Exiting loop.")
                break

            base.log(f"{base.white}Response Text: {base.green}{response.text}")
            base.log(f"{base.white}Full Response: {base.green}{response}")

        except (requests.exceptions.RequestException, ValueError) as e:
            base.log(f"{base.white}Error: {base.red}An error occurred: {e}")
            break

        # 设置延时，避免频繁请求
        time.sleep(2)
