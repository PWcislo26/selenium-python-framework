import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ChromeOptions, FirefoxOptions


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):

    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless=new")
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")
    browser = request.param
    if browser == "chrome":
        my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")
    yield my_driver
    my_driver.quit()

