from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import subprocess
class WebInterface:
    driver = None
    @staticmethod
    def browser_start():
        # PowerShellコマンドを使用してChromeブラウザを起動 selenium専用のプロファイルで起動
        ps_cmd = r'& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\newmi\AppData\Local\Google\Chrome\Selenium" --profile-directory="Default" --no-sandbox --remote-allow-origins=*'
        cmd = subprocess.run(["powershell", "-Command", ps_cmd])
    @staticmethod
    def connect():
        # 既存のChromeブラウザに接続するための設定
        WebInterface.browser_start()
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        WebInterface.driver = webdriver.Chrome(options=chrome_options)
        print("Chromeドライバーに接続しています...")
        try:
            # WebDriverを初期化
            print("Chromeドライバーに接続成功")
        except Exception as e:
            print(f"Chromeドライバーへの接続に失敗しました: {e}")
            exit(1)
    @staticmethod
    def get_driver():
        return WebInterface.driver
    