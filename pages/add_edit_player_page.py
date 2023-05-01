from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Player(BasePage):
    expected_title = "Add player"
    expected_title_xpath = "//span[text()='Add player']"
    header_title_after_add_player = "Edit player Jan Kowalski"
    header_of_box_after_add_player_xpath = "//span[text()='Edit player Jan Kowalski']"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    matches_xpath = "//span[text()='Matches']"
    email_xpath = "//input[@name='email']"
    name_xpath = "//input[@name='name']"
    surname_xpath = "//input[@name='surname']"
    phone_xpath = "//input[@name='phone']"
    weight_xpath = "//input[@name='weight']"
    height_xpath = "//input[@name='height']"
    age_xpath = "//input[@name='age']"
    leg_dropdown_xpath = "//div[@id='mui-component-select-leg']"
    right_leg_xpath = "//li[@data-value='right']"
    left_leg_xpath = "//li[@data-value='left']"
    club_xpath = "//input[@name='club']"
    level_xpath = "//input[@name='level']"
    main_position_xpath = "//input[@name='mainPosition']"
    second_position_xpath = "//input[@name='secondPosition']"
    district_dropdown_xpath = "//div[@id='mui-component-select-district']"
    masovia_xpath = "//li[@data-value='mazowieckie']"
    warmia_and_mazuria_xpath = "//li[@data-value='warminsko-mazurskie']"
    less_poland_xpath = "//li[@data-value='malopolskie']"
    lublin_xpath = "//li[@data-value='lubelskie']"
    west_pomerania_xpath = "//li[@data-value='zachodniopomorskie']"
    achievements_xpath = "//input[@name='achievements']"
    button_add_language_xpath = "//button[@aria-label='Add language']"
    button_add_link_to_youtube_xpath = "//button[@aria-label='Add link to Youtube']"
    button_submit_xpath = "//button[@type='submit']"
    button_clear_xpath = "//span[text()='Clear']"

    def check_title_of_page(self):
        self.wait_for_element_to_be_visible(self.expected_title_xpath)
        assert self.get_page_title() == self.expected_title

    def check_header_of_box_after_add_player(self):
        sleep(2)
        self.assert_element_text(self.driver, self.header_of_box_after_add_player_xpath,
                                 self.header_title_after_add_player)

    def type_email(self, email):
        self.field_send_keys(self.email_xpath, email)

    def type_name(self, name):
        self.field_send_keys(self.name_xpath, name)

    def type_surname(self, surname):
        self.field_send_keys(self.surname_xpath, surname)

    def type_phone(self, phone):
        self.field_send_keys(self.phone_xpath, phone)

    def type_weight(self, weight):
        self.field_send_keys(self.weight_xpath, weight)

    def type_height(self, height):
        self.field_send_keys(self.height_xpath, height)

    def type_age(self, age):
        self.field_send_keys(self.age_xpath, age)

    def choose_leg(self, leg):
        self.click_on_the_element(self.leg_dropdown_xpath)
        if leg == "right":
            self.click_on_the_element(self.right_leg_xpath)
        else:
            self.click_on_the_element(By.XPATH, self.left_leg_xpath)

    def type_club(self, club):
        self.field_send_keys(self.club_xpath, club)

    def choose_district(self, district):
        self.click_on_the_element(self.district_dropdown_xpath)
        if district == "Masovia":
            self.wait_for_element_to_be_clickable(self.masovia_xpath)
        elif district == "Warmia-Mazuria":
            self.wait_for_element_to_be_clickable(self.warmia_and_mazuria_xpath)
            # self.field_send_keys(self.warmia_and_mazuria_xpath, district)
        elif district == "Lesser Poland":
            self.wait_for_element_to_be_clickable(self.less_poland_xpath)
        elif district == "Lublin":
            self.wait_for_element_to_be_clickable(self.lublin_xpath)
        elif district == "West Pomerania":
            self.wait_for_element_to_be_clickable(self.west_pomerania_xpath)
        else:
            raise ValueError(f"Unrecognized district: {district}")
        self.district = district
        return district

    def check_district(self):
        sleep(2)
        self.assert_element(self.choose_district(self.district), "Warmia-Mazuria")

    def type_main_position(self, main_position):
        self.field_send_keys(self.main_position_xpath, main_position)

    def click_button_submit(self):
        self.wait_for_element_to_be_visible(self.button_submit_xpath)
        self.click_on_the_element(self.button_submit_xpath)

    def fill_in_form_add_player(self):
        self.type_name('Jan')
        self.type_surname('Kowalski')
        self.type_age('14.05.1994')
        self.type_main_position('Atak')
        self.click_button_submit()
        sleep(2)

    def edit_existing_player(self):
        self.type_email('mail@test.com')
        self.type_phone('123456789')
        self.type_weight('72')
        self.type_height('182')
        self.choose_leg("right")
        self.type_club('Klub piłkarski')
        self.choose_district('Warmia-Mazuria')
        # sleep(2)
        self.click_button_submit()
        # sleep(2)
