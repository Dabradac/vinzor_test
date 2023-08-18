import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.mark.usefixtures("runMode")
@pytest.fixture(scope='class')
def setup(request):
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.set_window_size(1920, 1080)
    request.cls.driver = driver
    yield driver
    driver.close()
