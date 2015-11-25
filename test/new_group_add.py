# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_new_group_add(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="New group", header="New group header", footer="New group footer"))
    app.session.logout()


def test_new_empty_group_add(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
