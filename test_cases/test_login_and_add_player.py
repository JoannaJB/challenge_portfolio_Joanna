import os
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.add_edit_player_page import Player
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from pages.side_panel import SidePanel
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginAndAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        # Create a new instance of the WebDriver and open browser
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

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
        side_panel = SidePanel(self.driver)
        side_panel.click_main_page()
        dashboard_page.check_last_created_player()

    @classmethod
    def tearDown(self):
        self.driver.quit()
