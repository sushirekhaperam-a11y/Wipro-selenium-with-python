import time
import pytest
from Pages.Login_page import LoginPage
from utilities.logger import get_logger
from utilities.excel_util import get_excel_data
test_data=get_excel_data("C://Users//Sushi//PycharmProjects//SeleniumPytestPageObjectModel//testdata//login_data.xlsx", "Sheet1")

logger = get_logger()
class TestLogin:
    def test_valid_login(self,driver):
        logger.info("opening application")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        time.sleep(2)
        #create the object of the login page
        lp = LoginPage(driver)
        logger.info("enter the credentials")
        lp.login("Admin","admin123")
        time.sleep(2)
        assert "OrangeHRM" in driver.title

    def test_invalid_login(self,driver):
        logger.info("opening application")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        time.sleep(2)
        lp=LoginPage(driver)
        logger.info("enter the credentials")
        lp.login("Admin","wrongpassword")
        time.sleep(2)
        assert "Invalid credentials" in lp.get_error_message()
    #test data stored in excel sheet
    @pytest.mark.parametrize("username,password"
        ,test_data)
    def test_login_excel(self,driver,username,password):
        logger.info("opening application")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        time.sleep(2)
        lp = LoginPage(driver)
        lp.login(username,password)
        if password == "admin123":
            assert "OrangeHRM" in driver.title
        else:
            assert "Invalid credentials" in lp.get_error_message()






