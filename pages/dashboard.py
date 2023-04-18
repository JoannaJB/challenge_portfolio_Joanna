from time import sleep

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"
    main_page_xpath = "//span[text()='Main page']"
    players_xpath = "//span[text()='Players']"
    language_xpath = "//span[contains(@class,'MuiTypography-root')][text()='Polski']"
    sing_out_xpath = "//span[text()='Sign out']"
    dev_team_contact_xpath = "//span[text()='Dev team contact']"
    add_player_xpath = "//span[text()='Add player']"
    last_created_player_xpath = "//h6[text()='Last created player']//..//a[1]"
    last_update_player_xpath = "//h6[text()='Last updated player']//..//a[2]"
    last_created_match_xpath = "//h6[text()='Last created match']//..//a[3]"
    last_updated_match_xpath = "//h6[text()='Last updated match']//..//a[4]"
    last_updated_report_xpath = "//h6[text()='Last updated report']//..//a[5]"

    def title_of_page(self):
        sleep(2)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_add_player(self):
        self.click_on_the_element(self.add_player_xpath)

