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
        alert= driver.find_element(By.XPATH,"//input[@id='alertbtn']")
        alert.click()
        alt = driver.switch_to.alert
        alt.accept()
        time.sleep(2)
        confirm = driver.find_element(By.XPATH, "//input[@id='confirmbtn']")
        confirm.click()
        c = driver.switch_to.alert
        c.dismiss()
        time.sleep(2)
        driver.close()

