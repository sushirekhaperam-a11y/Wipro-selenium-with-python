import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
class Test_login:
    def test_login(self):
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        time.sleep(4)
        Radio = driver.find_element(By.XPATH,"//input[@value='radio1']")
        Radio.click()
        assert "Practice Page" in driver.title
        try:
            country = Select(driver.find_element(By.XPATH, "//div[@class='wrapperTwo']//div//select"))
            country.select_by_visible_text("India")
        except NoSuchElementException as e:
            print(" country is not found:", e)
