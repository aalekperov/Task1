# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname = "Homer", middlename = "Jay", lastname = "Simpson", nickname = "simpson",
             photo_path = 'c:\\GitHub\\Task1\\res\\homer.jpg', title = "worker",
             company = "Springfield Nuclear Power Plant", company_address = "Springfield", home = "+1(123)456-67-00",
             mobile_phone_num = "+1(123)456-67-89", work_phone_num = "+1(123)456-67-88", fax_num = "+1(123)456-67-87",
             email1 = "homer.simpson@fox.tv", email2 = "homer.simpson2@fox.tv", email3 = "homer.simpson3@fox.tv", homepage = "http://simpsons.com",
             birthday_d = "12", birthday_m = "May", birthday_y = "1959",
             anniversary_d = "10", anniversary_m = "May", anniversary_y = "1957",
             second_address = "Springfield", second_home = "+1(123)456-67-05", notes = "No comments")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


