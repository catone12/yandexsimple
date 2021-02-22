import pytest
#from BaseApp import BasePage
from selenium import webdriver
@pytest.fixture(scope="session")
def app(request):
    fix= webdriver.Firefox()
    def close_driver():
        fix.quit()
    request.addfinalizer(close_driver)
    return fix

