from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.settings import DEFAULT_LOCATOR_TYPE


class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, locator, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, locator).send_keys(value)

    def click_on_the_element(self, locator, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, locator).click()

    def click_and_choose_element(self, locator, locator_type=By.XPATH):
        try:
            element = self.driver.find_element(locator_type, locator)
            element.click()
        except NoSuchElementException as e:
            print(f"Element not found: {locator} ({locator_type})")
            raise e
        except ElementNotInteractableException as e:
            print(f"Element not clickable: {locator} ({locator_type})")
            raise e

    def get_page_title(self):
        return self.driver.title

    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element

            :param driver: webdriver instance
            :param xpath: xpath to element with text to be observed
            :param expected_text: text what we expecting to be found
            :return: None
        """
        element = driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text
        print(element_text)
        print(expected_text)
        assert expected_text == element_text

    def assert_element(self, element, expected_element):
        print(element)
        print(expected_element)
        assert expected_element == element

    def wait_for_element_to_be_clickable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator))).click()

    def wait_for_element_to_be_visible(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((locator_type, locator)))
