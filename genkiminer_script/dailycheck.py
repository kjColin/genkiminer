from ascript.android import action
# from ascript.android import action.Hid
from ascript.android.node import Selector
import time
from ascript.android import system
from ascript.android.system import R

def sign_in():
    print(f'signin--')
    # 打开登录页面
    action.click(540, 1600)
    res = Selector(1).desc("Web tabs GenkiMinerBot").find()
    if res is not None:
        res.click()
        time.sleep(1)
        print('返回主页面')
    else:
        print('没有找到主页面')
    time.sleep(10)
    action.click(540, 1600)
    print('next')
    time.sleep(1)
    action.click(540, 1600)
    print('next')
    time.sleep(1)
    action.click(540, 1090)
    time.sleep(1)
    action.click(540, 1600)
    print('next')
    time.sleep(1)
    action.click(950, 1090)
    print('skip')
    time.sleep(1)
    action.click(540, 1650)
    print('earn')
    action.click(950, 1090)
    print('skip')
    time.sleep(1)
    action.click(540, 1650)
    print('earn')


def bot():
    print(f'bot--')
    jc = 0  # 初始化搜索计数器
    while True:
        # 检查超时
        if jc > 60:
            print("wallet_bot操作超时")
            # main()
            return
        res = Selector().text("I agree to the Terms of Use").type("CheckBox").find()
        if res is not None:
            res.click()
            print("agreed")

        res = Selector().text("START").type("TextView").clickable(True).find()
        if res is not None:
            res.click()
            time.sleep(1)
            print('start')
        res = Selector().text("Message").type("EditText").find()
        url = 'https://t.me/GenkiMinerBot/GenkiMiner?startapp=IYeI58x5t'
        if res:
            res.input(url)
            time.sleep(1)
            print('input url')
        else:
            print('没有找到输入框')
        res = Selector().desc("Send").find()
        if res:
            res.click()
            time.sleep(1)
            print('send')
        else:
            print('没有找到发送按钮')
        res = Selector().desc("Bot menu").parent(1).brother(-0.1).child(-1).find()
        if res :
            res.click(res.rect.centerX(), res.rect.centerY())
            time.sleep(10)
            print('bot menu')
            sign_in()
            return
        else:
            print('没有找到bot menu')


        res = Selector().text("Open Wallet").type("Button").find()
        if res is not None:
            res.click()
            time.sleep(1)
            print('open wallet')
            time.sleep(10)


def search_task():
    print(f'search_task--')
    search_text = 'GenkiMinerBot'
    jc = 0
    while True:
        if jc > 60:
            print(f'搜索超时')
            # 调用个主函数

            return
        time.sleep(10)
        res = Selector().text("Remind me later").brother(-0.1).find()
        if res is not None:
            res.click()
            time.sleep(0.5)

        res = Selector().desc("Search").type("ImageButton").clickable(True).find()
        if res is not None:
            print(f'可以开始搜索')
            res.click()
            time.sleep(0.5)

        res = Selector().text("Search").type("EditText").clickable(True).find()
        if res is not None:
            res.input(search_text)
            time.sleep(0.5)

        print('开始等待搜索结果...')
        timeout = 60  # 设置超时时间为60秒
        elapsed_time = 0  # 经过的时间
        check_interval = 1  # 每次检查间隔为1秒
        while elapsed_time < timeout:
            res = Selector().text("Global search").type("TextView").find()
            if res:  # 检查res_list是否非空
                print(f'搜索成功')
                break
            else:  # 如果res_list为空，则等待一段时间再检查
                time.sleep(check_interval)  # 等待一段时间再检查
                elapsed_time += check_interval  # 增加经过的时间

        res_list = Selector().text('GenkiMinerBot').type("ViewGroup").clickable(False).find_all()
        for i in res_list:
            if len(i.text) == 29:
                print(f'找到结果：{i.text}')
                res = i
                time.sleep(0.5)
                action.click(res.rect.centerX(), res.rect.centerY())
                time.sleep(10)
                # bot()
                return
        print(f'未找到结果')
        time.sleep(0.5)
        jc += 1
def login_account():
    print(f'login_account--')
    system.open('org.telegram.messenger.web')
    time.sleep(1)
    res = Selector().text("Not now").type("TextView").find()
    if res:
        res.click()
        time.sleep(0.5)
    else:
        print(f'没有弹出提示')
    res = Selector().text("拒绝").type("Button").clickable(True).find()
    if res is not None:
        print(f'点击拒绝')
        action.click(res.rect.centerX(), res.rect.centerY())
        time.sleep(0.5)
    else:
        print(f'没有拒绝按钮')
        search_task()
        return
def main():
    login_account()
