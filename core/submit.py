import requests
from core.headers import headers
import time
from smart_airdrop_claimer import base

def submit(token, proxies=None):
    url = "https://api.genkiminer.fun/api/v1/launchpool/submitAddress"
    data = {
        "address": "0x911232b427640ee49c27c03e9eddbc36627be916"
    }
    while True:
        try:
            response = requests.post(
                url=url, headers=headers(token), data=data, proxies=proxies, timeout=20
            )
            json_response = response.json()
            base.log(f"{base.white}Response: {json_response}")

            # Check the response status
            if json_response.get('status') == 200:  # Assuming 200 is the success status
                base.log(f"{base.white}Status: {base.green}200, {base.yellow}Exiting loop.")
                return json_response
            else:
                base.log(f"{base.white}Status: {base.red}{json_response.get('status')}, {base.yellow}Retrying...")

        except (requests.exceptions.RequestException, ValueError) as e:
            base.log(f"{base.white}Error: {base.red}An error occurred: {e}")

        # Set delay to avoid frequent requests
        time.sleep(2)