from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
# webInterface.py はユーザーのカスタムモジュールと仮定
from webInterface import WebInterface 
# ↓↓↓ エラー処理が変更になるため、これもインポート ↓↓↓
from selenium.common.exceptions import NoSuchElementException, TimeoutException
class SoraVideo:
    def __init__(self, description, duration=10, orientation_type="landscape", image_url=""):
        self.driver = WebInterface.get_driver()
        self.orientation_type = orientation_type
        self.duration = duration
        self.description = description
        self.image_url = image_url
    def create_video(self):
        url = "https://sora.chatgpt.com/profile/"
        self.driver.get(url)
        time.sleep(3)
        # ここに動画作成のためのSoraの操作コードを追加
        print("Soraでの動画作成処理開始")
        # 例: 説明文の入力
        description_textarea = self.driver.find_element(By.CSS_SELECTOR, "textarea")
        description_textarea.send_keys(self.description)
        self._select_orientation()
        self._select_duration()
        self._select_image()
        # 例: 動画作成ボタンのクリック
        time.sleep(2)
        create_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-state='closed'][data-disabled='false']")
        create_button.click()
        print("動画作成ボタンをクリックしました。動画が生成されるまでお待ちください...")
    def save_video_latest(self):
        url = "https://sora.chatgpt.com/drafts"
        self.driver.get(url)
        time.sleep(5)
        video_latest = self.driver.find_elements(By.CSS_SELECTOR, "video")[0]
        src = video_latest.get_attribute("src")

        time.sleep(2)
        # ---- 動画をダウンロード ----
        file_name = "latest_video.mp4"
        print("Downloading video...")

        response = requests.get(src, stream=True)
        response.raise_for_status()

        with open(file_name, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"✅ 動画を保存しました: {file_name}")

    def save_video():
        pass
    def _select_image(self):
        if not self.image_url:
            return
        file_uploader_input = self.driver.find_elements(By.CSS_SELECTOR, "input[type='file']")[1]
        file_uploader_input.send_keys(self.image_url)
        time.sleep(2)

    def _select_orientation(self):
        setting_button = self.driver.find_elements(By.CSS_SELECTOR, "button[aria-label='Settings']")[1]
        setting_button.click()
        time.sleep(1)
        orientation_tab = self.driver.find_elements(By.CSS_SELECTOR,"div[role='menuitem']")[0]
        orientation_tab.click()
        time.sleep(1)
        orientations = self.driver.find_elements(By.CSS_SELECTOR,"div[role='menuitemradio']")
        if self.orientation_type == "landscape":
            orientations[1].click()
        elif self.orientation_type == "portrait":
            orientations[0].click()
        time.sleep(1)
    def _select_duration(self):
        setting_button = self.driver.find_elements(By.CSS_SELECTOR, "button[aria-label='Settings']")[1]
        # setting_button.click()
        # time.sleep(1)
        setting_button.click()
        time.sleep(1)

        duration_tab = self.driver.find_elements(By.CSS_SELECTOR,"div[role='menuitem']")[1]
        duration_tab.click()
        time.sleep(1)
        
        durations = self.driver.find_elements(By.CSS_SELECTOR,"div[role='menuitemradio']")
        if self.duration == 15:
            durations[0].click()
        elif self.duration == 10:
            durations[1].click()
        time.sleep(1)