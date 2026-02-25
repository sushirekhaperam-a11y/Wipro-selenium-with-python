import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
class Test_multiselectcheckbox:
    def test_checkbox(self):
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        time.sleep(4)
        checkbox_list = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
        count = len(checkbox_list)
        print(count)
        for i in checkbox_list:
            time.sleep(4)
            i.click()
        driver.close()
