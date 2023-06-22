import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.contact_us_page import ContactUsPage
from utils.alert_handle import AlertHandle
from pages.menu_page import MenuPage


class ContactUs(unittest.TestCase):
    def setUp(self) -> None:
        option = webdriver.ChromeOptions()

        option.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
        self.driver.get("https://automationexercise.com/")

        self.contact_us_page = ContactUsPage(self.driver)
        self.menu_page = MenuPage(self.driver)

    def test_submit_message(self):
        # Given
        self.menu_page.open_contact_us_page()
        # When
        self.contact_us_page.fill_data_on_contact_us_form("Piotr", "seleniumremote@gmail.com", "test", "test message")
        AlertHandle.accept_alert(self)
        # Then
        self.contact_us_page.check_alert_success_is_displayed()

    def tearDown(self) -> None:
        self.driver.quit()
