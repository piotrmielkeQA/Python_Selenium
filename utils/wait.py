from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver
from selenium.webdriver.support import expected_conditions as ec


class Wait():
    def WaitForElement(self, element):
        wait = WebDriverWait(driver, 10)
        element = wait.until(ec.visibility_of_element_located(element))
        ActionChains(driver).move_to_element(element).perform()
