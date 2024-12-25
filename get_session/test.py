import csv
import re
import json
import time
import urllib.parse
from DrissionPage._base.chromium import Chromium
from lxml import etree
import requests

def get_session(tab):
    tab.get('https://t.me/GenkiminerBot')
    i = 0
    while True:
        if tab.ele('@text()=Open in Web', timeout=4):
            tab.ele('@text()=Open in Web').click('js')
            time.sleep(20)
        res = tab.ele('@text()=Launch Blum', timeout=1) or tab.ele('@text()=START', timeout=1)
        if res:
            print('进入小程序')
            break
        else:
            tab.get('https://t.me/GenkiminerBot')

        # if tab.ele('@text()=Preview channel',timeout=2):
        #     tab.ele('@text()=Preview channel').click('js')

        # if tab.ele('@text()=Start Bot',timeout=2):
        #     tab.ele('@text()=Start Bot').click('js')
        i = i + 1
        if i > 3:
            print('没能打开频道')
            return False
    j = 0
    while True:
        # if tab.ele('@text()=START', timeout=1):
        #     tab.ele('@text()=START').click()
        #     time.sleep(1)
        res = tab.ele('.bot-menu-text')
        if res:
            res.click()
        # res = tab.ele('.Button tiny primary has-ripple')
        # if res:
        #     res.click()
            print('点击开始游戏')
        if tab.ele('@text()=Confirm', timeout=1):
            tab.ele('@text()=Confirm').click()
            print('confirmed')
            time.sleep(5)
        if tab.ele('@@class=i18n@@text()=Launch', timeout=1):
            tab.ele('@@class=i18n@@text()=Launch').click()
            print('打开小游戏')
            time.sleep(5)
        for _ in range(5):
            try:
                iframe = tab.get_frame('t:iframe', timeout=1)
                if iframe:
                    print('成功获取iframe')
                    encode(iframe)
                    return True

            except Exception as e:
                print(f"尝试获取 iframe 失败: {e}")
                time.sleep(1)
        j = j + 1
        if j > 3:
            print('没能打开iframe')
            return False
def encode(iframe):
    html = iframe.html
    # print(html)
    match = re.search(r'src="([^"]+)"', html)
    if match:
        src = match.group(1)
        # print(src)
        # with open('../src.csv', 'a+', newline='', encoding='utf-8') as f:
        #     writer = csv.writer(f)
        #     writer.writerow([src])
        match = re.search(r'https://game\.genkiminer\.fun/#tgWebAppData=(.*?)(&amp;tgWebAppPlatform=|&amp;tgWebAppVersion=|$)', src)
        if match:
            session_data = match.group(1)  # 提取匹配的组
            # print(session_data)  # 输出匹配的组
            session = urllib.parse.unquote(session_data)  # 解码
            print(session)  # 输出解码后的字符串
            with open('session.csv', 'a+', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([session])
                return True
        else:
            print('解密session失败')
            return False
    else:
        print('提取iframe失败')
        return False
if __name__ == '__main__':
    browser = Chromium()
    tab = browser.latest_tab
    get_session(tab)