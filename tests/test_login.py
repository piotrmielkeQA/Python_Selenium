import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.login import LoginPage


class Login(unittest.TestCase):
    def setUp(self) -> None:
        option = webdriver.ChromeOptions()

        option.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
        self.driver.get("https://automationexercise.com/")

        self.login_page = LoginPage(self.driver)

    def test_login_success(self):
        self.login_page.login_with_email_password("seleniumremote@gmail.com", "tester")
        self.login_page.logout()

    def test_login_failed(self):
        self.login_page.login_with_email_password("test@gmail.com", "tester")
        try:
            self.driver.find_element(By.XPATH, "//*[@style='color: red;']")
        except NoSuchElementException:
            return False
        return True

    def tearDown(self) -> None:
        self.driver.quit()
