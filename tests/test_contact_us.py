import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.contact_us import ContactUsPage


class ContactUs(unittest.TestCase):
    def setUp(self) -> None:
        option = webdriver.ChromeOptions()
        option.add_argument("--headless")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
        self.driver.get("https://automationexercise.com/")

        self.contact_us = ContactUsPage(self.driver)


    def test_submit_message(self):
        self.contact_us.submit_message_on_contact_us("Piotr", "seleniumremote@gmail.com", "test", "test message")



