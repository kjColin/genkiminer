import urllib.parse
from DrissionPage import Chromium
import json
import time
import configparser
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog, simpledialog

# 配置文件管理
def load_config():
    config = configparser.ConfigParser()
    default_settings = {
        'base_url': 'https://game.genkiminer.fun/#tgWebAppData=',
        'delay': '2',
        'auto_close': 'true',
        'max_windows': '20',
        'batch_size': '5',
        'user_name': '',
        'user_url': ''
    }
    
    if os.path.exists('config.ini'):
        config.read('config.ini')
        # 检查并添加缺失的配置项
        if 'Settings' not in config:
            config['Settings'] = {}
        for key, value in default_settings.items():
            if key not in config['Settings']:
                config['Settings'][key] = value
        # 保存更新后的配置
        with open('config.ini', 'w') as f:
            config.write(f)
    else:
        config['Settings'] = default_settings
        with open('config.ini', 'w') as f:
            config.write(f)
    
    return config

def save_config(config):
    with open('config.ini', 'w') as f:
        config.write(f)

# 浏览器管理类
class BrowserManager:
    def __init__(self):
        self.active_browsers = []
        self.config = load_config()

    def open_browser(self, url):
        try:
            max_windows = int(self.config['Settings']['max_windows'])
            if len(self.active_browsers) >= max_windows:
                self.close_old_browsers(keep_last=max_windows-1)
            
            # 使用选项创建浏览器实例
            browser = Chromium()
            tab = browser.new_tab()
            # 直接在主页面打开URL
            tab.get(url)
            # # 等待加载完成
            # tab.wait.load_complete()
            
            self.active_browsers.append(browser)
            return browser
            
        except Exception as e:
            raise Exception(f"Failed to open browser: {str(e)}")
    
    def close_old_browsers(self, keep_last=1):
        try:
            while len(self.active_browsers) > keep_last:
                browser = self.active_browsers.pop(0)
                try:
                    browser.quit()
                except:
                    pass  # 忽略关闭失败的错误
        except Exception as e:
            print(f"Error closing browsers: {e}")

# GUI类
class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("账号管理器")
        self.root.geometry("600x400")
        self.config = load_config()
        self.browser_manager = BrowserManager()
        self.accounts = []
        self.setup_ui()
        self.load_accounts()
        
        # Add checkbox for auto_close setting
        self.auto_close_var = tk.BooleanVar(value=self.config['Settings'].getboolean('auto_close'))
        self.auto_close_check = ttk.Checkbutton(
            self.root, text="自动关闭旧浏览器", variable=self.auto_close_var, command=self.toggle_auto_close
        )
        self.auto_close_check.pack(pady=5)
        
        # 添加高级设置框架
        self.setup_advanced_settings()

    def setup_ui(self):
        # 创建主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建账号列表
        columns = ("序号", "账号")
        self.account_list = ttk.Treeview(main_frame, columns=columns, show="headings")
        for col in columns:
            self.account_list.heading(col, text=col)
        self.account_list.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # 添加滚动条
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.account_list.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.account_list.configure(yscrollcommand=scrollbar.set)
        
        # 按钮框架
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=5)
        
        # 控制按钮
        ttk.Button(button_frame, text="打开选中账号", command=self.open_selected).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="导出账号", command=self.export_accounts).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="刷新列表", command=self.load_accounts).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="打开后10个账号", command=self.open_next_10).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="打开指定账号", command=self.open_specific).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="打开所有账号", command=self.open_all_accounts).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="设置延迟", command=self.set_delay).pack(side=tk.LEFT, padx=5)

        # 在主框架中添加状态标签
        self.status_label = ttk.Label(self.root, text="")
        self.status_label.pack(fill=tk.X, pady=5)

    def setup_advanced_settings(self):
        settings_frame = ttk.LabelFrame(self.root, text="高级设置", padding="5")
        settings_frame.pack(fill=tk.X, padx=10, pady=5)

        # 最大窗口数量设置
        ttk.Label(settings_frame, text="最大窗口数:").grid(row=0, column=0, padx=5)
        self.max_windows_var = tk.StringVar(value=self.config['Settings']['max_windows'])
        max_windows_entry = ttk.Entry(settings_frame, textvariable=self.max_windows_var, width=10)
        max_windows_entry.grid(row=0, column=1, padx=5)

        # 批量打开数量设置
        ttk.Label(settings_frame, text="批量打开数:").grid(row=0, column=2, padx=5)
        self.batch_size_var = tk.StringVar(value=self.config['Settings']['batch_size'])
        batch_size_entry = ttk.Entry(settings_frame, textvariable=self.batch_size_var, width=10)
        batch_size_entry.grid(row=0, column=3, padx=5)

        # 保存设置按钮
        ttk.Button(settings_frame, text="保存设置", command=self.save_advanced_settings).grid(row=0, column=4, padx=5)

    def save_advanced_settings(self):
        try:
            self.config['Settings']['max_windows'] = self.max_windows_var.get()
            self.config['Settings']['batch_size'] = self.batch_size_var.get()
            save_config(self.config)
            messagebox.showinfo("成功", "设置已保存")
        except Exception as e:
            messagebox.showerror("错误", f"保存设置失败: {str(e)}")

    def load_accounts(self):
        try:
            self.account_list.delete(*self.account_list.get_children())
            self.accounts = []
            with open("data.txt", "r") as f:
                for i, line in enumerate(f, 1):
                    encoded = urllib.parse.quote(line.strip())
                    self.accounts.append(encoded)
                    self.account_list.insert("", "end", values=(i, encoded[:50] + "..."))
        except FileNotFoundError:
            messagebox.showerror("错误", "未找到 data.txt 文件")
        
    def open_selected(self):
        selection = self.account_list.selection()
        if not selection:
            messagebox.showwarning("提示", "请先选择一个账号")
            return
            
        index = self.account_list.index(selection[0])
        try:
            if self.auto_close_var.get():
                self.browser_manager.close_old_browsers(
                    keep_last=int(self.config['Settings']['max_windows'])-1
                )
            
            browser = self.browser_manager.open_browser(
                self.config['Settings']['base_url'] + self.accounts[index]
            )
            self.status_label.config(text=f"正在打开第 {index + 1} 个账号的页面")
            self.root.update_idletasks()
            time.sleep(float(self.config['Settings']['delay']))
            
        except Exception as e:
            messagebox.showerror("错误", f"打开浏览器失败: {str(e)}")
        
    def export_accounts(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            try:
                with open(filename, 'w') as f:
                    for account in self.accounts:
                        f.write(f"{account}\n")
                messagebox.showinfo("成功", "账号已成功导出")
            except Exception as e:
                messagebox.showerror("错误", f"导出失败: {str(e)}")

    def open_next_10(self):
        current_selection = self.account_list.selection()
        start_index = self.account_list.index(current_selection[-1]) + 1 if current_selection else 0
        end_index = min(start_index + 10, len(self.accounts))

        for index in range(start_index, end_index):
            try:
                if self.auto_close_var.get():
                    self.browser_manager.close_old_browsers(
                        keep_last=int(self.config['Settings']['max_windows'])-1
                    )
                # 显示正在打开的账号
                account_number = index + 1
                self.status_label.config(text=f"正在打开第 {account_number} 个账号的页面")
                self.root.update_idletasks()
                browser = self.browser_manager.open_browser(
                    self.config['Settings']['base_url'] + self.accounts[index]
                )
                time.sleep(float(self.config['Settings']['delay']))
            except Exception as e:
                messagebox.showerror("错误", f"打开浏览器失败: {str(e)}")

        self.status_label.config(text="已完成打开后10个账号")
        messagebox.showinfo("提示", f"已打开账号 {start_index + 1} 到 {end_index} 的页面")

    def open_specific(self):
        line_number = simpledialog.askinteger("输入账号行号", f"请输入要打开的账号行号（1 到 {len(self.accounts)}）:")
        if line_number and 1 <= line_number <= len(self.accounts):
            try:
                if self.auto_close_var.get():
                    self.browser_manager.close_old_browsers(
                        keep_last=int(self.config['Settings']['max_windows'])-1
                    )
                browser = self.browser_manager.open_browser(
                    self.config['Settings']['base_url'] + self.accounts[line_number - 1]
                )
                time.sleep(float(self.config['Settings']['delay']))
                messagebox.showinfo("提示", f"已打开第 {line_number} 个账号的页面")
            except Exception as e:
                messagebox.showerror("错误", f"打开浏览器失败: {str(e)}")
        else:
            messagebox.showwarning("提示", "请输入有效的账号行号")

    def open_all_accounts(self):
        for index in range(len(self.accounts)):
            try:
                if self.auto_close_var.get():
                    self.browser_manager.close_old_browsers(
                        keep_last=int(self.config['Settings']['max_windows'])-1
                    )
                browser = self.browser_manager.open_browser(
                    self.config['Settings']['base_url'] + self.accounts[index]
                )
                time.sleep(float(self.config['Settings']['delay']))
            except Exception as e:
                messagebox.showerror("错误", f"打开浏览器失败: {str(e)}")
        messagebox.showinfo("提示", "已打开所有账号的页面")

    def set_delay(self):
        delay = simpledialog.askfloat("设置延迟", "请输入每个账号之间的延迟（秒）:", initialvalue=self.config['Settings'].getfloat('delay'))
        if delay is not None:
            self.config['Settings']['delay'] = str(delay)
            save_config(self.config)
            messagebox.showinfo("提示", f"延迟已设置为 {delay} 秒")
        else:
            messagebox.showwarning("提示", "未修改延迟")

    def toggle_auto_close(self):
        self.config['Settings']['auto_close'] = str(self.auto_close_var.get())
        save_config(self.config)

if __name__ == "__main__":
    try:
        app = MainWindow()
        app.root.mainloop()
    except Exception as e:
        print(f"Failed to start GUI: {e}")
