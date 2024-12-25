import requests
from smart_airdrop_claimer import base
from core.headers import headers


def chest(token, proxies=None):
    """
    自动处理箱子任务，包括创建订单、等待处理、检查奖励，同时记录详细日志。

    Args:
        token (str): 用户的令牌。
        proxies (dict, optional): 请求代理。
    """
    for i in range(10):
        try:
            # Step 1: 创建订单
            base.log(f"{base.white}Attempt {i + 1}: {base.yellow}Creating order...")
            url = "https://api.genkiminer.fun/api/v1/shop/createOrder"
            data = {
                "payType": "1",
                "shopItemId": "100"
            }
            response = requests.post(
                url=url, headers=headers(token=token), data=data, proxies=proxies, timeout=20
            )
            if response.status_code == 200:
                order_id = response.json()["data"]["id"]
                base.log(f"{base.white}Order created successfully: {base.green}Order ID {order_id}")
            else:
                base.log(f"{base.white}Order creation failed: {base.red}{response.text}")
                continue

            # Step 2: 获取玩家 Tick
            base.log(f"{base.white}Attempt {i + 1}: {base.yellow}Fetching player tick...")
            url = "https://api.genkiminer.fun/api/v1/player/getTick"
            response = requests.get(url, headers=headers(token=token), proxies=proxies, timeout=20)
            if response.status_code == 200:
                base.log(f"{base.white}Player tick fetched: {base.green}{response.json()}")
            else:
                base.log(f"{base.white}Failed to fetch player tick: {base.red}{response.text}")
                continue

            # # 等待 15 秒
            # base.log(f"{base.white}Attempt {i + 1}: {base.yellow}Waiting for 15 seconds before checking reward...")
            # time.sleep(15)

            # Step 3: 检查奖励
            base.log(f"{base.white}Attempt {i + 1}: {base.yellow}Checking reward for Order ID {order_id}...")
            url = "https://api.genkiminer.fun/api/v1/shop/checkOrderReward"
            data = {"orderId": order_id}
            response = requests.post(url, headers=headers(token=token), data=data, proxies=proxies, timeout=20)
            if response.status_code == 200:
                reward_response = response.json()
                base.log(f"{base.white}Reward checked successfully: {base.green}{reward_response}")
            else:
                base.log(f"{base.white}Failed to check reward: {base.red}{response.text}")
        except Exception as e:
            base.log(f"{base.red}Attempt {i + 1}: Error occurred - {e}")
