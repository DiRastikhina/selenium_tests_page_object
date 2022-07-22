from .base_page import BasePage
from .locators import LoginPageLocators
import secrets
import string

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find("login") > -1, "Url doesn't have login in adress"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no login form in the page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "There is no register form in the page"
    
    def register_new_user(self,email, password):
        regmail = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        regmail.send_keys(email)
        
        regpass = self.browser.find_element(*LoginPageLocators.REGISTER_PASS)
        regpass.send_keys(password)
        
        regpass_repeat = self.browser.find_element(*LoginPageLocators.REGISTER_PASS_REPEAT)
        regpass_repeat.send_keys(password)
        
        regbutton = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        regbutton.click()
    
    def get_random_password(self,length):
        secure_str = ''.join((secrets.choice(string.ascii_letters) for i in range(10)))
        return secure_str