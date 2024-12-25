import sys
from smart_airdrop_claimer import base
from core.token import get_token
from core.itemdata import itemdata
from core.coin import coin
from core.mission import process_mission
from core.chest import chest
from core.spin import spin
from core.ads import ads_do_mission
import time
import json

sys.dont_write_bytecode = True


# # 冒泡排序
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):

class GenkiMinerBot():
    def __init__(self):
        # Get file directory
        self.data_file = base.file_path(file_name="data-proxy.json")
        self.config_file = base.file_path(file_name="config.json")
        # self.keyword_file = base.file_path(file_name="keyword.txt")

        # Initialize line
        self.line = base.create_line(length=50)

        # Initialize banner
        self.banner = base.create_banner(game_name="GenkiMinerBot")

        # Get config
        self.auto_chest = base.get_config(
            config_file=self.config_file, config_name="auto-chest"
        )

        self.auto_do_mission = base.get_config(
            config_file=self.config_file, config_name="auto-mission"
        )

        self.auto_spin = base.get_config(
            config_file=self.config_file, config_name="auto-spin"
        )

        self.auto_ads = base.get_config(
            config_file=self.config_file, config_name="auto-ads"
        )

        self.auto_coin = base.get_config(
            config_file=self.config_file, config_name="auto-coin"
        )
    def main(self):
        while True:
            base.clear_terminal()
            print(self.banner)
            accounts = json.load(open(self.data_file, "r"))["accounts"]
            num_acc = len(accounts)
            base.log(self.line)
            base.log(f"{base.green}Number of accounts: {base.white}{num_acc}")

            for no, account in enumerate(accounts):
                base.log(self.line)
                base.log(f"{base.green}Account number: {base.white}{no+1}/{num_acc}")
                data = account["acc_info"]
                proxy_info = account["proxy_info"]
                parsed_proxy_info = base.parse_proxy_info(proxy_info)
                if parsed_proxy_info is None:
                    break

                actual_ip = base.check_ip(proxy_info=proxy_info)

                proxies = base.format_proxy(proxy_info=proxy_info)

                try:
                    token = get_token(data=data)

                    if token:

                        itemdata(token=token)

                        # coin
                        if self.auto_coin:
                            base.log(f"{base.yellow}Auto Coin: {base.green}ON")
                            coin(token=token)
                        else:
                            base.log(f"{base.yellow}Auto Coin: {base.red}OFF")

                        # Chest
                        if self.auto_chest:
                            base.log(f"{base.yellow}Auto Chest: {base.green}ON")
                            chest(token=token)
                        else:
                            base.log(f"{base.yellow}Auto Chest: {base.red}OFF")

                        # Claim ref
                        if self.auto_spin:
                            base.log(f"{base.yellow}Auto spin: {base.green}ON")
                            spin(token=token)
                        else:
                            base.log(f"{base.yellow}Auto spin: {base.red}OFF")

                        # ads
                        if self.auto_ads:
                            base.log(f"{base.yellow}Auto ads: {base.green}ON")
                            ads_do_mission(token=token)
                        else:
                            base.log(f"{base.yellow}Auto ads: {base.red}OFF")


                        # Do mission
                        if self.auto_do_mission:
                            base.log(f"{base.yellow}Auto Do mission: {base.green}ON")
                            process_mission(token=token)
                        else:
                            base.log(f"{base.yellow}Auto Do mission: {base.red}OFF")


                    else:
                        base.log(f"{base.red}Token not found! Please get new query id")
                except Exception as e:
                    base.log(f"{base.red}Error: {base.white}{e}")


            print()
            wait_time = 0
            base.log(f"{base.yellow}Wait for {int(wait_time/60)} minutes!")
            time.sleep(wait_time)


if __name__ == "__main__":
    try:
        game = GenkiMinerBot()
        game.main()
    except KeyboardInterrupt:
        sys.exit()
