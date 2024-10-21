@account-login @web
Feature: Login Rubeus Account
    As a registered user
    User wants to login on the Account
    So user can access the environment list 

    # Background:
    #     Given the Account login page is displayed

    @right-user
    Scenario: Login with right data
        Given the Account login page is displayed
        When user fills email field with "matheusvieira@rubeus.com.br"
        And user fills password field with "exemplo"
        And user clicks Entrar
        Then the Account environments page is displayed
        And user has many listed environments

    @wrong-user
    Scenario Outline: Login with wrong data
        Given the Account login page is displayed
        When user fills email field with "<email>"
        And user fills password field with "<password>"
        And user clicks Entrar
        Then the error message is displayed

        Examples: Wrong_user
            |       email       |    password   |
            | wrong@mail.com    | 123           |
