from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.finish_btn = (By.ID, "finish")
        self.complete_header = (By.CLASS_NAME, "complete-header")

    def fill_info(self, first, last, zip_code):
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(zip_code)
        self.driver.find_element(*self.continue_btn).click()

    def finish_order(self):
        self.driver.find_element(*self.finish_btn).click()

    def get_success_message(self):
        return self.driver.find_element(*self.complete_header).text