import requests

from smart_airdrop_claimer import base
from core.headers import headers


def itemdata(token, proxies=None):
    """
    获取玩家物品数据并记录日志。

    Args:
        token (str): 用户的令牌。
        proxies (dict, optional): 请求代理。

    Returns:
        dict: 物品及其数量的映射，如果发生错误则返回 None。
    """
    url = "https://api.genkiminer.fun/api/v1/player/itemData"

    try:
        base.log(f"{base.white}Fetching player item data...")

        # 发起 GET 请求
        response = requests.get(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        base.log(f"{base.white}Request completed with status code: {base.green}{response.status_code}")

        # 如果响应不是 200，抛出异常
        response.raise_for_status()

        # 解析响应 JSON
        base.log(f"{base.white}Response successfully parsed.")
        items = response.json()["data"]["items"]

        # 定义键与物品名称的对应关系（带索引 item"1", item"2" ...）
        for item in items.values():
            item_id = item["itemId"]
            count = item["count"]

            # 通过条件判断映射 itemId
            if item_id == 20007:
                name = "加密币"
            elif item_id == 20000:
                name = "挖矿次数"
            elif item_id == 20001:
                name = "金币"
            elif item_id == 20002:
                name = "钥匙"
            elif item_id == 20005:
                name = "钻石"
            else:
                name = f"货币({item_id})"

            base.log(f"{base.blue}{name}: {count}")

        return items
    except requests.exceptions.RequestException as req_err:
        base.log(f"{base.red}HTTP Request Error: {req_err}")
    except KeyError as key_err:
        base.log(f"{base.red}KeyError: Missing key in response - {key_err}")
    except Exception as e:
        base.log(f"{base.red}An unexpected error occurred: {e}")
    return None
