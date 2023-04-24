from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AddMatch(BasePage):
    add_match_button = "//span[text()='Add match']"
    header_of_box_add_a_match_xpath = "//div[@class='MuiCardHeader-content']//span"
    header_title_add_match = "Adding match player Jan Kowalski"
    matches_xpath = "//span[text()='Matches']"
    reports_xpath = "//span[text()='Reports']"
    table_after_add_match_xpath = "//tr[@class='MuiTableRow-root']"
    my_team_in_table_xpath = "//td[1]"

    my_team_xpath = "//input[@name='myTeam']"
    enemy_team_xpath = "//input[@name='enemyTeam']"
    my_team_score_xpath = "//input[@name='myTeamScore']"
    enemy_team_score_xpath = "//input[@name='enemyTeamScore']"
    date_xpath = "//input[@name='date']"
    match_at_home_xpath = "//span[text()='Match at home']"
    match_out_home_xpath = "//span[text()='Match out home']"
    tshirt_color_xpath = "//input[@name='tshirt']"
    league_xpath = "//input[@name='league']"
    time_played_xpath = "//input[@name='timePlayed']"
    number_xpath = "//input[@name='number']"
    web_match_xpath = "//input[@name='webMatch']"
    general_xpath = "//input[@name='general']"
    rating_xpath = "//input[@name='rating']"
    submit_button_xpath = "//span[text()='Submit']"
    clear_button_xpath = "//span[text()='Clear']"

    def click_add_match(self):
        self.click_on_the_element(self.add_match_button)

    def check_header_of_box_add_a_match(self):
        sleep(2)
        self.assert_element_text(self.driver, self.header_of_box_add_a_match_xpath, self.header_title_add_match)

    def type_my_team(self, my_team):
        self.field_send_keys(self.my_team_xpath, my_team)
        self.my_team = my_team
        return my_team

    def type_enemy_team(self, enemy_team):
        self.field_send_keys(self.enemy_team_xpath, enemy_team)

    def type_my_team_score(self, my_team_score):
        self.field_send_keys(self.my_team_score_xpath, my_team_score)

    def type_enemy_team_score(self, enemy_team_score):
        self.field_send_keys(self.enemy_team_score_xpath, enemy_team_score)

    def type_date(self, date):
        self.field_send_keys(self.date_xpath, date)

    def click_button_submit(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)

    def fill_in_match_form(self):
        self.type_my_team("Drużyna Wygrana")
        self.type_enemy_team("Drużyna Przegrana")
        self.type_my_team_score("3")
        self.type_enemy_team_score("0")
        self.type_date('17-06-2022')
        self.click_button_submit()
        sleep(3)

    def check_visibility_table_after_add_match(self):
        table = self.wait_for_element_to_be_visible(self.table_after_add_match_xpath)
        self.assert_element_text(self.driver, self.my_team_in_table_xpath, self.my_team)
        print(f"Widoczna tabela z poprawną {self.my_team}")
