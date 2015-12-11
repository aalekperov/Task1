__author__ = 'Atash'

from model.contact import Contact


def test_add_modify_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "Homer Simpson"))
    app.contact.modify(Contact(firstname = "Homer1", birthday_d = "19"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)



