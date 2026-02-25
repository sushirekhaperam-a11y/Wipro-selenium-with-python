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
        driver.get("https://the-internet.herokuapp.com/windows")
        time.sleep(4)
        driver.implicitly_wait(10)
        click_here = driver.find_element(By.XPATH,"//a[normalize-space()='Click Here']")
        click_here.click()
        #fetch the window handles of the tabs
        windows = driver.window_handles
        print(windows)
        # switching the tab to child
        driver.switch_to.window(windows[1])
        #printing the text
        text = driver.find_element(By.XPATH,"//h3[normalize-space()='New Window']")
        print(text)
        driver.close()
        #switching back to the  parent window
        driver.switch_to.window(windows[0])
        click_here.is_displayed()
        driver.close()