from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class ManagerPage:
    add_customer_btn = (By.XPATH, "//button[@ng-click='addCust()']")
    open_account_btn = (By.XPATH, "//button[normalize-space()='Open Account']")
    first_name = (By.XPATH, "//input[@placeholder='First Name']")
    last_name = (By.XPATH, "//input[@placeholder='Last Name']")
    post_code = (By.XPATH, "//input[@placeholder='Post Code']")
    submit_btn = (By.XPATH, "//button[@type='submit']")
    user_select = (By.ID, "userSelect")
    currency_select = (By.ID, "currency")

    def __init__(self, driver):
        self.driver = driver

    def add_customer(self, first, last, post):
        self.driver.find_element(*self.add_customer_btn).click()
        time.sleep(1)
        self.driver.find_element(*self.first_name).send_keys(first)
        time.sleep(1)
        self.driver.find_element(*self.last_name).send_keys(last)
        time.sleep(1)
        self.driver.find_element(*self.post_code).send_keys(post)
        time.sleep(1)
        self.driver.find_element(*self.submit_btn).click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(1)

    def open_account(self, customer_name, currency):
        self.driver.find_element(*self.open_account_btn).click()
        time.sleep(1)
        Select(self.driver.find_element(*self.user_select)).select_by_visible_text(customer_name)
        time.sleep(1)
        Select(self.driver.find_element(*self.currency_select)).select_by_visible_text(currency)
        time.sleep(1)
        self.driver.find_element(*self.submit_btn).click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(1)