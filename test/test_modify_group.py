__author__ = 'Atash'

from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    app.group.modify(Group(name="Modified group"))
