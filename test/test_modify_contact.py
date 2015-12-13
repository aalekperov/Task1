__author__ = 'Atash'
from random import randrange
from model.contact import Contact


def test_modify_some_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname = "Homer1", lastname="Simpson1", birthday_d = "19")
    if app.contact.count() == 0:
        app.contact.create(contact)
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




