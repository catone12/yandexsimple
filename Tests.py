
import allure
from Dat import YandexSeacrhData as dat
from BaseApp import BaseApp
from selenium.webdriver.common.by import By

    

class TestYand:
    @allure.feature('Random Yandex')
    @allure.story('Получаем страницу почты')
    @allure.severity('blocker')
    def test_yandex_search(self,app):
        #аннотацию fixture не принимает (или class)
        #запускаем сайт
        BaseApp(app).go_to_site()
        #a=BasePage(app).proverka_url("https://yandex.ru/")
        #print(a)




