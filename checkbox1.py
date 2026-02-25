import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
class Test_login:
    def test_login(self):
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(4)
        name = driver.find_element(By.NAME,"username")
        name.send_keys("Admin")
        password = driver.find_element(By.NAME,"password")
        password.send_keys("admin123")
        time.sleep(4)
        Login = driver.find_element(By.XPATH,"//button[@type='submit']")
        Login.click()
        pim = driver.find_element(By.XPATH,"")
        pim.click()
        time.sleep(2)
        checkbox_list = driver.find_elements(By.XPATH, "//i[@class = 'oxd-icon bi-check oxd-checkbox-input-icon']")
        count = len(checkbox_list)
        print(count)
        for i in range(1,checkbox_list):
            time.sleep(2)
            i.click()
        driver.close()