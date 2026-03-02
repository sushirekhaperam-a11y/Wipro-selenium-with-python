import time
import pytest

from Pages.Login_page import LoginPage
from Pages.Thankyou_page import ThankyouPage
from Pages.finish_page import FinishPage
from Pages.information import InformationPage
from Pages.products_page import CartPage
from Pages.sauce_login import Sauce_LoginPage
from Pages.checkout_page import CheckoutPage
from utilities.excel_util import get_excel_data1
from utilities.logger import get_logger
test_data = get_excel_data1("C://Users//Sushi//PycharmProjects//SeleniumPytestPageObjectModel//testdata//sauce_login_data.xlsx","Sheet1")
logger = get_logger()
class Test_Cart:
    @pytest.mark.parametrize("username,password,firstname,lastname,postalcode",test_data)
    def test_add_products(self,driver,username,password,firstname,lastname,postalcode):
        logger.info("opening application")
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        #create the object of the cart page(driver)
        logger.info("Enter the credentials")
        lp= Sauce_LoginPage(driver)
        lp.login(username,password)
        time.sleep(4)
        logger.info("Adding the products to cart")
        cp = CartPage(driver)
        cp.click_add_to_cart(add_to_cart="add_to_cart")
        time.sleep(2)
        cp.click_cart_icon(cart_icon="cart_icon")
        time.sleep(2)
        # checkout page object
        logger.info("click the checkout option")
        co = CheckoutPage(driver)
        co.click_check_out(check_out="check_out")
        time.sleep(2)
        # Information page
        logger.info("enter the details")
        information = InformationPage(driver)
        information.Details(firstname,lastname,postalcode)
        time.sleep(2)
        # finish page
        logger.info("click on the finish ")
        finish = FinishPage(driver)
        finish.click_finish(finish="finish")
        time.sleep(2)
        #Thank you page
        logger.info("Thank you for shopping")
        th = ThankyouPage(driver)
        th.click_back_home(back_home="back_home")
        time.sleep(2)

