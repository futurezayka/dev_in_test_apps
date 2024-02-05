import pytest
from selenium.common import NoSuchElementException
from time import sleep
from framework import LoginPage
from utils.xPath import Xpath


@pytest.mark.parametrize("email, password, element", [
    ('qa.ajax.app.automation@gmail.com', '111111111', 'addHubButton'),
])
def test_wrong(driver, email, password, element, logger):
    user_login(driver, email, password, element, logger)


@pytest.mark.parametrize("email, password, element", [
    ('qa.ajax.app.automation@gmail.com', 'qa_automation_password', 'addHubButton'),
])
def test_success(driver, email, password, element, logger):
    user_login(driver, email, password, element, logger)


def user_login(driver, email, password, element, logger):
    logger.info(f"\n\nStarting test for user: {email} password: {password}")
    login_page = LoginPage(driver)

    try:
        logger.info("Attempting login...")
        sleep(3)
        login_page.login(email, password)
        sleep(3)
        assert login_page.find_element('xpath', Xpath[element]).is_enabled()

        logger.info('Test passed')

    except (NoSuchElementException, AssertionError) as e:
        logger.info(f"Login failed with exception: {e}")
        raise
