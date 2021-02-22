from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
from YandexPages import YandexPages
import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
class BaseApp(YandexPages):

    def __init__(self,app):
        super().__init__()
        self.browser =  app
        #self.browser = webdriver.Remote(command_executor="http://192.168.0.101:4444/wd/hub",desired_capabilities={"browserName": "firefox",})
        #в качестве примера испольузется обычный браузер , а ниже сам selenium grid (настроенный)
        self.base_url = "https://yandex.ru/"
        self.countmails=0
        #Переменная для подсчета писем
        #self.Yandex=SearchHelper(self)
        self.browser.implicitly_wait(10)

    def find_element(self, locator: str, time: int = 10) -> str:
        return WebDriverWait(self.browser,time).until(EC.visibility_of_element_located(locator),message=f"Can't find element by locator {locator}")
        #чтобы часто не использовать этот метод в YandexPages,я просто буду ссылаться на него

    def go_to_site(self) -> str:
        with allure.step("Зашли"):
            return self.browser.get(self.base_url)
    def proverka_avtorizacii(self, time: int = 10) -> str:
        #return self.find_element()


        return WebDriverWait(self.browser, time).until(EC.invisibility_of_element_located((By.XPATH,'//span[contains(@class,"username ")]')),message=f"Can't find element by locator ")
    def proverka_url(self, url: str,time: int = 10) -> str:
        try:
            return WebDriverWait(self.browser, time).until(EC.url_to_be(url),message=f"Can't find element by locator {url}")

        except TimeoutException:
            return False
    def proverka_url_changes(self, url: str,time: int = 10) -> str:
        try:
            return WebDriverWait(self.browser, time).until(EC.url_changes(url),message=f"Can't find element by locator {url}")

        except TimeoutException:
            return False
#url_changes
