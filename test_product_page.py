from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest

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

@pytest.mark.parametrize('link', generate_link())
def test_guest_can_add_product_to_basket(browser, link):
   # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
   # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser,link)
    page.open()
    page.add_product_into_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_messages()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_if_empty_basket()
    