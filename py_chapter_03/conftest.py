import pytest
from selenium import webdriver

chromeDriver_Path = "Drivers\chromedriver.exe"
firefoxDriver_Path = "Drivers\geckodriver.exe"


@pytest.fixture(scope="function")
def setup(request):
    print('launch browser chrome')

    driver = webdriver.Chrome(executable_path=chromeDriver_Path)

    driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

    request.cls.driver = driver

    yield driver

    driver.close()






