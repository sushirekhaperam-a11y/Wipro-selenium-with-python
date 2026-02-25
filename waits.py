import time

import driver
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class Test_DatePicker:
    def test_date(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://testautomationpractice.blogspot.com/")
        time.sleep(5)
        # This is an global setting that applies to every element location call for entire session
        driver.implicitly_wait(10)
        #explicit wait
        radio_btn= driver.find_element(By.XPATH,"//input[@id='female']")
        wait = WebDriverWait(driver, timeout=2)
        wait.until(lambda _: radio_btn.is_displayed())
        #custom wait
        errors = [NoSuchElementException, ElementNotInteractableException]
        wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
        wait.until(lambda _: radio_btn.send_keys("Displayed") or True)

