class LoginPage:
    def login(self, username, password):
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys(username)