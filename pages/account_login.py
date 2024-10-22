"""
Este modulo contem o POM da pagina de login do Account
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from libraries.pom import SeleniumObject

class AccountLoginPage(SeleniumObject):

    URL = "https://login.rubeus.com.br/"

    # Locators
    EMAIL_INPUT = (By.XPATH, "(//input[@class='mdc-text-field__input'])[1]")
    PASSWORD_INPUT = (By.XPATH, "(//input[@class='mdc-text-field__input'])[2]")
    CONTINUAR_CONECTADO_INPUT = (By.XPATH, "//input[@id='remember-login-checkbox']")
    ENTRAR_BUTTON = (By.XPATH, "//div[@class='mdc-form-field mdc-form__item'][contains(.,'Entrar')]")
    ERROR_MESSAGE = (By.XPATH, "//span[@class='textSnackbar'][contains(.,'E-mail ou senha inválidos.')]")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def fill_email(self, email):
        email_input = self.find_element(self.EMAIL_INPUT)
        email_input.send_keys(email)

    def fill_password(self, password):
        password_input = self.find_element(self.PASSWORD_INPUT)
        password_input.send_keys(password)

    def click_entrar(self, timeout=10):
        entrar = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((self.ENTRAR_BUTTON))
        )
        entrar.click()

    def message(self, timeout=10):
        snackbar = WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located((self.ERROR_MESSAGE))
        )
        return snackbar.text

    def press_enter_in_element(self, element=None):
        if element:
            element.send_keys(Keys.ENTER)
        else:
            self.browser.find_element(By.TAG_NAME, "body").send_keys(Keys.ENTER)
