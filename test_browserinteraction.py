import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class Test_action:
    def test_action(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        # navigate to url
        driver.get("https://trytestingthis.netlify.app/")
        time.sleep(4)
        #browser interactions
        title = driver.title
        print(title)
        time.sleep(2)
        url = driver.current_url
        print(url)
        time.sleep(2)
        #Navigational commands
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.close()

