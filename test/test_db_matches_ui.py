from model.contact import Contact
from model.group import Group

'''
def test_group_list(app, db):
    def clean(group):
        return Group(id=group.id, name=group.name.replace(" ", ""))

    db_list = map(clean, db.get_group_list())
    ui_list = map(clean, app.group.get_group_list())

    assert sorted(ui_list, key = Group.id_or_max) == sorted(db_list, key = Group.id_or_max)

'''


def test_contact_list(app, db):
    def clean(contact):
        return Group(id=contact.id, name=contact.firstname.replace(" ", ""))

    contact_db_list = list(map(clean, db.get_contact_list()))
    contact_ui_list = list(map(clean, app.contact.get_contact_list()))
    assert sorted(contact_ui_list, key = Group.id_or_max) == sorted(contact_db_list, key = Group.id_or_max)
