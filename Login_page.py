#locators - page actions
''''
loctors  = Page actions

reusbality ,
easy maintainnece
readability

.Verify with blank crdentails
5.Verify input text field validation
6 Verify password  field allowance
7. Verify logo of the login page

logon page
1. verify ;login with valid credentails
2. verify login with invalid credemtials
3.Verify password masking
4
'''
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    # locators
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, "//button[normalize-space()='Login']")
    dashboard_text = (By.XPATH, "//h6[normalize-space()='Dashboard']")
    add_to_cart = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")
    error_msg = (By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")


    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(self.username_input[0], self.username_input[1])
    # We use * to unpack the tuple.

    # enter username
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    # enter password
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    # click on login button
    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.driver.find_element(*self.error_msg).text
    #add to cart
    def click_add_to_cart(self, add_to_cart):
        self.driver.find_element(*self.add_to_cart).click()

    # cart icon
    def click_cart_icon(self, cart_icon):
        self.driver.find_element(*self.cart_icon).click()





