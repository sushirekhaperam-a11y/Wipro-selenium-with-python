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
        driver.get("https://the-internet.herokuapp.com/upload")
        time.sleep(4)
        browser = driver.find_element(By.XPATH,"//input[@id='file-upload']")
        browser.send_keys("C:\\Users\\Sushi\\Downloads\\AF_Mcqs.docx")
        time.sleep(4)
        upload = driver.find_element(By.XPATH,"//input[@id='file-submit']")
        upload.click()
        time.sleep(2)
        fileuploaded = driver.find_element(By.XPATH,"//h3[normalize-space()='File Uploaded!']")
        assert fileuploaded.text == "File Uploaded!"
        time.sleep(4)
        driver.close()