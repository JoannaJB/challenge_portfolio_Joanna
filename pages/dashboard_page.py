from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from pages.base_page import BasePage


class Dashboard(BasePage):
    futbolowy_kolektyw_button_xpath = "//div[@title='Logo Scouts Panel']"
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"
    main_page_xpath = "//span[text()='Main page']"
    players_xpath = "//span[text()='Players']"
    language_xpath = "//span[contains(@class,'MuiTypography-root')][text()='Polski']"
    sign_out_xpath = "//span[text()='Sign out']"
    dev_team_contact_xpath = "//span[text()='Dev team contact']"
    add_player_xpath = "//span[text()='Add player']"
    last_created_player_xpath = "//h6[text()='Last created player']//..//a[1]"
    last_update_player_xpath = "//h6[text()='Last updated player']//..//a[2]"
    last_created_match_xpath = "//h6[text()='Last created match']//..//a[3]"
    last_updated_match_xpath = "//h6[text()='Last updated match']//..//a[4]"
    last_updated_report_xpath = "//h6[text()='Last updated report']//..//a[5]"
    wait = WebDriverWait(driver, 10)

    def check_title_of_page(self):
        self.wait_for_element_to_be_clickable(self.futbolowy_kolektyw_button_xpath)
        assert self.get_page_title() == self.expected_title
        sleep(2)

    def click_add_player(self):
        self.click_on_the_element(self.add_player_xpath)
