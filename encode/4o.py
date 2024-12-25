import urllib.parse
from DrissionPage import Chromium
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize counter and accounts list
count = 0
accounts = []

def read_file(file_path):
    try:
        with open(file_path, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        sys.exit(1)

def encode_lines(lines):
    encoded_accounts = []
    for line_number, line in enumerate(lines, start=1):
        encoded_string = line.strip()
        double_encoded_string = urllib.parse.quote(encoded_string)
        encoded_accounts.append(double_encoded_string)
        logging.info(f"第{line_number}个的账号地址: {double_encoded_string}")
    return encoded_accounts

def open_browser(url):
    try:
        browser = Chromium()
        tab = browser.new_tab()
        tab.get(url)
        return browser
    except Exception as e:
        logging.error(f"Error opening browser: {e}")
        return None

def main():
    global count, accounts
    file_path = "data.txt"
    base_url = 'https://game.genkiminer.fun/#tgWebAppData='

    lines = read_file(file_path)
    accounts = encode_lines(lines)

    while True:
        count += 1
        if count > len(accounts):
            logging.info("All accounts processed.")
            break

        while True:
            line_to_open = input(f"按 Enter 键继续下一个账号，或输入要打开的行号（1 到 {count}），输入 'exit' 退出: ")

            if line_to_open.lower() == 'exit':
                logging.info("程序已退出。")
                sys.exit(0)

            if line_to_open == '':
                browser = open_browser(base_url + accounts[count - 1])
                if browser:
                    logging.info(f"已打开第{count}个账号的页面")
                break
            else:
                try:
                    line_number_input = int(line_to_open)
                    if 1 <= line_number_input <= count:
                        browser = open_browser(base_url + accounts[line_number_input - 1])
                        if browser:
                            logging.info(f"已打开第{line_number_input}个账号的页面")
                        break
                    else:
                        logging.warning(f"请输入有效的账号号（1 到 {count}）")
                except ValueError:
                    logging.warning("请输入有效的账号号或 'exit' 退出")

if __name__ == "__main__":
    main()
