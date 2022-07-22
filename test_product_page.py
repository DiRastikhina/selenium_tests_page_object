from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import time

def generate_link():
    link_list=[]
    link_base = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    for i in range(10):
        if i == 7:
             link = pytest.param((link_base + str(i)), marks=pytest.mark.xfail)
        else:
             link = link_base + str(i) 
        link_list.append(link)
    return link_list

class TestGuestAddToBasketFromProductPage():
    @pytest.mark.need_review
    @pytest.mark.parametrize('link', generate_link())
    def test_guest_can_add_product_to_basket(self,browser, link):
        page = ProductPage(browser,link)
        page.open()
        page.add_product_into_basket()
        page.solve_quiz_and_get_code()
        page.should_be_success_messages()
    
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser,link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_if_empty_basket()
    
    @pytest.mark.need_review    
    def test_guest_can_go_to_login_page_from_product_page (self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser,link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = str(time.time()) + "@fakemail.org"
        password = login_page.get_random_password(9)
        login_page.register_new_user(email,password)
        login_page.should_be_authorized_user()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser,link)
        page.open()
        page.add_product_into_basket()
        page.solve_quiz_and_get_code()
        page.should_be_success_messages()

    @pytest.mark.need_review
    def test_user_cant_see_product_in_basket_opened_from_product_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser,link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_if_empty_basket()
    