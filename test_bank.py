import time
import pytest
from Pages.home_page import LoginPage
from Pages.bank_manager_login import ManagerPage
from Pages.add_customer import CustomerPage
from utilities.logger import get_logger
from utilities.excel_util import get_excel_data1
logger = get_logger()
test_data = get_excel_data1("C://Users//Sushi//PycharmProjects//SeleniumPytestPageObjectModel//testdata//bank_details.xlsx", "Sheet1")

class TestLogin:
    # test data stored in excel sheet
    @pytest.mark.parametrize("First_name, Last_name , Post,Money,Full_name,Deposit,withdraw", test_data)
    def test_excel(self, driver,First_name, Last_name , Post,Money,Full_name,Deposit,withdraw):
        logger.info("Opening application")
        driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        time.sleep(3)
        login = LoginPage(self.driver)
        manager = ManagerPage(self.driver)
        customer = CustomerPage(self.driver)

        # Manager Login
        login.click_manager()
        time.sleep(2)

        # Add Customer
        manager.add_customer(First_name, Last_name, Post)
        time.sleep(2)

        # Open Account
        manager.open_account(Full_name, Money)
        time.sleep(2)

        # Back to Home
        customer.click_home()
        time.sleep(2)

        # Customer Login
        login.click_customer()
        customer.login(Full_name)
        time.sleep(2)

        # Deposit
        customer.deposit(Deposit)
        time.sleep(2)

        # Withdraw
        customer.withdraw(withdraw)
        time.sleep(2)

        # Validate Balance
        balance = customer.get_balance()
        assert int(balance) == 4000
        time.sleep(2)