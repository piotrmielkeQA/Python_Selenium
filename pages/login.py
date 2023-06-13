from selenium.webdriver.common.by import By

from pages.base import BasePage


class LoginPage(BasePage):
    login_tab_selector = (By.CSS_SELECTOR, "a[href='/login']")
    email_field_selector = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    password_field_selector = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    login_button_selector = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    login_fail_information_selector = (By.CLASS_NAME, "color: red")
    logout_button_selector = (By.XPATH, "//*[@href='/logout']")

    def login_with_email_password(self, email, password):
        self.driver.find_element(*self.login_tab_selector).click()
        self.driver.find_element(*self.email_field_selector).send_keys(email)
        self.driver.find_element(*self.password_field_selector).send_keys(password)
        self.driver.find_element(*self.login_button_selector).click()

    def logout(self):
        self.driver.find_element(*self.login_fail_information_selector).click()



