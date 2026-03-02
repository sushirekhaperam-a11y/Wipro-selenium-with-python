import time
import pytest

from Pages.Thankyou_page import ThankyouPage
from Pages.checkout_page import CheckoutPage
from Pages.finish_page import FinishPage
from Pages.information import InformationPage
from Pages.products_page import CartPage
from Pages.sauce_login import Sauce_LoginPage
from utilities.logger1 import get_logger1
from utilities.excel_util1 import get_excel_data
from utilities.excel_util import get_excel_data1
test_data=get_excel_data("C://Users//Sushi//PycharmProjects//SeleniumPytestPageObjectModel//testdata//login_data.xlsx", "Sheet1")
test_data1 = get_excel_data1("C://Users//Sushi//PycharmProjects//SeleniumPytestPageObjectModel//testdata//details.xlsx","Sheet1")
logger1 = get_logger1()
class TestLogin:
    def test_valid_login(self,driver):
        logger1.info("opening application")
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        #create the object of the login page
        lp = Sauce_LoginPage(driver)
        logger1.info("enter the credentials")
        lp.login("standard_user","secret_sauce")
        time.sleep(2)
        assert "Swag Labs" in driver.title

    def test_invalid_login(self,driver):
        logger1.info("opening application")
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        lp=Sauce_LoginPage(driver)
        logger1.info("enter the credentials")
        lp.login("standard_user","wrongpassword")
        time.sleep(2)
        assert "Epic sadface: Username and password do not match any user in this service" in lp.get_error_message()
    #test data stored in excel sheet
    @pytest.mark.parametrize("username,password" , test_data)
    def test_login_excel(self, driver, username, password):
        logger1.info("opening application")
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        lp = Sauce_LoginPage(driver)
        lp.login(username, password)
        if password == "secret_sauce":
            assert "Swag Labs" in driver.title
        else:
            assert "Epic sadface: Username and password do not match any user in this service" in lp.get_error_message()
    def test_add_products(self,driver):
        logger1.info("opening application")
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        #create the object of the cart page(driver)
        logger1.info("enter the credentials")
        lp= Sauce_LoginPage(driver)
        lp.login("standard_user","secret_sauce")
        time.sleep(4)
        cp = CartPage(driver)
        cp.click_add_to_cart(add_to_cart="add_to_cart")
        time.sleep(2)
        cp.click_cart_icon(cart_icon="cart_icon")
        time.sleep(2)
    def test_checkout(self,driver):
        logger1.info("opening application")
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        #create the object of the cart page(driver)
        logger1.info("enter the credentials")
        lp= Sauce_LoginPage(driver)
        lp.login("standard_user","secret_sauce")
        time.sleep(4)
        cp = CartPage(driver)
        cp.click_add_to_cart(add_to_cart="add_to_cart")
        time.sleep(2)
        cp.click_cart_icon(cart_icon="cart_icon")
        time.sleep(2)
        co = CheckoutPage(driver)
        co.click_check_out(check_out="check_out")
        time.sleep(2)
    def test_details(self,driver):
        logger1.info("opening application")
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        #create the object of the cart page(driver)
        logger1.info("enter the credentials")
        lp= Sauce_LoginPage(driver)
        lp.login("standard_user","secret_sauce")
        time.sleep(4)
        cp = CartPage(driver)
        cp.click_add_to_cart(add_to_cart="add_to_cart")
        time.sleep(2)
        cp.click_cart_icon(cart_icon="cart_icon")
        time.sleep(2)
        co = CheckoutPage(driver)
        co.click_check_out(check_out="check_out")
        time.sleep(2)
        information = InformationPage(driver)
        information.Details("sushi", "rekha", 1223)
        time.sleep(2)
    @pytest.mark.parametrize("firstname,lastname,postalcode",test_data1)
    def test_invalid_details(self, driver,firstname,lastname,postalcode):
        logger1.info("opening application")
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        # create the object of the cart page(driver)
        logger1.info("enter the credentials")
        lp = Sauce_LoginPage(driver)
        lp.login("standard_user", "secret_sauce")
        time.sleep(4)
        cp = CartPage(driver)
        cp.click_add_to_cart(add_to_cart="add_to_cart")
        time.sleep(2)
        cp.click_cart_icon(cart_icon="cart_icon")
        time.sleep(2)
        co = CheckoutPage(driver)
        co.click_check_out(check_out="check_out")
        time.sleep(2)
        information = InformationPage(driver)
        information.Details(firstname,lastname,postalcode)
        time.sleep(2)

    def test_finish(self, driver):
        logger1.info("opening application")
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        # create the object of the cart page(driver)
        lp = Sauce_LoginPage(driver)
        lp.login("standard_user", "secret_sauce")
        time.sleep(4)
        cp = CartPage(driver)
        cp.click_add_to_cart(add_to_cart="add_to_cart")
        time.sleep(2)
        cp.click_cart_icon(cart_icon="cart_icon")
        time.sleep(2)
        co = CheckoutPage(driver)
        co.click_check_out(check_out="check_out")
        time.sleep(2)
        information = InformationPage(driver)
        information.Details("sushi", "rekha", 1223)
        time.sleep(2)
        finish = FinishPage(driver)
        finish.click_finish(finish="finish")
        time.sleep(2)

    def test_thankyou(self, driver):
        logger1.info("opening application")
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        # create the object of the cart page(driver)
        lp = Sauce_LoginPage(driver)
        lp.login("standard_user", "secret_sauce")
        time.sleep(4)
        cp = CartPage(driver)
        cp.click_add_to_cart(add_to_cart="add_to_cart")
        time.sleep(2)
        cp.click_cart_icon(cart_icon="cart_icon")
        time.sleep(2)
        co = CheckoutPage(driver)
        co.click_check_out(check_out="check_out")
        time.sleep(2)
        information = InformationPage(driver)
        information.Details("sushi", "rekha", 1223)
        time.sleep(2)
        finish = FinishPage(driver)
        finish.click_finish(finish="finish")
        time.sleep(2)
        th = ThankyouPage(driver)
        th.click_back_home(back_home="back_home")
        time.sleep(2)






