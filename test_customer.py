import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
class TestBanking:

    def test_complete_flow(self):
        time.sleep(3)

        # Manager Login
        self.driver.find_element(By.XPATH, "//button[text()='Bank Manager Login']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@ng-click='addCust()']").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("sunil")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("p")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Post Code']").send_keys("12345")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(2)

        # Open Account
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Open Account']").click()
        time.sleep(2)
        Select(self.driver.find_element(By.ID, "userSelect")).select_by_visible_text("sunil p")
        time.sleep(2)
        Select(self.driver.find_element(By.ID, "currency")).select_by_visible_text("Rupee")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Process']").click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//button[text()='Home']").click()
        time.sleep(2)

        # Customer Login
        self.driver.find_element(By.XPATH, "//button[text()='Customer Login']").click()
        time.sleep(2)
        Select(self.driver.find_element(By.ID, "userSelect")).select_by_visible_text("sunil p")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Login']").click()
        time.sleep(2)


        # Deposit
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Deposit']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@ng-model='amount']").send_keys("5000")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

        # Withdraw
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Withdrawl']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@ng-model='amount']").send_keys("2000")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

        # Validate Balance
        balance = self.driver.find_element(By.XPATH, "//div[@ng-hide='noAccount']/strong[2]").text
        assert int(balance) == 3000
        time.sleep(2)