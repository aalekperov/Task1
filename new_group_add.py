# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from application_group import Application_Group
import unittest
from group import Group


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class new_group_add(unittest.TestCase):
    def setUp(self):
        self.app = Application_Group()


    def test_new_group_add(self):

        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="New group", header="New group header", footer="New group footer"))
        self.app.logout()

    def test_new_empty_group_add(self):

        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()


    def tearDown(self):
        self.app.wd.quit()

if __name__ == '__main__':
    unittest.main()
