from utils.xPath import Xpath
from .page import Page


class LoginPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        self.click_element('xpath', Xpath['Login'])
        self.find_element('xpath', Xpath['emailForm']).send_keys(email)
        self.find_element('xpath', Xpath['passwordForm']).send_keys(password)
        self.click_element('xpath', Xpath['loginButton'])

