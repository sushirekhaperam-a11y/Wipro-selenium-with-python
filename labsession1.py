import time
from selenium import webdriver
from selenium.common import  NoSuchElementException,ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
class Test_login:
    def test_login(self):
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        time.sleep(4)
        try:
            addtocart = driver.find_element(By.XPATH, "//div[3]//div[3]//button[1]")
            addtocart.click()
        except NoSuchElementException as e:
            print("add to cart are not found:", e)
        try:
            addtocart1= driver.find_element(By.XPATH, "//div[4]//div[3]//button[1]")
            addtocart1.click()
        except NoSuchElementException as e:
            print("add to cart are not found:", e)
        try:
            items= driver.find_element(By.XPATH, "//img[@alt='Cart']")
            items.click()
        except NoSuchElementException as e:
            print(" No item  found:", e)
        try:
            proceed= driver.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']")
            proceed.click()
        except NoSuchElementException as e:(
            print(" proceed is not found:", e))
        try:
            placeorder= driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']")
            placeorder.click()
        except NoSuchElementException as e:
            print(" place order is not found:", e)
        try:
            country = Select(driver.find_element(By.XPATH, "//div[@class='wrapperTwo']//div//select"))
            country.select_by_visible_text("India")
        except NoSuchElementException as e:
            print(" country is not found:", e)
        try:
            condition=driver.find_element(By.XPATH,"//div[@class='wrapperTwo']")
            condition.click()
        except NoSuchElementException as e:
            print(" Agree and conditions term is not found:", e)
        try:
            proceed=driver.find_element(By.XPATH,"//button[normalize-space()='Proceed']")
            proceed.click()
        except NoSuchElementException as e:
            print(" Agree and conditions term is not found:", e)
        try:
            lastpage=driver.find_element(By.XPATH,"//div[@id='root']")
            lastpage.click()
        except NoSuchElementException as e:
            print(" Thankyou page  is not found:", e)
        driver.quit()

