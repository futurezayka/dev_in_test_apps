from time import sleep
import pytest
from selenium.common import NoSuchElementException

from framework import LoginPage
from utils.xPath import Xpath, SideBar


@pytest.mark.parametrize("email, password", [
    ('qa.ajax.app.automation@gmail.com', 'qa_automation_password'),
])
def test_sidebar(driver, email, password, logger):
    logger.info('\n\nSidebar test started')
    page = LoginPage(driver)
    sleep(3)
    page.login(email, password)
    sleep(5)
    logger.info('Clicking on the sidebar drawer')
    page.click_element('xpath', Xpath['sidebarDrawer'])

    for element, xpath in SideBar.items():
        logger.info(f"Checking if sidebar element '{element}' is enabled")
        try:
            assert page.find_element('xpath', xpath).is_enabled()
        except (NoSuchElementException, AssertionError) as e:
            logger.info(f"Sidebar element {element} thrown an error: {e}")
            raise

    logger.info('Sidebar test completed successfully')
