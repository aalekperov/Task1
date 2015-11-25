# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_new_group_add(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="New group", header="New group header", footer="New group footer"))
    app.logout()


def test_new_empty_group_add(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
