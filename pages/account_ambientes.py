"""
Este modulo contem o POM da pagina de Ambientes do Account
"""

from selenium.webdriver.common.by import By

class AccountAmbientesPage:

    AMBIENTES = (By.XPATH, "(//div[@class='listItem'])")
    SEARCH_INPUT = (By.XPATH, "//input[@class='search-class-input']")

    def __init__(self, browser):
        self.browser = browser

    def meus_ambientes(self):
        ambientes = self.browser.find_elements(*self.AMBIENTES)
        meus_ambientes = [ambiente.text for ambiente in ambientes]
        return meus_ambientes

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title
