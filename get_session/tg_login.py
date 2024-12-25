import csv
import re
import json
import time
import urllib.parse
from DrissionPage._base.chromium import Chromium
from lxml import etree
import requests
def VerifyCode(url):
    headers = {

        "^upgrade-insecure-requests": "1^",
        "^Referer": "https://ludamao.net/^",
        "^User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36^",
        "^referer": "https://ludamao.net/^",
        "^Origin": "https://ludamao.net^"
    }
    response = requests.get(url, headers=headers)
    html = response.text
    verify_code_elements = re.findall(r'<td id="code">(.*?)</td>', html)
    if len(verify_code_elements) > 0:
        verify_code = verify_code_elements[0]
        print(f"获取验证码成功:{verify_code}")
        return verify_code
    else:
        print("获取验证码失败")
        with open('../Error.csv', 'a+', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([url])
        return None

def Sign_Telegram(phone, VerifyLink,telegram_tab):
    telegram_tab.get('https://web.telegram.org/')
    # 判断网络可用性,超时返回False
    for _ in range(1, 5):
        if _ == 4:
            print('登录超时')
            return False
        res = telegram_tab.ele('@text()=Log in by phone Number')
        if res:
            res.click()  # LOG IN BY PHONE NUMBER,有时候会点击失败
            time.sleep(2)
            print('LOG IN BY PHONE NUMBER')
            if telegram_tab.ele('@text()=Log in by QR Code'):
                break
            else:
                print('没有进入手机号登录界面')
                continue
        else:
            print('点击失败')
            continue
    i = 0
    while True:
        try:
            telegram_tab.ele('@id=sign-in-phone-number').input(phone,clear=True)  # 需要确定国家，按照此方法需输入两次
            time.sleep(1)
            # telegram_tab.ele('@id=sign-in-phone-number').input(phone.replace('+86', ''))
            # time.sleep(1)  #
            telegram_tab.ele(locator='Next').click()
            print('输入号码成功，下一步')
            break
        except Exception as e:
            print('登录无效，正在重新点击', e)
        i = i + 1
        if i > 3:
            return False
    i = 0
    while True:
        try:
            # if telegram_tab.ele(locator='Too many attempts. Try again in 3 hours', timeout=1):
            #     print('尝试太多了，请在三小时后重试')
            #     return False
            # if telegram_tab.ele(locator='FLOOD_WAIT', timeout=1):
            #     print('封号什么什么什么的')
            #     return False
            # if telegram_tab.ele(locator='PHONE_NUMBER_BANNED', timeout=1):
            #     print('账号被封禁')
            #     return False
            # if telegram_tab.ele(locator='This phone number is banned.', timeout=1):
            #     print('当前账号无效')
            #     return False
            # if telegram_tab.ele(locator='Incorrect password.', timeout=1):
            #     return False
            if telegram_tab.ele('@id=sign-in-code', timeout=10):
                code = VerifyCode(VerifyLink)
                print(f"验证码:{code}")
                if code != None and code != False:
                    telegram_tab.ele('@id=sign-in-code',
                                     timeout=20).input(code, clear=True)  # 输入验证码
                if code == False:
                    print('接码平台反馈无效')
                    return False
            if telegram_tab.ele(locator='Your account is protected with'):
                telegram_tab.ele('xpath://*[@id="auth-pages"]/div/div[2]/div[5]/div/div[2]/div/input[2]').input(
                    'Zpaily88', clear=True)  # 输入密码并点击
            if telegram_tab.ele(locator='Next', timeout=2):
                telegram_tab.ele(locator='Next').click()  # Next

            if telegram_tab.ele('@id=telegram-search-input',
                                timeout=20):  # 如果定位到主页元素
                break
            else:
                telegram_tab.refresh()
        except Exception as e:
            print(e)
        i = i + 1
        if i > 3:
            return False

    print("电报登陆成功")
    return True
browser = Chromium()
telegram_tab = browser.latest_tab
Sign_Telegram('+8615802355675', 'https://ludamao.net/tg_verify_code.html',telegram_tab)