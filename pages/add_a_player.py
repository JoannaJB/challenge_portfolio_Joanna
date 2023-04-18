from time import sleep

from pages.base_page import BasePage

class AddPlayer(BasePage):
    expected_title = "Add player"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    email_xpath = "//input[@name='email']"
    name_xpath = "//input[@name='name']"
    surname_xpath = "//input[@name='surname']"
    phone_xpath = "//input[@name='phone']"
    weight_xpath = "//input[@name='weight']"
    height_xpath = "//input[@name='height']"
    age_xpath = "//input[@name='age']"
    leg_xpath = "//div[@id='mui-component-select-leg']"
    club_xpath = "//input[@name='club']"
    level_xpath = "//input[@name='level']"
    main_position_xpath = "//input[@name='mainPosition']"
    second_position_xpath = "//input[@name='secondPosition']"
    district_xpath = "//div[@id='mui-component-select-district']"
    achievements_xpath = "//input[@name='achievements']"
    button_add_language_xpath = "//button[@aria-label='Add language']"
    button_add_link_to_youtube_xpath = "//button[@aria-label='Add link to Youtube']"
    button_submit_xpath = "//button[@type='submit']"
    button_clear_xpath = "//span[text()='Clear']"

    def title_of_page(self):
        # sleep(5)
        assert self.get_page_title(self.add_player_url) == self.expected_title

    def type_email(self, email):
        self.field_send_keys(self.email_xpath, email)

    def type_name(self, name):
        self.field_send_keys(self.name_xpath, name)

    def type_surname(self, surname):
        self.field_send_keys(self.surname_xpath, surname)

    def type_age(self, age):
        self.field_send_keys(self.age_xpath, age)

    def type_main_position(self, main_position):
        self.field_send_keys(self.main_position_xpath, main_position)

    def click_button_submit(self):
        self.click_on_the_element(self.button_submit_xpath)

    def fill_in_form_add_player(self):
        self.type_email('mail@test.com')
        self.type_name('Jan')
        self.type_surname('Kowalski')
        self.type_age('14.05.1994')
        self.type_main_position('atak')
        self.click_button_submit()
        sleep(4)

