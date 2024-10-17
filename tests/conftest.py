"""
This module contains shared fixtures
"""

import json
import pytest
import selenium.webdriver as webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



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
    assert isinstance(config['url_remote'], str)
    assert len(config['url_remote']) > 0
    assert isinstance(config['environment'], str)
    assert len(config['environment']) > 0

    # Return a dictionary of configs
    return config



@pytest.fixture
def browser(config):

    #Inicializa uma instancia do WebDriver
    if config['type'] == 'local':

        if config['browser'] == 'Firefox':
            opts = webdriver.FirefoxOptions()
            opts.add_argument('--window-size=1366,768')
            b.webdriver.Firefox(options=opts)
        elif config['browser'] == 'Chrome':
            opts = webdriver.ChromeOptions()
            opts.add_argument('--window-size=1366,768')
            b = webdriver.Chrome(options=opts)
        elif config['browser'] == 'Headless Chrome':
            opts = webdriver.ChromeOptions()
            opts.add_argument('headless')
            b = webdriver.Chrome(options=opts)
        else:
            raise Exception(f'Browser "{config["browser"]}" is not supported')
    
    elif config['type'] == 'remote':
        
        if config['browser'] == 'Firefox':
            opts = webdriver.FirefoxOptions()
        elif config['browser'] == 'Chrome':
            opts = webdriver.ChromeOptions()

        opts.add_argument('--no-sandbox')

        b = webdriver.Remote(
            command_executor = config['url_remote'],
            options=opts
        )

    else:
        raise Exception(f'Type "{config["type"]}" is not supported')

    #Faz o navegador esperar até 10s pro elemento aparecer
    b.implicitly_wait(config['implicit_wait'])

    #Retorna a instancia do webdriver para configuracao
    yield b

    #Sai da instancia do WebDriver (limpa ao fim do teste)
    b.quit()