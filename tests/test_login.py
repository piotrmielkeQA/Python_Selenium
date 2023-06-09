import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.menu_page import MenuPage


class Login(unittest.TestCase):
    def setUp(self) -> None:
        option = webdriver.ChromeOptions()

        option.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
        self.driver.get("https://automationexercise.com/")

        self.login_page = LoginPage(self.driver)
        self.menu_page = MenuPage(self.driver)

    def test_login_success(self):
        # Given
        self.menu_page.open_login_page()
        # When
        self.login_page.fill_data_to_login("seleniumremote@gmail.com", "tester")
        self.login_page.click_login_button()
        # Then
        self.login_page.check_logout_button_is_displayed()

    def test_login_failed(self):
        # Given
        self.menu_page.open_login_page()
        # When
        self.login_page.fill_data_to_login("test@gmail.com", "tester")
        # Then
        self.login_page.check_alert_information_about_fail_logged()

    def tearDown(self) -> None:
        self.driver.quit()
