from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):  
    def add_product_into_basket(self):
        product_add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        product_add_button.click() 
        
    def product_added_message_exists(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_MESSAGE), f"There is no message that product is added"
     
    def check_name_of_added_book(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        message = self.browser.find_element(*ProductPageLocators.ADDED_MESSAGE).text
        assert message == book_name, f"There is no match {book_name} with message {message} in url {self.browser.current_url}"
        
    def price_book_in_basket_exists(self):
        assert self.is_element_present(*ProductPageLocators.SUM_BASKET), f"There is no message about sum in basket"
        
    def price_book_is_right(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        sum_basket = self.browser.find_element(*ProductPageLocators.SUM_BASKET).text
        assert book_price == sum_basket , f"Book price {book_price} doesn't match sum in basket {sum_basket}"
           
    def should_be_success_messages(self):
        self.product_added_message_exists() 
        self.check_name_of_added_book()
        self.price_book_in_basket_exists()
        self.price_book_is_right()
    