from smart_airdrop_claimer import base
from core.headers import headers

import requests


def get_mission(token, proxies=None):
    url = "https://api.genkiminer.fun/api/v1/mission/missionData"
    try:
        base.log(f"{base.white}Fetching mission data...")

        response = requests.get(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        base.log(f"{base.white}Request completed with status code: {base.green}{response.status_code}")

        # 检查响应是否正常
        response.raise_for_status()

        data = response.json()
        base.log(f"{base.white}Response successfully parsed.")

        # 提取任务状态
        missions_data = data['data']['missions']
        mission_status = {mission_id: mission_info['status'] for mission_id, mission_info in missions_data.items()}

        base.log(f"{base.white}Mission statuses fetched: {mission_status}")

        return mission_status
    except requests.exceptions.RequestException as req_err:
        base.log(f"{base.red}HTTP Request Error: {req_err}")
    except KeyError as key_err:
        base.log(f"{base.red}KeyError: Missing key in response - {key_err}")
    except Exception as e:
        base.log(f"{base.red}An unexpected error occurred: {e}")
    return None


def check_mission(token, mission_id, proxies=None):
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

        return data
    except requests.exceptions.RequestException as req_err:
        base.log(f"{base.red}HTTP Request Error: {req_err}")
    except KeyError as key_err:
        base.log(f"{base.red}KeyError: Missing key in response - {key_err}")
    except Exception as e:
        base.log(f"{base.red}An unexpected error occurred: {e}")
    return None


def get_reward(token, mission_id, proxies=None):
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

        return status
    except requests.exceptions.RequestException as req_err:
        base.log(f"{base.red}HTTP Request Error: {req_err}")
    except KeyError as key_err:
        base.log(f"{base.red}KeyError: Missing key in response - {key_err}")
    except Exception as e:
        base.log(f"{base.red}An unexpected error occurred: {e}")
    return None


def do_mission(token, mission_status, proxies=None):
    """
    遍历任务并根据状态处理，同时记录详细日志。
    - 状态 0：跳过，任务已完成。
    - 状态 1：执行 check_mission 并记录状态更新日志。
    - 状态 2：执行 get_reward 并记录状态更新日志。

    Args:
        token (str): 用户的令牌。
        mission_status (dict): 每个任务的状态信息，格式为 {mission_id: status}。
        proxies (dict, optional): 请求代理。
    """
    for mission_id, status in mission_status.items():
        if status == 0:
            # 已完成
            base.log(f"{base.white}Mission {mission_id}: {base.green}Already Completed")
            continue

        elif status == 1:
            # 检查任务状态
            base.log(f"{base.white}Mission {mission_id}: {base.yellow}Checking mission status...")
            check_result = check_mission(token, mission_id, proxies=proxies)

            if check_result and check_result.get("status") == 2:
                # 状态成功更新为 2
                base.log(f"{base.white}Mission {mission_id}: {base.green}Check success, ready to claim reward")
                status = 2
            else:
                base.log(f"{base.white}Mission {mission_id}: {base.red}Check failed or status not updated")
                continue
    process_reward(token, mission_status, proxies=proxies)
    return None

def process_reward(token, mission_status, proxies=None):
    for mission_id, status in mission_status.items():
        if status == 0:
            # 已完成
            base.log(f"{base.white}Mission {mission_id}: {base.green}Already Completed Twice")
            continue

        elif status == 1:
            # 检查任务状态
            base.log(f"{base.white}Mission {mission_id}: {base.yellow}Checking mission status Twice...")
            check_result = check_mission(token, mission_id, proxies=proxies)

            if check_result and check_result.get("status") == 2:
                # 状态成功更新为 2
                base.log(f"{base.white}Mission {mission_id}: {base.green}Check success, ready to claim reward Twice")
                status = 2
            else:
                base.log(f"{base.white}Mission {mission_id}: {base.red}Check failed or status not updated Twice")
                continue
        elif status == 2:
            # 获取奖励
            base.log(f"{base.white}Mission {mission_id}: {base.yellow}Claiming reward...")
            reward_result = get_reward(token, mission_id, proxies=proxies)

            if reward_result == 0:
                base.log(f"{base.white}Mission {mission_id}: {base.green}Reward claimed successfully")
            else:
                base.log(f"{base.white}Mission {mission_id}: {base.red}Failed to claim reward")
                continue
    return None


def process_mission(token,proxies=None):

    mission_status = get_mission(token)

    if mission_status:
        do_mission(token, mission_status)
    else:
        base.log(f"{base.red}Failed to retrieve mission status")

