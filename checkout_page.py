import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutPage:
    # locators
    check_out= (By.XPATH, "//button[@id='checkout']")

    def __init__(self, driver):
        self.driver = driver

    # We use * to unpack the tuple.

    # checkout page
    def click_check_out(self, check_out):
        self.driver.find_element(*self.check_out).click()




