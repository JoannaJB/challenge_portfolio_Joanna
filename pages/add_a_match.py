from pages.base_page import BasePage


class AddMatch(BasePage):
    matches_xpath = "//span[text()='Matches']"
    reports_xpath = "//span[text()='Reports']"
    my_team_field_xpath = "//input[@name='myTeam']"
    enemy_team_field_xpath = "//input[@name='enemyTeam']"
    my_team_score_field_xpath = "//input[@name='myTeamScore']"
    enemy_team_score_field_xpath = "//input[@name='enemyTeamScore']"
    date_field_xpath = "//input[@name='date']"
    match_at_home_xpath = "//span[text()='Match at home']"
    match_out_home_xpath = "//span[text()='Match out home']"
    tshirt_color_field_xpath = "//input[@name='tshirt']"
    league_field_xpath = "//input[@name='league']"
    time_played_field_xpath = "//input[@name='timePlayed']"
    number_field_xpath = "//input[@name='number']"
    web_match_field_xpath = "//input[@name='webMatch']"
    general_field_xpath = "//input[@name='general']"
    rating_field_xpath = "//input[@name='rating']"
    submit_button_xpath = "//span[text()='Submit']"
    clear_button_xpath = "//span[text()='Clear']"
