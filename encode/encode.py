import urllib.parse
from DrissionPage import Chromium

browser = Chromium()


with open("data.txt", "r") as f:
    for line in f:
        # print(repr(line))  # 使用 repr() 可以显示换行符和空格
        encoded_string = line.strip()
        double_encoded_string = urllib.parse.quote(encoded_string)
        print(double_encoded_string)
        new_tab = browser.new_tab()  # 创建新的标签页
        new_tab.get('https://game.genkiminer.fun/#tgWebAppData=' + double_encoded_string)



