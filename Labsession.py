import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.common import  NoSuchElementException,ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
class Test_login:
    def test_login(self):
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        time.sleep(4)
        try:
            name = driver.find_element(By.NAME, "user-name")
            name.send_keys("visual_user")
        except NoSuchElementException as e:
            print("username is not found:",e)
        try:
            password = driver.find_element(By.NAME, "password")
            password.send_keys("secret")
        except NoSuchElementException as e:
            print("password is incorrect:", e)
        try:
            Login = driver.find_element(By.XPATH, "//input[@id='login-button']")
            Login.click()
            assert "Swag Labs" in driver.title
        except NoSuchElementException as e:
            print("login button not found:", e)
        try:
            addtocart = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
            addtocart.click()
        except NoSuchElementException as e:
            print("products are not found:", e)
        try:
            insert = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
            insert.click()
        except NoSuchElementException as e:
            print("link not found:", e)
        try:
            checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
            checkout.click()
        except NoSuchElementException as e:
            print("checkout not found:", e)
        try:
            firstname = driver.find_element(By.ID, "first-name")
            firstname.send_keys("sushi")
        except NoSuchElementException as e:
            print("firstname is incorrect:", e)
        try:
            lastname = driver.find_element(By.ID, "last-name")
            lastname.send_keys("rekha")
        except NoSuchElementException as e:
            print("lastname is incorrect:", e)
        try:
            postcode = driver.find_element(By.ID, "postal-code")
            postcode.send_keys("12345")
        except NoSuchElementException as e:
            print("postalcode is incorrect:", e)
        try:
            c = driver.find_element(By.XPATH, "//input[@id='continue']")
            c.click()
        except NoSuchElementException as e:
            print("continue button not found:", e)
        try:
            finish = driver.find_element(By.XPATH, "//button[@id='finish']")
            finish.click()
        except NoSuchElementException as e:
            print("finish button not found:", e)
        try:
            last_page = driver.find_element(By.XPATH, "//h2[normalize-space()='Thank you for your order!']")
            last_page.click()
        except NoSuchElementException as e:
            print("thankyou page not found:", e)
            time.sleep(2)
        driver.quit()