import time

import accept
import driver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class Test_action:
    def test_action(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        # navigate to url
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        time.sleep(4)
        driver.implicitly_wait(10)
        mousehover = driver.find_element(By.XPATH,"//button[@id='mousehover']")
        mousehover.click()
        top= driver.find_element(By.XPATH,"//button[@id='mousehover']")
        top.click()
        time.sleep(2)
        reload= driver.find_element(By.XPATH, "//a[normalize-space()='Reload']")
        reload.click()
        time.sleep(2)
        driver.close()

