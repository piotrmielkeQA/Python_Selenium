from hashlib import new

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from data_generator.email_generator import EmailGenerator
from pages.base import BasePage


class SignUpPage(BasePage):
    sign_up_name_input_selector = (By.XPATH, "//input[@data-qa='signup-name']")
    sign_up_email_input_selector = (By.XPATH, "//input[@data-qa='signup-email']")
    sign_up_button_selector = (By.XPATH, "//input[@data-qa='signup-email']")
    sign_up_title_input_selector = (By.XPATH, "//input[@id='id_gender1']")
    sign_up_password_input_selector = (By.XPATH, "//input[@id='password']")
    sign_up_day_of_birth_select_selector = (By.XPATH, "//select[@id='days']")
    sign_up_month_of_birth_select_selector = (By.XPATH, "//select[@id='months']")
    sign_up_year_of_birth_select_selector = (By.XPATH, "//select[@id='years']")
    sign_up_first_name_input_selector = (By.XPATH, "//input[@id='first_name']")
    sign_up_last_name_input_selector = (By.XPATH, "//input[@id='last_name']")
    sign_up_company_input_selector = (By.XPATH, "//input[@id='company']")
    sign_up_address_input_selector = (By.XPATH, "//input[@id='address1']")
    sign_up_country_input_selector = (By.XPATH, "//select[@id='country']")
    sign_up_state_input_selector = (By.XPATH, "//input[@id='state']")
    sign_up_city_input_selector = (By.XPATH, "//input[@id='city']")
    sign_up_zipcode_input_selector = (By.XPATH, "//input[@id='zipcode']")
    sign_up_mobile_number_input_selector = (By.XPATH, "//input[@id='mobile_number']")
    sign_up_create_account_button_selector = (By.XPATH, "//button[@data-qa='create-account']")
    sign_up_continue_button_selector = (By.XPATH, "//a[@data-qa='continue-button']")
    sign_up_account_created_information = (By.XPATH, "//h2[@data-qa='account-created']")

    def go_to_create_account_page(self, name):
        self.fill_name_field(name)
        self.fill_email_field()
        self.click_sign_up_button()

    def fill_required_data_on_create_account_form(self, password, first_name, last_name, company, address, state, city,
                                                  zipcode, mobile_number):
        self.select_title()
        self.fill_password(password)
        self.select_day_of_birth()
        self.select_month_of_birth()
        self.select_year_of_birth()
        self.fill_first_name_field(first_name)
        self.fill_last_name_field(last_name)
        self.fill_company_field(company)
        self.fill_address_field(address)
        self.select_country()
        self.fill_state_field(state)
        self.fill_city_field(city)
        self.fill_zipcode_field(zipcode)
        self.fill_mobile_number_field(mobile_number)

    def fill_name_field(self, name):
        self.driver.find_element(*self.sign_up_name_input_selector).send_keys(name)

    def fill_email_field(self):
        email_generator = EmailGenerator
        self.driver.find_element(*self.sign_up_email_input_selector).send_keys(email_generator.random_email(self, 5))

    def click_sign_up_button(self):
        self.driver.find_element(*self.sign_up_button_selector).submit()

    def select_title(self):
        self.driver.find_element(*self.sign_up_title_input_selector).click()

    def fill_password(self, password):
        self.driver.find_element(*self.sign_up_password_input_selector).send_keys(password)

    def select_day_of_birth(self):
        # identify dropdown with Select class
        sel = Select(self.driver.find_element(*self.sign_up_day_of_birth_select_selector))
        # select by select_by_visible_text() method
        sel.select_by_value("2")

    def select_month_of_birth(self):
        # identify dropdown with Select class
        sel = Select(self.driver.find_element(*self.sign_up_month_of_birth_select_selector))
        sel.select_by_value("5")

    def select_year_of_birth(self):
        # identify dropdown with Select class
        sel = Select(self.driver.find_element(*self.sign_up_year_of_birth_select_selector))
        # select by select_by_visible_text() method
        sel.select_by_value("2020")

    def fill_first_name_field(self, first_name):
        self.driver.find_element(*self.sign_up_first_name_input_selector).send_keys(first_name)

    def fill_last_name_field(self, last_name):
        self.driver.find_element(*self.sign_up_last_name_input_selector).send_keys(last_name)

    def fill_company_field(self, company):
        self.driver.find_element(*self.sign_up_company_input_selector).send_keys(company)

    def fill_address_field(self, address):
        self.driver.find_element(*self.sign_up_address_input_selector).send_keys(address)

    def select_country(self):
        # identify dropdown with Select class
        sel = Select(self.driver.find_element(*self.sign_up_country_input_selector))
        # select by select_by_visible_text() method
        sel.select_by_value("Canada")

    def fill_state_field(self, state):
        self.driver.find_element(*self.sign_up_state_input_selector).send_keys(state)

    def fill_city_field(self, city):
        self.driver.find_element(*self.sign_up_city_input_selector).send_keys(city)

    def fill_zipcode_field(self, zipcode):
        self.driver.find_element(*self.sign_up_zipcode_input_selector).send_keys(zipcode)

    def fill_mobile_number_field(self, mobile_number):
        self.driver.find_element(*self.sign_up_mobile_number_input_selector).send_keys(mobile_number)

    def click_create_account_button(self):
        self.driver.find_element(*self.sign_up_create_account_button_selector).click()

    def check_continue_button_is_displayed(self):
        try:
            self.driver.find_element(*self.sign_up_continue_button_selector)
        except NoSuchElementException:
            return False
        return True

    def check_if_information_account_created_is_displayed(self):
        try:
            self.driver.find_element(*self.sign_up_account_created_information)
        except NoSuchElementException:
            return False
        return True
