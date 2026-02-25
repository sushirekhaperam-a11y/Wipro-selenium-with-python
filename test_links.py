import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
DOWNLOAD_DIR = "C://Users//Sushi//Downloads"
class Test_action:
    def test_action(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/download")
        time.sleep(4)
        links = driver.find_elements(By.TAG_NAME,"a")
        count = len(links)
        print(count)
        for link in links:
            print(link.text)
        driver.close()