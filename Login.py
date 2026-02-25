import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
class Test_login:
    def test_login(self):
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(4)
        name = driver.find_element(By.NAME,"username")
        name.send_keys("Admin")
        password = driver.find_element(By.NAME,"password")
        name.send_keys("admin123")
        time.sleep(4)
        Login = driver.find_element(By.XPATH,"//button[@type='submit']")
        Login.click()
        assert "OrangeHRM" in driver.title
