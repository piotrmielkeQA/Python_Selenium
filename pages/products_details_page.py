from selenium.webdriver.common.by import By

from data_generator.email_generator import EmailGenerator
from pages.base import BasePage


class ProductsDetailsPage(BasePage):
    product_details_name_input_selector = (By.XPATH, "//input[@id='name']")
    product_details_email_input_selector = (By.XPATH, "//input[@id='email']")
    product_details_review_textarea_selector = (By.XPATH, "//textarea[@id='review']")
    product_details_submit_button_selector = (By.XPATH, "//button[@id='button-review']")

    def fill_name_field(self, name):
        self.driver.find_element(*self.product_details_name_input_selector).send_keys(name)

    def fill_email_field(self):
        email_generator = EmailGenerator
        self.driver.find_element(*self.product_details_email_input_selector).send_keys(email_generator.random_email(self, 5))

    def fill_review_field(self, review):
        self.driver.find_element(*self.product_details_review_textarea_selector).send_keys(review)

    def click_submit_review_button(self):
        self.driver.find_element(*self.product_details_submit_button_selector).submit()

    def fill_data_on_review_product(self, name, review):
        self.fill_name_field(name)
        self.fill_email_field()
        self.fill_review_field(review)

    
