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
        driver.get("https://rsuitejs.com/components/date-picker/")
        time.sleep(5)

        dat = driver.find_element(By.XPATH, "//div[4]//div[1]//div[1]//div[1]//div[1]//span[1]//*[name()='svg']")
        dat.click()
        time.sleep(2)

        year = driver.find_element(By.XPATH, "//button[@id='rs-:r2b:-grid-label']")
        year.click()
        time.sleep(2)

        month = driver.find_element(By.XPATH, "//div[@aria-label='Oct, 2027']//span[@class='rs-calendar-month-dropdown-cell-content'][normalize-space()='Oct']")
        month.click()
        time.sleep(2)

        date = driver.find_element(By.XPATH, "//div[@title='Oct 29, 2027']//div[@class='rs-calendar-table-cell-content']")
        date.click()
        time.sleep(3)

        ok = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
        ok.click()
        time.sleep(3)

        driver.quit()