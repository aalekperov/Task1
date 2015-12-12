__author__ = 'Atash'

from model.contact import Contact


def test_add_modify_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname = "Homer1", lastname="Simpson1", birthday_d = "19")
    if app.contact.count() == 0:
        app.contact.create(contact)
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




