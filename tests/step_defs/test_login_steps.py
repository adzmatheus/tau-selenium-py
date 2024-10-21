"""
Testes que cobrem o login com Account na Plataforma Rubeus
"""

import pytest
from pytest_bdd import scenario, scenarios, given, when, then, parsers

from pages.account_login import AccountLoginPage
from pages.account_ambientes import AccountAmbientesPage


scenarios('../features/account_login.feature')

# This function will be executed after all scenario steps
# @pytest.mark.parametrize(
#     ['email', 'password'],
#     [("matheusvieira@rubeus.com.br", "exemplo")]
# )
# @scenario('../features/account_login.feature', 'Login with right data')
# def test_right_login(email, password):
#     pass

# @scenario('../features/account_login.feature', 'Login with wrong data')
# def test_wrong_login():
#     pass

# Given steps (only this steps can be fixtures)
@given("the Account login page is displayed", target_fixture="account_login_page")
def account_login_page(browser):
    page = AccountLoginPage(browser)
    page.load()
    return page


# When steps
@when(parsers.parse('user fills email field with "{email}"'), converters={"email": str})
def fill_email(account_login_page, email):
    account_login_page.fill_email(email)

@when(parsers.parse('user fills password field with "{password}"'), converters={"password": str})
def fill_password(account_login_page, password):
    account_login_page.fill_password(password)

@when("user clicks Entrar")
def click_entrar(account_login_page):
    account_login_page.click_entrar()


# Then steps
@then("the Account environments page is displayed", target_fixture="account_ambientes_page")
def account_ambientes_page(browser):
    page = AccountAmbientesPage(browser)
    return page

@then("user has many listed environments")
def user_has_ambientes(account_ambientes_page):
    assert len(account_ambientes_page.meus_ambientes()) > 0

@then("the error message is displayed")
def snackbar_error(account_login_page):
    alert = account_login_page.message()
    assert "E-mail ou senha inválidos" in alert

# @pytest.mark.parametrize("email,password",
#     [("xaholisa@gmail.com", "123"),
#     ("","")]
# )
# def test_account_rubeus_login(browser, email, password):

#     login_page = AccountLoginPage(browser)
#     ambientes_page = AccountAmbientesPage(browser)
 
#     #Given the Account home page is open
#     login_page.load()

#     #When the user fill the email as "validEmail"
#     login_page.fill_email(email)

#     #And the user fill the password as "validPassword"
#     login_page.fill_password(password)

#     #And the user press ENTER after fill password
#     login_page.click_entrar()

#     #Then the user should be redirected to "Ambientes"
#     assert len(ambientes_page.meus_ambientes()) > 0
    