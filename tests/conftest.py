"""
This module contains shared fixtures
"""

import json
import pytest
import selenium.webdriver



@pytest.fixture
def config(scope='session'):
    
    # Read config file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert config['type'] in ['local', 'remote']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return a dictionary of configs
    return config



@pytest.fixture
def browser(config):

    #Inicializa uma instancia do WebDriver
    if config['browser'] == 'Firefox':
        b.selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["Browser"]}" is not supported')

    #Faz o navegador esperar até 10s pro elemento aparecer
    b.implicitly_wait(config['implicit_wait'])

    #Retorna a instancia do webdriver para configuracao
    yield b

    #Sai da instancia do WebDriver (limpa ao fim do teste)
    b.quit()