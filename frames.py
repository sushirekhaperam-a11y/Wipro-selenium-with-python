import time

import driver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class Test_DatePicker:
    def test_date(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://jqueryui.com/datepicker/")
        time.sleep(5)
        driver.implicitly_wait(10)
        #frame = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
        driver.switch_to.frame(0)
        date_picker = driver.find_element(By.XPATH,"//input[@id='datepicker']")
        date_picker.click()
        time.sleep(2)
        driver.close()