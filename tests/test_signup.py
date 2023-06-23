import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.menu_page import MenuPage
from pages.sign_up_page import SignUpPage


class SignUp(unittest.TestCase):

    def setUp(self) -> None:
        option = webdriver.ChromeOptions()

        option.add_argument("--start-maximized")
        #self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
        self.driver = webdriver.Chrome('C:\\Users\mielpi1\Desktop\Python_Selenium\driver\chrome_driver\chromedriver.exe', options=option)
        self.driver.get("https://automationexercise.com/")

        self.sign_up_page = SignUpPage(self.driver)
        self.menu_page = MenuPage(self.driver)

    def test_create_account(self):
        # Given
        self.menu_page.open_login_page()
        # When
        self.sign_up_page.go_to_create_account_page("Piotr")
        self.sign_up_page.fill_required_data_on_create_account_form("1234", "Piotr", "Mielke", "Company", "Address",
                                                                    "State", "City", "12345", "12345678")
        self.sign_up_page.click_create_account_button()
        # Then
        self.sign_up_page.check_continue_button_is_displayed()
        self.sign_up_page.check_if_information_account_created_is_displayed()


    def tearDown(self) -> None:
        self.driver.quit()