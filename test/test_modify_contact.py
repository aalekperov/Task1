__author__ = 'Atash'

from model.contact import Contact


def test_add_new_contact(app):
    app.contact.modify(Contact(firstname = "Homer1", birthday_d = "19"))


