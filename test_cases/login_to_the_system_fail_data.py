import unittest

import pytest

from pages.login_page import LoginPage
from test_cases.conftest import Setup


@pytest.mark.usefixtures("setup")
class TestLoginPage(unittest.TestCase, Setup):

    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.check_title_of_page()
        user_login.check_header_of_box()
        user_login.fill_in_login_form_fail_data()
        user_login.check_text_invalid_login_password()
