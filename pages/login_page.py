from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base import BasePage


class LoginPage(BasePage):
    email_field_selector = (By.XPATH, "//input[@data-qa='login-email']")
    password_field_selector = (By.XPATH, "//input[@data-qa='login-password']")
    login_button_selector = (By.XPATH, "//button[@data-qa='login-button']")
    login_fail_information_selector = (By.XPATH, "//p[@style='color: red;']")
    logout_button_selector = (By.XPATH, "//a[@href='/logout']")

    def fill_data_to_login(self, email, password):
        self.fill_email_field(email)
        self.fill_password_field(password)

    def fill_email_field(self, email):
        self.driver.find_element(*self.email_field_selector).send_keys(email)

    def fill_password_field(self, password):
        self.driver.find_element(*self.password_field_selector).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button_selector).click()

    def click_button_logout(self):
        self.driver.find_element(*self.login_fail_information_selector).click()

    def check_logout_button_is_displayed(self):
        try:
            self.driver.find_element(*self.logout_button_selector)
        except NoSuchElementException:
            return False
        return True

    def check_alert_information_about_fail_logged(self):
        try:
            self.driver.find_element(*self.login_fail_information_selector)
        except NoSuchElementException:
            return False
        return True

