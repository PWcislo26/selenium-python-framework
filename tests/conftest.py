import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):

    browser = request.param
    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--enable-javascript")
        service = ChromeService(ChromeDriverManager().install())
        my_driver = webdriver.Chrome(service=service, options=chrome_options)
    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")
    yield my_driver
    my_driver.quit()
