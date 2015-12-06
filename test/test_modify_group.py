__author__ = 'Atash'

from model.group import Group


def test_modify_group(app):
    app.group.modify(Group(name="Modified group"))
