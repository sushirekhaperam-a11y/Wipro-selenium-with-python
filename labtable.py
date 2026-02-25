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
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        time.sleep(5)
        driver.implicitly_wait(10)
        cell = driver.find_element(By.XPATH,"//table[@id='product']/tbody/tr[10]/td[2]")
        print(cell.text)
        driver.quit()