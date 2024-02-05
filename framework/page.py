from time import sleep

from appium.webdriver.common.appiumby import AppiumBy


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, find_by: str, value):
        assert find_by.lower() in ['xpath', 'id', 'name']
        return self.driver.find_element(getattr(AppiumBy, find_by.upper()), value)

    def click_element(self, find_by: str, value):
        target_element = self.find_element(find_by, value)
        sleep(3)
        target_element.click()
