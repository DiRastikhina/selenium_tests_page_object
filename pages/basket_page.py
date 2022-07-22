from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def check_if_empty_basket(self):
        self.check_empty_basket()
        self.check_empty_message_basket()
         
    def check_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_INBASKET), "There are some products in basket, but should not be"
         
    def check_empty_message_basket(self):
        basket_message = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY).text
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY), f"Message {basket_message} doesn't match expected string"
        