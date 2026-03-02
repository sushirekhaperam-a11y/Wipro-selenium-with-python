from selenium.webdriver.common.by import By
import time
class LoginPage:
    manager_login_btn = (By.XPATH, "//button[text()='Bank Manager Login']")
    customer_login_btn = (By.XPATH, "//button[text()='Customer Login']")
    def __init__(self, driver):
        self.driver = driver

    def click_manager(self):
        self.driver.find_element(*self.manager_login_btn).click()

    time.sleep(1)

    def click_customer(self):
        self.driver.find_element(*self.customer_login_btn).click()