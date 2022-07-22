from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.login
class TestLoginFromProductPage():
    #для работы с API используем такой код
    #@pytest.fixture(scope="function", autouse=True)
    #def setup(self):
    #    self.product = ProductFactory(title = "Best book created by robot")
        # создаем по апи
    #    self.link = self.product.link
    #    yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали 
    #    self.product.delete()
        
    def test_guest_can_go_to_login_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser,link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser,link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_if_empty_basket()
    