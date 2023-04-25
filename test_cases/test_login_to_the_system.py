import unittest

import pytest

from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from pages.side_panel import SidePanel
from test_cases.conftest import Setup


@pytest.mark.usefixtures("setup")
class TestLoginPage(unittest.TestCase, Setup):

    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.check_title_of_page()
        user_login.check_header_of_box()
        user_login.fill_in_login_form()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.check_title_of_page()
        side_panel = SidePanel(self.driver)
        side_panel.click_sign_out()
        user_login.check_header_of_box()
        user_login.check_remind_password()
