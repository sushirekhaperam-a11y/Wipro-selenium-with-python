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

        driver.get("https://trytestingthis.netlify.app/")
        time.sleep(2)

        dropdown = Select(driver.find_element(By.ID, "owc"))

        dropdown.select_by_value("option 1")
        dropdown.select_by_value("option 3")

        time.sleep(2)

        print("Selected Options:")
        for option in dropdown.all_selected_options:
            print(option.text)

        dropdown.deselect_all()
        print("All options deselected")

        time.sleep(2)
        driver.quit()