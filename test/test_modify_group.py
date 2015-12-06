__author__ = 'Atash'

from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="Modified group"))
    app.session.logout()