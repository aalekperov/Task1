# -*- coding: utf-8 -*-
from model.group import Group


def test_new_group_add(app):
    app.group.create(Group(name="New group", header="New group header", footer="New group footer"))
    app.session.logout()

def test_new_empty_group_add(app):
    app.group.create(Group(name="", header="", footer=""))
