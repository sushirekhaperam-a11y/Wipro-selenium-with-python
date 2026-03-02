import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class InformationPage:
    # locators
    first_name= (By.XPATH, "//input[@id='first-name']")
    last_name = (By.XPATH,"//input[@id='last-name']")
    postal_code = (By.XPATH,"//input[@id='postal-code']")
    c = (By.XPATH,"//input[@id='continue']")

    def __init__(self, driver):
        self.driver = driver

    # We use * to unpack the tuple.

    # checkout page
    def click_first_name(self, first_name):
        self.driver.find_element(*self.first_name).send_keys(first_name)
    def click_last_name(self,last_name):
        self.driver.find_element(*self.last_name).send_keys(last_name)
    def click_postal_ccode(self,postal_code):
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
    def click_continue(self):
        self.driver.find_element(*self.c).click()
    def Details(self,firstname,lastname,postalcode):
        self.click_first_name(firstname)
        self.click_last_name(lastname)
        self.click_postal_ccode(postalcode)
        self.click_continue()



