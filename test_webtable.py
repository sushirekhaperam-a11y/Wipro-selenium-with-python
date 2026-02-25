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
        driver.get("https://the-internet.herokuapp.com/tables")
        time.sleep(5)
        driver.implicitly_wait(10)
        # no of rows
        rows = driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr")
        for i in rows:
            print(i.text)
        #no of columns
        col= driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr[1]/td")
        for j in col:
            print(j.text)
        cell = driver.find_element(By.XPATH,"//table[@id='table1']/tbody/tr[3]/td[4]")
        print(cell.text)
        driver.quit()