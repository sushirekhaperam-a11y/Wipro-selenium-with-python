#create a fixture for invoke chrome browser and close the chrome browser
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
@pytest.fixture(scope= "class")
def setup(request):
    service = Service(ChromeDriverManager().install())
    #driver instance is created to web driver globally in test script
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    #driver  set locally passed to request at  class level so  that driver is available for other testcases in the tests folder
    request.cls.driver = driver
    yield
    driver.quit()



