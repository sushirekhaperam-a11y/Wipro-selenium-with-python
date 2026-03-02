import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CartPage:
    # locators
    add_to_cart = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    cart_icon= (By.XPATH, "//a[@class='shopping_cart_link']")

    def __init__(self, driver):
        self.driver = driver

    # We use * to unpack the tuple.

    # add to cart
    def click_add_to_cart(self, add_to_cart):
        self.driver.find_element(*self.add_to_cart).click()

    # cart icon
    def click_cart_icon(self, cart_icon):
        self.driver.find_element(*self.cart_icon).click()





