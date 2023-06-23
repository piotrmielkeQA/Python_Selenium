from selenium.webdriver.common.by import By

from pages.base import BasePage


class MenuPage(BasePage):
    contact_us_tab_selector = (By.XPATH, "//a[@href='/contact_us']")
    login_tab_selector = (By.CSS_SELECTOR, "a[href='/login']")
    products_tab_selector = (By.XPATH, "//a[@href='/products']")

    def open_contact_us_page(self):
        self.driver.find_element(*self.contact_us_tab_selector).click()

    def open_login_page(self):
        self.driver.find_element(*self.login_tab_selector).click()

    def open_product_page(self):
        self.driver.find_element(*self.products_tab_selector).click()





