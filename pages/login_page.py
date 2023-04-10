from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//input[@id='password']"
    sign_in_button_xpath = "//span[text()='Sign in']"
    remind_password_xpath = "//a[text()='Remind password']"
    language_choice_xpath = "//div[@role='button']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
