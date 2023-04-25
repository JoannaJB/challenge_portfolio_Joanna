import os

import pytest
import pytest_html
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utils.settings import IMPLICITLY_WAIT, DRIVER_PATH


class Setup:
    @pytest.fixture(scope="class")
    def setup(self):
        # Create a new instance of the WebDriver and open browser
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        # Yield the driver so that it can be used in the test function
        yield self.driver

        # Quit the driver after the test finishes
        self.driver.quit()

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extras = getattr(report, "extras", [])
        if report.when == "call":
            # always add url to report
            extras.append(pytest_html.extras.url("https://scouts-test.futbolkolektyw.pl/en"))
            xfail = hasattr(report, "wasxfail")
            if (report.skipped and xfail) or (report.failed and not xfail):
                # only add additional html on failure
                request = item.funcargs['request']
                report_directory = os.path.dirname(request.config.option.htmlpath)
                # file name = str(int(round(time.time() * 1000))) + ".png"
                file_name = report.nodeid.replace("::", "_") + ".png"
                destination_file = os.path.join(report_directory, file_name)
                request.node.funcargs['driver'].save_screenshot(destination_file)
                # call.excinfo.value.driver.save_screenshot(destination_file)
                # driver.save_screenshot(destination_file)
                if file_name:
                    html = '<div><img src="%s" alt="Screenshot" style="width:300px;height=200px"' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name

                extras.append(pytest_html.extras.html(html))
            report.extras = extras

    def pytest_html_report_title(self, report):
        report.title = "Automated Test Report for the Scouts Panel"
