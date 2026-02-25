import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

DOWNLOAD_DIR = "C:\\Users\\Sushi\\Downloads"
class Test_action:
    def test_action(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/download")
        time.sleep(4)
        alert = driver.find_element(By.XPATH,"//a[normalize-space()='alert.jpeg']")
        alert.click()

        #verify the file download
        file_path = os.path.join(DOWNLOAD_DIR,"alert.jpeg")
        assert os.path.exists(file_path)
        time.sleep(4)
        driver.close()

