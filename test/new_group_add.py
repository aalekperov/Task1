# -*- coding: utf-8 -*-
from model.group import Group


def test_new_group_add(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="New group", header="New group header", footer="New group footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_new_empty_group_add(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)