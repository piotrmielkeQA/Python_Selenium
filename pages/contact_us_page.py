from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base import BasePage


class ContactUsPage(BasePage):
    contact_us_name_input_selector = (By.XPATH, "//input[@data-qa='name']")
    contact_us_email_input_selector = (By.XPATH, "//input[@data-qa='email']")
    contact_us_subject_input_selector = (By.XPATH, "//input[@data-qa='subject']")
    contact_us_textarea_selector = (By.XPATH, "//textarea[@data-qa='message']")
    contact_us_submit_button_selector = (By.XPATH, "//input[@data-qa='submit-button']")
    contact_us_alert_success_information = (By.XPATH, "//div[@class='status alert alert-success']")

    def fill_data_on_contact_us_form(self, name, email, subject, message):
        self.fill_name_field(name)
        self.fill_email_field(email)
        self.fill_subject_field(subject)
        self.fill_message_field(message)
        self.click_submit_button()

    def fill_name_field(self, name):
        self.driver.find_element(*self.contact_us_name_input_selector).send_keys(name)

    def fill_email_field(self, email):
        self.driver.find_element(*self.contact_us_email_input_selector).send_keys(email)

    def fill_subject_field(self, subject):
        self.driver.find_element(*self.contact_us_subject_input_selector).send_keys(subject)

    def fill_message_field(self, message):
        self.driver.find_element(*self.contact_us_textarea_selector).send_keys(message)

    def click_submit_button(self):
        self.driver.find_element(*self.contact_us_submit_button_selector).click()

    def check_alert_success_is_displayed(self):
        try:
            self.driver.find_element(*self.contact_us_alert_success_information)
        except NoSuchElementException:
            return False
        return True
