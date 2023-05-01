import os
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPageFailData(unittest.TestCase):

    @classmethod
    def setUp(self):
        # Create a new instance of the WebDriver and open browser
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_to_the_system_fail_data(self):
        user_login = LoginPage(self.driver)
        user_login.check_title_of_page()
        user_login.check_header_of_box()
        user_login.fill_in_login_form_fail_data()
        user_login.check_text_invalid_login_password()

    @classmethod
    def tearDown(self):
        self.driver.quit()
