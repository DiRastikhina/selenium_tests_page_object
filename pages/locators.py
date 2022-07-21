from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    
class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADDED_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner")
    SUM_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner p:first-child strong")