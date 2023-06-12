from selenium.webdriver.common.by import By

from pages.base import BasePage


class ContactUsPage(BasePage):
    contact_us_tab_selector = (By.XPATH, "//*[@href='/contact_us']")
    name_field_selector = (By.CSS_SELECTOR, "input[data-qa='name']")
    email_field_selector = (By.CSS_SELECTOR, "input[data-qa='email']")
    subject_field_selector = (By.CSS_SELECTOR, "input[data-qa='subject']")
    message_field_selector = (By.CSS_SELECTOR, "textarea[data-qa='message']")
    submit_button_selector = (By.CSS_SELECTOR, "input[data-qa='submit-button']")
    alert_success_information = (By.CLASS_NAME, "alert-success")

    def submit_message_on_contact_us(self, name, email, subject, message):
        self.driver.find_element(*self.contact_us_tab_selector).click()
        self.driver.find_element(*self.name_field_selector).send_keys(name)
        self.driver.find_element(*self.email_field_selector).send_keys(email)
        self.driver.find_element(*self.subject_field_selector).send_keys(subject)
        self.driver.find_element(*self.message_field_selector).send_keys(message)
        self.driver.find_element(*self.submit_button_selector).click()





