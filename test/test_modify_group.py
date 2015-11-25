__author__ = 'Atash'

from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="Modified group", header="Modified group header", footer="Modified group footer"))
    app.session.logout()