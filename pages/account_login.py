"""
Este modulo contem o POM da pagina de login do Account
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AccountLoginPage:

    URL = "https://login.rubeus.com.br/"

    # Locators
    EMAIL_INPUT = (By.XPATH, "(//input[@class='mdc-text-field__input'])[1]")
    PASSWORD_INPUT = (By.XPATH, "(//input[@class='mdc-text-field__input'])[2]")
    CONTINUAR_CONECTADO_INPUT = (By.XPATH, "//input[@id='remember-login-checkbox']")
    ENTRAR_BUTTON = (By.XPATH, "(//span[@class='mdc-button__ripple'])[2]")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def login(self, email, password):
        email_input = self.browser.find_element(*self.EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password + Keys.RETURN)

