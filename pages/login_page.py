from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    expected_title = "Scouts panel - sign in"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//input[@id='password']"
    sign_in_button_xpath = "//span[text()='Sign in']"
    remind_password_xpath = "//a[text()='Remind password']"
    language_choice_xpath = "//div[@role='button']"
    header_title_of_box = "Scouts Panel"
    expected_header_of_box_xpath = "//h5"
    invalid_login_password_xpath = "//span[text()='Identifier or password invalid.']"

    def check_title_of_page(self):
        sleep(2)
        assert self.get_page_title() == self.expected_title

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_in_sign_in(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def fill_in_login_form(self):
        self.type_in_email("user10@getnada.com")
        self.type_in_password("Test-1234")
        self.click_in_sign_in()
        # sleep(3)

    def fill_in_login_form_fail_data(self):
        self.type_in_email("mail@gmail.com")
        self.type_in_password("Haslo000")
        self.click_in_sign_in()

    def check_header_of_box(self):
        sleep(2)
        self.assert_element_text(self.driver, self.expected_header_of_box_xpath, self.header_title_of_box)

    def check_remind_password(self):
        self.wait_for_element_to_be_visible(self.remind_password_xpath)

    def check_text_invalid_login_password(self):
        self.wait_for_element_to_be_visible(self.invalid_login_password_xpath)
        self.assert_element_text(self.driver, self.invalid_login_password_xpath, "Identifier or password invalid.")
        sleep(2)


