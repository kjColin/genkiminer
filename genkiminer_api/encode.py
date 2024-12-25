import urllib.parse
from DrissionPage import Chromium

browser = Chromium()

# 初始化计数器
count = 0
tabs = []  # 用于存储打开的标签页

with open("data.txt", "r") as f:
    for line in f:
        encoded_string = line.strip()
        double_encoded_string = urllib.parse.quote(encoded_string)
        print(double_encoded_string)

        # 每20个打开一个新的窗口
        if count % 20 == 0:
            # 如果已有标签页，关闭它们
            for tab in tabs:
                tab.close()
            tabs.clear()  # 清空标签页列表

            new_browser = Chromium()  # 创建新的模拟器窗口
            new_tab = new_browser.new_tab()
            tabs.append(new_tab)  # 存储新的标签页
        else:
            new_tab = browser.new_tab()  # 使用现有的浏览器实例
            tabs.append(new_tab)  # 存储新打开的标签页

        new_tab.get('https://game.genkiminer.fun/#tgWebAppData=' + double_encoded_string)

        # 递增计数器
        count += 1

        # 每20个条目后等待用户输入
        if count % 20 == 0:
            print(f"已打开第{count-19} 到 第{count} 个账号")
            input("挖矿完成后，按 Enter 键继续...程序自动关闭所有标签页，进行之后20个号码")

