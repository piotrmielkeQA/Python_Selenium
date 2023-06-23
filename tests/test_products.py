import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.menu_page import MenuPage
from pages.products_page import ProductsPage
from pages.products_details_page import ProductsDetailsPage


class Products(unittest.TestCase):

    def setUp(self) -> None:
        option = webdriver.ChromeOptions()

        option.add_argument("--start-maximized")
        #self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
        self.driver = webdriver.Chrome('C:\\Users\mielpi1\Desktop\Python_Selenium\driver\chrome_driver\chromedriver.exe', options=option)
        self.driver.get("https://automationexercise.com/")

        self.products_page = ProductsPage(self.driver)
        self.menu_page = MenuPage(self.driver)
        self.products_details_page = ProductsDetailsPage(self.driver)

    def test_add_review_on_product(self):
        # Given
        self.menu_page.open_product_page()
        self.driver.refresh()
        self.driver.implicitly_wait(10)
        self.menu_page.open_product_page()
        # When
        self.products_page.search_product_by_name("Blue Top")
        self.products_page.go_to_view_product_view()
        self.driver.implicitly_wait(10)
        self.products_details_page.fill_data_on_review_product("Piotr", "Good product")
        self.products_details_page.click_submit_review_button()
        # Then
