import time
from selectors import DefaultSelector

import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
class Test_dropdown:
    def test_dropdown(self):
        driver.maximize_window()

        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(2)
        #switch the control to alert
        simplealt = driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
        simplealt.click()
        alt = driver.switch_to.alert
        alt.accept()
        time.sleep(4)
        #confirmational alert
        confirmalt =driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']")
        confirmalt.click()
        alt = driver.switch_to.alert
        alt.dismiss()
        time.sleep(4)
        #prompt alert
        promptalt = driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
        promptalt.click()
        alt= driver.switch_to.alert
        altertext = alt.text
        print(altertext)
        alt.send_keys("hello")
        alt.accept()
        time.sleep(4)
        driver.close()
