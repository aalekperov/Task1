# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
import os
import unittest
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class add_new_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def add_new_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def create_contact(self, contact):
        wd = self.wd
        self.add_new_contact_page()
        # fill new contact form
        # add first name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        # add middle name
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        # add last name
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # add nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # add photo
        # Почему-то не удается загрузить фото
        wd.find_element_by_name("photo").send_keys(os.getcwd()+contact.photo_path)
        # add title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        # add company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        # add company address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.company_address)
        # add home
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        # add mobile number
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone_num)
        # add work number
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone_num)
        # add fax number
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax_num)
        # add e-mail
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email1)
        # add e-mail2
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        # add e-mail3
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        # add homepage
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)

        # select birthday day
        Birthday_Dropdownlist_day = Select(wd.find_element_by_name("bday"))
        Birthday_Dropdownlist_day.select_by_visible_text(contact.birthday_d)
        # select birthday month
        Birthday_Dropdownlist_month = Select(wd.find_element_by_name("bmonth"))
        Birthday_Dropdownlist_month.select_by_visible_text(contact.birthday_m)
        # select birthday year
        wd.find_element_by_name("byear").send_keys(contact.anniversary_y)

        # select anniversary day
        Ann_Dropdownlist_day = Select(wd.find_element_by_name("aday"))
        Ann_Dropdownlist_day.select_by_visible_text(contact.anniversary_d)
        # select anniversary month
        Ann_Dropdownlist_month = Select(wd.find_element_by_name("amonth"))
        Ann_Dropdownlist_month.select_by_visible_text(contact.anniversary_m)
        # select anniversary year
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_y)

        # add second address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.second_address)
        # add home address 2
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.second_home)
        # add notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit adding new contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_home_page()

    def return_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()


    def test_add_new_contact(self):

        self.login(username="admin", password="secret")
        self.create_contact(Contact(firstname = "Homer", middlename = "Jay", lastname = "Simpson", nickname = "simpson",
                 photo_path = 'c:\\GitHub\\Task1\\res\\homer.jpg', title = "worker",
                 company = "Springfield Nuclear Power Plant", company_address = "Springfield", home = "Springfield, 742 Evergreen Terrace",
                 mobile_phone_num = "+1(123)456-67-89", work_phone_num = "+1(123)456-67-89", fax_num = "+1(123)456-67-89",
                 email1 = "homer.simpson@fox.tv", email2 = "homer.simpson@fox.tv", email3 = "", homepage = "http://simpsons.com",
                 birthday_d = "12", birthday_m = "May", birthday_y = "1959",
                 anniversary_d = "10", anniversary_m = "May", anniversary_y = "1957",
                 second_address = "Springfield", second_home = "742 Evergreen Terrace", notes = "No comments"))
        self.logout()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
