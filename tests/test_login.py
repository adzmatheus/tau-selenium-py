"""
Testes que cobrem o login na Plataforma Rubeus
"""

import pytest

from pages.account_login import AccountLoginPage
from pages.account_ambientes import AccountAmbientesPage

@pytest.mark.parametrize("email,password",
    [("xaholisa@gmail.com", "123"),
    ("","")]
)
def test_account_rubeus_login(browser, email, password):

    login_page = AccountLoginPage(browser)
    ambientes_page = AccountAmbientesPage(browser)
 
    #Given the Account home page is open
    login_page.load()

    #When the user fill the email as "validEmail"
    #

    #And the user fill the password as "validPassword"
    login_page.login(email, password)

    #Then the user should be redirected to "Ambientes"
    assert len(ambientes_page.meus_ambientes()) > 0
    