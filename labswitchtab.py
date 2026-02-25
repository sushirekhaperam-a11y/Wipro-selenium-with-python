import time

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
        open_tab = driver.find_element(By.XPATH,"//a[@id='opentab']")
        open_tab.click()
        windows = driver.window_handles
        print(windows)
        driver.switch_to.window(windows[1])
        # printing the text
        text = driver.find_element(By.XPATH, "//a[@href='https://www.qaclickacademy.com']//img[@alt='Logo']")
        print(text)
        driver.close()
        # switching back to the  parent window
        driver.switch_to.window(windows[0])
        driver.close()
