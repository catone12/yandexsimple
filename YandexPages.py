from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import allure
from allure_commons.types import AttachmentType
#from BaseApp import BasePage

def cli(fn):
    def wrapper(self):
        with allure.step("Click"):
            print('sdsssss')

            fn(self).click()

    return wrapper

#вообщем тут получается так, cli получает return локатора из click_login .Ну или проще поучает сам click_login
# потом wrapper получает в себя self,он очень важен, так как дает запустить сам click_login
# и в самом wrapper мы запускаем fn(self).click() , это очень похоже на click_login(self).click или еще больше расшифровав
# локатор.click()

#Либо другое объяснение:Он просто получает локатор в fn, но без self ,он не  может использовать этот локатор из click_login

#Либо он оберткой оборачивает wrapper сам становится функцией в классе, и он внутри себя вызывает fn ( click_login) и в нее же передает данные
#fn(self) и так получется что лишняя функция wrapper в клссе SearchHelper.Он похоже просто вызывает эту функцию
#добавляя немного от себя , пере или после тем как выполнить вызываемую fn(self)
#вообщем... я запутался.Прочесть про обертки!!!




class YandexPages():
    def __init__(self):
        self.LOCATOR_LOGIN_IN_TO_MAIL=(By.XPATH, "//a[contains(@class,'home-link_bold_yes')]")
        self.LOGIN_MAIL = (By.XPATH, "//input[@id='passp-field-login']")
        self.CLICK_LOGIN = (By.XPATH, "//button[@type='submit']")
        self.PASSWORD_MAIL = (By.XPATH, "//input[@id='passp-field-passwd']")
        self.CLICK_PASSWORD = (By.XPATH, "//button[@type='submit']")
        self.POST_MAIL = (By.XPATH, "//span[@class='mail-ComposeButton-Text']")
        self.POST_LOGIN1 = (By.XPATH, "//div[@class='ComposeRecipients-TopRow']//div[@class='composeYabbles']")
        self.TEXT_FIELD = (By.XPATH,"//div[@class='ComposeSubject']//input[starts-with(@class,'composeTextField ComposeSubject-TextField')]")
        self.CKE_WYSIWYG_DIV = (By.XPATH, "//div[@class='composeReact-MBodyPanels']//div[starts-with(@class,'cke_wysiwyg_div ')]")
        self.COMPOSE_SEND_BUTTON_DESKTOP = (By.XPATH, "//div[contains(@class,'ComposeSendButton_desktop')]")

        #self.app=app

        # аннотацию fixture не принимает (или class)
        #self.app.browser.implicitly_wait(10)




    def enter_mail(self):
        # заходим на почту
        with allure.step("WebDriverWait явное ожидание"):
            search_field = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(self.LOCATOR_LOGIN_IN_TO_MAIL))
        # явное ожидание ,локатор кидаем в него из другого файла
        with allure.step("клик"):
            search_field.click()
        with allure.step("создали переменную окно 0"):
            new_window = self.browser.window_handles[0]
        # создали переменную для действия на  вкладках
        with allure.step("создали переменную окно 1"):
            new_window1 = self.browser.window_handles[1]
        with allure.step("переключили на окно 0"):
            self.browser.switch_to.window(new_window)
        # переключили действия на первую вкладку
        with allure.step("переключили на окно 1"):
            self.browser.switch_to.window(new_window1)

    def enter_login(self,login: str):
        #логин вводим
        time.sleep(5)
        with allure.step("WebDriverWait явное ожидание"):
            search_field = self.find_element(self.LOGIN_MAIL)
        #запуск явного ожидания через BaseApp
        with allure.step("очистили окно ввода логина"):
            search_field.clear()
        with allure.step("ввели  логин"):
            search_field.send_keys(login)

        self.click_login()
        # ask=self.click_login()
        # ask.click()
        # пробуем ,что он в принципе получает локатор через return

    @cli
    def click_login(self) -> str:
        #кликнули на кнопку
        return self.find_element(self.CLICK_LOGIN)

       # search_field.click()

    def enter_password(self,password: str):
        #пароль вводим
        with allure.step("WebDriverWait явное ожидание"):
            search_field = self.find_element(self.PASSWORD_MAIL)
        with allure.step("очистили окно ввода пароля"):
            search_field.clear()
        with allure.step("ввели  пароль"):
            search_field.send_keys(password)
        self.click_password()

    def click_password(self):
        # кликнули на кнопку
        search_field=self.find_element(self.CLICK_PASSWORD)
        with allure.step("Click"):
            search_field.click()

    def count_mail(self):
        #считает письма на конкретной странице
        search_field = self.browser.find_elements_by_xpath("//div[starts-with(@class,'ns-view-messages-item-wrap ns-view-id-')]")
        with allure.step("считаем количество писем на странце"):
            return len(search_field)

    def go_mail(self):
        #пошли по почте

        a: int=len(self.browser.find_elements_by_xpath("//div[@data-key='box=messages-pager-date-box']//div[contains(@class,'b-mail-paginator__group js-year')]"))
        #переменная нужна для верхней границы почты (год)
        n: int=a
        #для указание на год
        aa: int=0
        #для подсчета почты
        for i in range(a,11,-1):
            #пробегаем по годам
            with allure.step(f"Год {2022-n-1+i}"):
                c=len(self.browser.find_elements_by_xpath(f"//div[@data-key='box=messages-pager-date-box']//div[contains(@class,'b-mail-paginator__group js-year')][{i}]/div[contains(@class,'b-mail-paginator__item')]"))
                #количество месяцев
                k=0
                #переменная для нижней границы месяцев
                if i==1:
                    #если год последний (конечный) на почте , то проверь сколько месяцев там есть и поставь эту границу
                    k=12-c+1
                    c=13
                for u in range(c-1,k,-1):
                    #пошли по месяцам
                    with allure.step(f"месяц {u}"):
                        try:
                            #Тут уже идет пробежка по почте и фиксация количества писем, если все же выскакивает ошибка (ElementClickInterceptedException),а она выскакиват
                            if u<10:
                                u=f'0{u}'
                            #search_field=self.app.browser.find_element_by_xpath(f"//div[@data-key='box=messages-pager-date-box']//a[@href='#inbox?datePager={u}.{2022-n-1+i}&']")
                            with allure.step("WebDriverWait явное ожидание"):
                                search_field=WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, f"//div[@data-key='box=messages-pager-date-box']//a[@href='#inbox?datePager={u}.{2022-n-1+i}&']")))
                            with allure.step("переместились к элементу почта , с помощью java_script"):
                                self.browser.execute_script("coordinates = arguments[0].getBoundingClientRect();scrollTo(coordinates.x,coordinates.y);", search_field)
                            with allure.step("Click"):
                                search_field.click()
                            time.sleep(2)
                            with allure.step("Берем из ссылки на сайте наше местоположение по тесту"):
                                v=self.browser.current_url
                            #берем из ссылки на сайте наше местоположение по тесту ,для вывода в консоли
                            with allure.step("прибавили к переменной класса , количество писем"):
                                aa+=self.count_mail()
                            print(f'{v[-8:-1]} писем {aa}  по году{i} по месяцу{u}')


                        except ElementClickInterceptedException:
                            with allure.step(f"ElementClickInterceptedException ,отправляем снова запрос"):
                                #Мы ее ловим здесь и снова отправляем запрос
                                #search_field=self.app.browser.find_element_by_xpath(f"//div[@data-key='box=messages-pager-date-box']//a[@href='#inbox?datePager={u}.{2022-n-1+i}&']")
                                with allure.step("WebDriverWait явное ожидание"):
                                    search_field=WebDriverWait(self.browser, 120).until(EC.presence_of_element_located((By.XPATH, f"//div[@data-key='box=messages-pager-date-box']//a[@href='#inbox?datePager={u}.{2022-n-1+i}&']")))
                                with allure.step("переместились к элементу почта , с помощью java_script"):
                                    self.browser.execute_script("coordinates = arguments[0].getBoundingClientRect();scrollTo(coordinates.x,coordinates.y);", search_field)
                                with allure.step("Click"):
                                    search_field.click()
                                time.sleep(2)
                                with allure.step("Берем из ссылки на сайте наше местоположение по тесту"):
                                    v=self.browser.current_url
                                with allure.step("прибавили к переменной класса , количество писем"):
                                    aa+=self.count_mail()
                                print(f'ошибка:ElementClickInterceptedException {v[-8:-1]} писем {aa}  по году{i} по месяцу{u}')
                        with allure.step("Делаем скриншот"):
                            allure.attach(self.browser.get_screenshot_as_png(), name=f"Год {2022-n-1+i},месяц {u}",attachment_type=AttachmentType.PNG)
                                #Фиксируем результаты в allure

        self.countmails=aa
        #записали весь результат в переменную(класса)

    def mail_post(self,post_login: str,fam: str):
        #Отправляем почту ,в нее подаем 2 аргумена(почту и фамилию)
        #self.app.browser.implicitly_wait(10)
        time.sleep(3)
        with allure.step("Click"):
            self.find_element(self.POST_MAIL).click()
        with allure.step("Отправляем mail получателя"):
            self.find_element(self.POST_LOGIN1).send_keys(post_login)
        #здесь нужно отметьтить то ,что если сделать здесь задержку в отправке письма, то высветится окошко выбора mail, а оно перекрывает остальные окна
        #значит нужно реализовать код иначе, но так как это было замечено случайно , то лучше реализовать это потом

        search_field=self.find_element(self.CKE_WYSIWYG_DIV)
        with allure.step("Click"):
            search_field.click()
        with allure.step("В теле письма пишем"):
            search_field.send_keys(f"Количество писем: {self.countmails}")
        with allure.step("Заголовок пишем"):
            self.find_element(self.TEXT_FIELD).send_keys(f"Тестовое  задание.  {fam}")
        with allure.step("Click"):
            self.find_element(self.COMPOSE_SEND_BUTTON_DESKTOP).click()
        time.sleep(5)