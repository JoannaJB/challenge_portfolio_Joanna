import os
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.add_edit_player_page import Player
from pages.add_match_page import AddMatch
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from pages.side_panel import SidePanel
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginAndAddPlayerAddMatch(unittest.TestCase):

    @classmethod
    def setUp(self):
        # Create a new instance of the WebDriver and open browser
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_add_player_add_match(self):
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
        player.check_header_of_box_after_add_player()
        side_panel = SidePanel(self.driver)
        side_panel.click_matches()
        match = AddMatch(self.driver)
        match.click_add_match()
        match.check_header_of_box_add_a_match()
        match.fill_in_match_form()
        match.check_visibility_table_after_add_match()

    @classmethod
    def tearDown(self):
        self.driver.quit()
