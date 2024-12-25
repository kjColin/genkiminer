import requests
import sys
import time

from core.headers import headers
from smart_airdrop_claimer import base


sys.dont_write_bytecode = True

def ads(token, proxies=None):
        try:
            base.log(f"{base.white}Attempt : {base.yellow}Fetching player tick...")
            url = "https://api.genkiminer.fun/api/v1/player/getTick"
            response = requests.get(url, headers=headers(token=token), proxies=proxies, timeout=20)
            print(response.text)
            print(response)
            if response.status_code == 200:
                base.log(f"{base.white}Player tick fetched: {base.green}{response.json()}")
            else:
                base.log(f"{base.white}Failed to fetch player tick: {base.red}{response.text}")

            # # 等待 15 秒
            # base.log(f"{base.white}Attempt {i + 1}: {base.yellow}Waiting for 15 seconds before checking reward...")
            # time.sleep(15)
        except Exception as e:
            base.log(f"{base.red}Attempt : Error occurred - {e}")
            return None

def ads_do_mission(token, proxies=None):
    target_missions = ["1005", "1006", "1008", "1009"]

    for mission_id in target_missions:
        base.log(f"{base.white}Mission {mission_id}: {base.yellow}Watching ads...")

        # 假设 ads() 函数是执行广告任务
        ads(token, proxies=proxies)

        time.sleep(15)

        url = "https://api.genkiminer.fun/api/v1/mission/checkMissionState"
        data = {
            "missionId": mission_id
        }

        try:
            base.log(f"{base.white}Checking mission state for mission ID: {mission_id}...")

            response = requests.post(
                url=url,
                headers=headers(token=token),
                data=data,
                proxies=proxies,
                timeout=20,
            )
            base.log(f"{base.white}Request completed with status code: {base.green}{response.status_code}")

            response.raise_for_status()

            data = response.json()
            base.log(f"{base.white}Mission state checked successfully.")

            # 如果只需要处理每个任务的数据而不终止循环，直接处理完一个任务后继续下一个任务
            base.log(f"{base.white}Completed mission {mission_id}.")
        except requests.exceptions.RequestException as req_err:
            base.log(f"{base.red}HTTP Request Error: {req_err}")
        except KeyError as key_err:
            base.log(f"{base.red}KeyError: Missing key in response - {key_err}")
        except Exception as e:
            base.log(f"{base.red}An unexpected error occurred: {e}")

        url = "https://api.genkiminer.fun/api/v1/mission/getMissionReward"
        data = {
            "missionId": mission_id
        }

        try:
            base.log(f"{base.white}Fetching reward for mission ID: {mission_id}...")

            response = requests.post(
                url=url,
                headers=headers(token=token),
                data=data,
                proxies=proxies,
                timeout=20,
            )
            base.log(f"{base.white}Request completed with status code: {base.green}{response.status_code}")

            response.raise_for_status()

            data = response.json()
            status = data["status"]
            base.log(f"{base.white}Reward fetched successfully. Status: {status}")

        except requests.exceptions.RequestException as req_err:
            base.log(f"{base.red}HTTP Request Error: {req_err}")
        except KeyError as key_err:
            base.log(f"{base.red}KeyError: Missing key in response - {key_err}")
        except Exception as e:
            base.log(f"{base.red}An unexpected error occurred: {e}")

    # 返回最终结果可以放到循环外部
    return None
