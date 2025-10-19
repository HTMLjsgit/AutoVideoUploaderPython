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
from pywinauto import Desktop
from pywinauto.application import Application

from YoutubeVideoUpload import YoutubeVideoUpload
from SoraVideo import SoraVideo

#初期化
WebInterface.connect()
SoraVideo = SoraVideo("男性が公園でジョギングをしている動画。背景には青空と緑の木々が広がり、爽やかな雰囲気が漂っています。", 15).create_video()

# youtubeVideoUpload = YoutubeVideoUpload("C:/Users/newmi/Videos/douga.mp4", "C:/Users/newmi/Pictures/AJ.png",
#                                          "タイトルテスト", "説明文テスト", publish_type="public")
# youtubeVideoUpload.upload_video()