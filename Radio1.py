import time
from tkinter import Scrollbar

from cffi.ffiplatform import int_or_long
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
class Test_login:
    def test_login(self):
        driver.maximize_window()
        driver.get("https://testautomationpractice.blogspot.com/")
        time.sleep(4)
        Radio= driver.find_element(By.XPATH,"//input[@id='female']")
        Radio.click()
        time.sleep(4)
        check1 = driver.find_element(By.XPATH,"//input[@id='monday']")
        check1.click()
        driver.quit()