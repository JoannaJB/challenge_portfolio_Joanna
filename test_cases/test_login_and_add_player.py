import unittest

import pytest

from pages.add_edit_player_page import Player
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from test_cases.conftest import Setup


@pytest.mark.usefixtures("setup")
class TestLoginAndAddPlayer(unittest.TestCase, Setup):

    def test_login_and_add_player(self):
        user_login = LoginPage(self.driver)
        user_login.check_title_of_page()
        user_login.check_header_of_box()
        user_login.fill_in_login_form()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.check_title_of_page()
        dashboard_page.click_add_player()
        player = Player(self.driver)
        player.check_title_of_page()
        player.fill_in_form_add_player()
