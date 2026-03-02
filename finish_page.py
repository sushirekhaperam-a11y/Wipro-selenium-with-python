import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class FinishPage:
    # locators
    finish= (By.XPATH, "//button[@id='finish']")

    def __init__(self, driver):
        self.driver = driver

    # We use * to unpack the tuple.

    # checkout page
    def click_finish(self,finish):
        self.driver.find_element(*self.finish).click()