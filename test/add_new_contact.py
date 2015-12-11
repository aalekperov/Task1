# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname = "Homer", middlename = "Jay", lastname = "Simpson", nickname = "simpson",
             photo_path = 'c:\\GitHub\\Task1\\res\\homer.jpg', title = "worker",
             company = "Springfield Nuclear Power Plant", company_address = "Springfield", home = "Springfield, 742 Evergreen Terrace",
             mobile_phone_num = "+1(123)456-67-89", work_phone_num = "+1(123)456-67-89", fax_num = "+1(123)456-67-89",
             email1 = "homer.simpson@fox.tv", email2 = "homer.simpson@fox.tv", email3 = "", homepage = "http://simpsons.com",
             birthday_d = "12", birthday_m = "May", birthday_y = "1959",
             anniversary_d = "10", anniversary_m = "May", anniversary_y = "1957",
             second_address = "Springfield", second_home = "742 Evergreen Terrace", notes = "No comments"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


