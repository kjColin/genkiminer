import sys
from smart_airdrop_claimer import base
from core.token import get_token
from core.itemdata import itemdata
from core.coin import coin
from core.mission import process_mission
from core.chest import chest
from core.spin import spin
from core.ads import ads_do_mission
from core.submit import submit
import time

sys.dont_write_bytecode = True


class GenkiMinerBot():
    def __init__(self):
        # Get file directory
        self.data_file = base.file_path(file_name="data.txt")
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
        self.auto_coin = base.get_config(
            config_file=self.config_file, config_name="auto-submit"
        )
    def main(self):
        while True:
            base.clear_terminal()
            print(self.banner)
            data = open(self.data_file, "r").read().splitlines()
            num_acc = len(data)
            base.log(self.line)
            base.log(f"{base.green}Number of accounts: {base.white}{num_acc}")

            for no, data in enumerate(data):
                base.log(self.line)
                base.log(f"{base.green}Account number: {base.white}{no+1}/{num_acc}")

                try:
                    token = get_token(data=data)

                    if token:

                        itemdata(token=token)

                        # # coin
                        # if self.auto_coin:
                        #     base.log(f"{base.yellow}Auto Coin: {base.green}ON")
                        #     coin(token=token)
                        # else:
                        #     base.log(f"{base.yellow}Auto Coin: {base.red}OFF")

                        # # Chest
                        # if self.auto_chest:
                        #     base.log(f"{base.yellow}Auto Chest: {base.green}ON")
                        #     chest(token=token)
                        # else:
                        #     base.log(f"{base.yellow}Auto Chest: {base.red}OFF")

                        # # Claim ref
                        # if self.auto_spin:
                        #     base.log(f"{base.yellow}Auto spin: {base.green}ON")
                        #     spin(token=token)
                        # else:
                        #     base.log(f"{base.yellow}Auto spin: {base.red}OFF")

                        # # ads
                        # if self.auto_ads:
                        #     base.log(f"{base.yellow}Auto ads: {base.green}ON")
                        #     ads_do_mission(token=token)
                        # else:
                        #     base.log(f"{base.yellow}Auto ads: {base.red}OFF")


                        # # Do mission
                        # if self.auto_do_mission:
                        #     base.log(f"{base.yellow}Auto Do mission: {base.green}ON")
                        #     process_mission(token=token)
                        # else:
                        #     base.log(f"{base.yellow}Auto Do mission: {base.red}OFF")
                        
                        # Submit
                        if self.auto_do_mission:
                            base.log(f"{base.yellow}Auto submit: {base.green}ON")
                            submit(token=token)
                        else:
                            base.log(f"{base.yellow}Auto submit: {base.red}OFF")


                    else:
                        base.log(f"{base.red}Token not found! Please get new query id")
                except Exception as e:
                    base.log(f"{base.red}Error: {base.white}{e}")

            print()
            wait_time = 60*60
            base.log(f"{base.yellow}Wait for {int(wait_time/60)} minutes!")
            time.sleep(wait_time)


if __name__ == "__main__":
    try:
        game = GenkiMinerBot()
        game.main()
    except KeyboardInterrupt:
        sys.exit()
