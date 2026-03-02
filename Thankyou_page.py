import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ThankyouPage:
    # locators
    back_home= (By.XPATH, "//button[@id='back-to-products']")

    def __init__(self, driver):
        self.driver = driver

    # We use * to unpack the tuple.

    # checkout page
    def click_back_home(self, back_home):
        self.driver.find_element(*self.back_home).click()