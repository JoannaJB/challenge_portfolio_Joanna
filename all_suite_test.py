import unittest

from unittest.loader import makeSuite

from test_cases.test_add_match import TestLoginAndAddPlayerAddMatch
from test_cases.test_login_add_player_and_edit import TestLoginAndAddPlayerAndEdit
from test_cases.test_login_and_add_player import TestLoginAndAddPlayer
from test_cases.test_login_to_the_system import TestLoginPage
from test_cases.test_login_to_the_system_fail_data import TestLoginPageFailData


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginAndAddPlayerAddMatch))
    test_suite.addTest(makeSuite(TestLoginAndAddPlayerAndEdit))
    test_suite.addTest(makeSuite(TestLoginAndAddPlayer))
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestLoginPageFailData))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
