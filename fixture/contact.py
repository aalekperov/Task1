__author__ = 'Atash'
from selenium.webdriver.support.ui import Select
import os
from model.contact import Contact


class ContatHelper:

    def __init__(self, app):
        self.app = app

    def add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # add first name
        self.change_field_value("firstname", contact.firstname)
        # add middle name
        self.change_field_value("middlename", contact.middlename)
        # add last name
        self.change_field_value("lastname", contact.lastname)
        # add nickname
        self.change_field_value("nickname", contact.nickname)
        # add photo
        #wd.find_element_by_name("photo").send_keys(os.getcwd() + contact.photo_path)
        # add title
        self.change_field_value("title", contact.title)
        # add company
        self.change_field_value("company", contact.company)
        # add company address
        self.change_field_value("address", contact.company_address)
        # add home
        self.change_field_value("home", contact.home)
        # add mobile number
        self.change_field_value("mobile", contact.mobile_phone_num)
        # add work number
        self.change_field_value("work", contact.work_phone_num)
        # add fax number
        self.change_field_value("fax", contact.fax_num)
        # add e-mail
        self.change_field_value("email", contact.email1)
        # add e-mail2
        self.change_field_value("email2", contact.email2)
        # add e-mail3
        self.change_field_value("email3", contact.email3)
        # add homepage
        self.change_field_value("homepage", contact.homepage)
        # select birthday
        self.select_birthday(contact.birthday_d, contact.birthday_m, contact.birthday_y)
        #select anniversary day
        self.select_anniversaryday(contact.anniversary_d, contact.anniversary_m, contact.anniversary_y)
        # add second address
        self.change_field_value("address2", contact.second_address)
        # add home address 2
        self.change_field_value("phone2", contact.second_home)
        # add notes
        self.change_field_value("notes", contact.notes)

    def select_anniversaryday(self, day, month, year):
        wd = self.app.wd
        if day is not None:
            Ann_Dropdownlist_day = Select(wd.find_element_by_name("aday"))
            Ann_Dropdownlist_day.select_by_visible_text(day)
        if month is not None:
            # select anniversary month
            Ann_Dropdownlist_month = Select(wd.find_element_by_name("amonth"))
            Ann_Dropdownlist_month.select_by_visible_text(month)
        if year is not None:
            # select anniversary year
            wd.find_element_by_name("ayear").send_keys(year)

    def select_birthday(self, day, month, year):
        wd = self.app.wd
        if day is not None:
            # select birthday day
            Birthday_Dropdownlist_day = Select(wd.find_element_by_name("bday"))
            Birthday_Dropdownlist_day.select_by_visible_text(day)
        if month is not None:
            # select birthday month
            Birthday_Dropdownlist_month = Select(wd.find_element_by_name("bmonth"))
            Birthday_Dropdownlist_month.select_by_visible_text(month)
        if year is not None:
            # select birthday year
            wd.find_element_by_name("byear").send_keys(year)

    def create(self, contact):
        wd = self.app.wd
        self.add_new_contact_page()
        self.fill_contact_form(contact)
        # submit adding new contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        #submit deleting
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_home_page()

    def modify(self, new_contact):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # click modify
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.fill_contact_form(new_contact)
        #submit update
        wd.find_element_by_name("update").click()
        self.return_home_page()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(id = id))
        return contacts

