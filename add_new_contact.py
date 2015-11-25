# -*- coding: utf-8 -*-
from contact import Contact
import pytest
from application_contact import Application_contact


@pytest.fixture
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname = "Homer", middlename = "Jay", lastname = "Simpson", nickname = "simpson",
             photo_path = 'c:\\GitHub\\Task1\\res\\homer.jpg', title = "worker",
             company = "Springfield Nuclear Power Plant", company_address = "Springfield", home = "Springfield, 742 Evergreen Terrace",
             mobile_phone_num = "+1(123)456-67-89", work_phone_num = "+1(123)456-67-89", fax_num = "+1(123)456-67-89",
             email1 = "homer.simpson@fox.tv", email2 = "homer.simpson@fox.tv", email3 = "", homepage = "http://simpsons.com",
             birthday_d = "12", birthday_m = "May", birthday_y = "1959",
             anniversary_d = "10", anniversary_m = "May", anniversary_y = "1957",
             second_address = "Springfield", second_home = "742 Evergreen Terrace", notes = "No comments"))
    app.logout()

