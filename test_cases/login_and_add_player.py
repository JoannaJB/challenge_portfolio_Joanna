import os
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.add_a_player import AddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestLoginAndAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.fill_in_login_form()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_add_player()
        add_player = AddPlayer(self.driver)
        add_player.title_of_page()
        add_player.fill_in_form_add_player()
    @classmethod
    def tearDown(self):
        self.driver.quit()