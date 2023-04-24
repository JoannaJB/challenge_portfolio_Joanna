import os

import pytest
import pytest_html
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    # Create a new instance of the WebDriver
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Set the browser window size
    # driver.set_window_size(1280, 800)

    # Yield the driver so that it can be used in the test function
    yield driver

    # Quit the driver after the test finishes
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("https://scouts-test.futbolkolektyw.pl/en"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            # file name = str(int(round(time.time() * 1000))) + ".png"
            file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="Screenshot" style="width:300px;height=200px"' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name

            extras.append(pytest_html.extras.html(html))
        report.extras = extras


def pytest_html_report_title(report):
    report.title = "Automated Test Report for the Scouts Panel"
