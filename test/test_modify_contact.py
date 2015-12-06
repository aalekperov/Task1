__author__ = 'Atash'

from model.contact import Contact


def test_add_new_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "Homer Simpson"))
    app.contact.modify(Contact(firstname = "Homer1", birthday_d = "19"))


