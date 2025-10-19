from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# webInterface.py はユーザーのカスタムモジュールと仮定
from webInterface import WebInterface 
# ↓↓↓ エラー処理が変更になるため、これもインポート ↓↓↓
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class YoutubeVideoUpload:
    def __init__(self, video_path,thumbnail_path, title, description, publish_type="private"):
        self.title = title
        self.video_path = video_path
        self.description = description
        self.thumbnail_path = thumbnail_path
        self.publish_type = publish_type
        self.driver = WebInterface.get_driver()

    def upload_video(self):
        url = "https://studio.youtube.com/channel/"
        self.driver.get(url)
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "button[aria-label=作成]").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "tp-yt-paper-item").click()
        time.sleep(1)

        #動画のアップロード処理
        upload_input_video = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )

        upload_input_video.send_keys(self.video_path)
        
        time.sleep(5)
        # サムネイルのアップロード処理
        if self.thumbnail_path:
            upload_input_thumbnail = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
            )
            upload_input_thumbnail.send_keys(self.thumbnail_path)
        time.sleep(3)
        # タイトルと説明文の入力
        if self.title:
            title_textarea = self.driver.find_elements(By.ID, "textbox")[0]
            title_textarea.clear()
            time.sleep(1)
            title_textarea.send_keys(self.title)
            time.sleep(2)
        if self.description:
            description_textarea = self.driver.find_elements(By.ID, "textbox")[1]
            description_textarea.send_keys(self.description)
            time.sleep(2)   

        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "tp-yt-paper-radio-button[name='VIDEO_MADE_FOR_KIDS_NOT_MFK']").click()
        time.sleep(2)
        for i in range(3):
            self._next_button_click()
        self._publish_video(_type=self.publish_type)

        print("ファイルの送信に成功しました。アップロードが開始されます。")

    def _next_button_click(self):
        # 次へボタンをクリックする処理
        next_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='次へ']"))
        )
        next_button.click()
        time.sleep(1)
        print("次へボタンをクリックしました。")
    def _publish_video(self, _type="private"):
        # 公開ボタンをクリックする処理
        if _type == "private":
            self.driver.find_element(By.CSS_SELECTOR, "tp-yt-paper-radio-button[name='PRIVATE']").click()
            publish_button = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='保存']")
        elif _type == "public":
            self.driver.find_element(By.CSS_SELECTOR, "tp-yt-paper-radio-button[name='PUBLIC']").click()
            publish_button = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='公開']")
        elif _type == "unlisted":
            self.driver.find_element(By.CSS_SELECTOR, "tp-yt-paper-radio-button[name='UNLISTED']").click()
            publish_button = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='保存']")
        time.sleep(2)
        
        publish_button.click()
        time.sleep(1)
        print("公開ボタンをクリックしました。")