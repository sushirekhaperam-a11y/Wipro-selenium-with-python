from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class CustomerPage:
    user_select = (By.ID, "userSelect")
    login_btn = (By.XPATH, "//button[text()='Login']")
    deposit_btn = (By.XPATH, "//button[normalize-space()='Deposit']")
    withdraw_btn = (By.XPATH, "//button[normalize-space()='Withdrawl']")
    amount_input = (By.XPATH, "//input[@ng-model='amount']")
    submit_btn = (By.XPATH, "//button[@type='submit']")
    balance = (By.XPATH, "//div[@ng-hide='noAccount']/strong[2]")
    home_btn = (By.XPATH, "//button[text()='Home']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, customer_name):
        Select(self.driver.find_element(*self.user_select)).select_by_visible_text(customer_name)
        time.sleep(1)
        self.driver.find_element(*self.login_btn).click()
        time.sleep(1)

    def deposit(self, amount):
        self.driver.find_element(*self.deposit_btn).click()
        time.sleep(1)
        self.driver.find_element(*self.amount_input).send_keys(amount)
        time.sleep(1)
        self.driver.find_element(*self.submit_btn).click()
        time.sleep(1)

    def withdraw(self, amount):
        self.driver.find_element(*self.withdraw_btn).click()
        time.sleep(1)
        self.driver.find_element(*self.amount_input).send_keys(amount)
        time.sleep(1)
        self.driver.find_element(*self.submit_btn).click()
        time.sleep(1)

    def get_balance(self):
        return self.driver.find_element(*self.balance).text

    time.sleep(1)

    def click_home(self):
        self.driver.find_element(*self.home_btn).click()
        time.sleep(1)