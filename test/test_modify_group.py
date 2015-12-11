__author__ = 'Atash'

from model.group import Group


def test_modify_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    app.group.modify(Group(name="Modified group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)
