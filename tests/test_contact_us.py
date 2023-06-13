import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.contact_us import ContactUsPage


class ContactUs(unittest.TestCase):
    def setUp(self) -> None:
        option = webdriver.ChromeOptions()

        option.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
        self.driver.get("https://automationexercise.com/")

        self.contact_us = ContactUsPage(self.driver)

    def test_submit_message(self):
        self.contact_us.submit_message_on_contact_us("Piotr", "seleniumremote@gmail.com", "test", "test message")
        Alert(self.driver).accept()
        try:
            self.driver.find_element(By.CLASS_NAME, "status alert alert-success")
        except NoSuchElementException:
            return False
        return True
    def tearDown(self) -> None:
        self.driver.quit()
