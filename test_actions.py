import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
class Test_action:
    def test_action(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.amazon.in/")
        time.sleep(4)
        actions = ActionChains(driver)
        #double click
        amz = driver.find_element(By.XPATH,"//a[normalize-space()='Bestsellers']")
        actions.double_click(amz).perform()
        time.sleep(4)
        driver.back()
        time.sleep(4)
        #right click
        mobiles = driver.find_element(By.XPATH,"//a[normalize-space()='Mobiles']")
        actions.context_click(mobiles).perform()
        time.sleep(4)

        #move the element
        prime = driver.find_element(By.XPATH,"//span[normalize-space()='Prime']")
        actions.move_to_element(prime).perform()
        time.sleep(4)
        #Click and hold
        fresh = driver.find_element(By.XPATH,"//span[normalize-space()='Fresh']")
        actions.click_and_hold(fresh).perform()
        time.sleep(4)
        driver.close()
