from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from pages.base_page import BasePage


class SidePanel(BasePage):
    main_page_xpath = "//span[text()='Main page']"
    players_xpath = "//span[text()='Players']"
    matches_xpath = "//span[text()='Matches']"
    reports_xpath = "//span[text()='Reports']"
    language_xpath = "//span[contains(@class,'MuiTypography-root')][text()='Polski']"
    sign_out_xpath = "//span[text()='Sign out']"

    def click_matches(self):
        self.click_on_the_element(self.matches_xpath)

    def click_sign_out(self):
        self.click_on_the_element(self.sign_out_xpath)
