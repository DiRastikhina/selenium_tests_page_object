from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

#class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    REGISTER_PASS = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    REGISTER_PASS_REPEAT = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    
class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADDED_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner")
    SUM_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner p:first-child strong")
    
class BasketPageLocators():
    MESSAGE_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCTS_INBASKET = (By.CSS_SELECTOR, ".col-sm-6.h3")