
import pytest as pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browsers():
    chrome_browser = Chrome(executable_path=ChromeDriverManager().install())
    chrome_browser.maximize_window()

    chrome_browser.get("https://accounts.ukr.net/")
#    chrome_browser.get("https://mail.google.com")

    yield chrome_browser

    chrome_browser.quit()

