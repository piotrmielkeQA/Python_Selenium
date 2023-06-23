from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base import BasePage
from utils.wait import Wait


class ProductsPage(BasePage):
    products_search_input_selector = (By.XPATH, "//input[@id='search_product']")
    products_search_submit_button_selector = (By.XPATH, "//button[@id='submit_search']")
    products_view_product_selector = (By.XPATH, "//a[@href='/product_details/1']")

    def fill_search_product_field(self, product_name):
        self.driver.find_element(*self.products_search_input_selector).send_keys(product_name)

    def click_submit_search_button(self):
        self.driver.find_element(*self.products_search_submit_button_selector).click()

    def go_to_view_product_view(self):
        self.driver.implicitly_wait(10)
        # self.driver.execute_script("window.scrollTo(0,document.querySelectorAll('//a[@href='/product_details/1'])")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.driver.find_element(*self.products_view_product_selector).click()

    def search_product_by_name(self, product_name):
        self.fill_search_product_field(product_name)
        self.click_submit_search_button()


