from abc import ABC

# Abstracao do POM (Page Object Model)

# Browser
class SeleniumObject:
    def find_element(self, locator):
        return self.browser.find_element(*locator)

    def find_elements(self, locator):
        return self.browser.find_elements(*locator)


# # Page
# class Page(ABC, SeleniumObject):
#     def __init__(self, browser, url=''):
#         self.browser = browser
#         self.url = url
#         self._reflection()

#     def load(self):
#         self.browser.get(self.url)

#     def _reflection(self):
#         for attribute in dir(self):
#             real_attribute = getattr(self, attribute)
#             if isinstance(real_attribute, PageElement):
#                 real_attribute.browser = self.browser


# # Element
# class PageElement(ABC, SeleniumObject):
#     def __init__(self, browser=None):
#         self.browser = browser