import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
class Test_action:
    def test_action(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.facebook.com/")
        time.sleep(4)
        actions = ActionChains(driver)
        email = driver.find_element(By.XPATH,"//input[@name='email']")
        seriesaction = actions.move_to_element(email).key_down(Keys.SHIFT).send_keys("hello")
        seriesaction.perform()
        time.sleep(4)

        #ctrl a
        actions.click(email).key_down(Keys.CONTROL).send_keys('a').send_keys('c').key_up(Keys.CONTROL).perform()
        time.sleep(4)
        password = driver.find_element(By.XPATH, "//input[@name='pass']")
        passaction = actions.move_to_element(password).key_down(Keys.CONTROL).key_up(Keys.CONTROL).send_keys("v")
        passaction.perform()
        driver.close()
