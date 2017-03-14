# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

#случайные названия. Будут использованы для company, company_address, second_address, notes
def random_string_common(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*20
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#случайные имена. Считаем, что имена не содержат числ и символов. Только буквы. Будут использованы для firstname, middlename, lastname, title
def random_string_name(prefix, maxlen):
    symbols = string.ascii_letters + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#случайный номер телефона. Содержит цифры, пробел, +, - и ().
def random_string_phone(maxlen):
    digits = string.digits + " " + "+" + "-" + "(" + ")"
    return "".join([random.choice(digits) for i in range(random.randrange(maxlen))])

#случайная дата. в датах указать так: random_date_tuple()[0]
def random_date_tuple():
    monthes = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    random_day = random.randint(1,31)
    random_month = random.choice(monthes)
    random_year = random.randint(1850, 2017)
    date_tuple = (random_day, random_month, random_year)
    return date_tuple


#случайный мейл. Возвращаемый формат: "smth-123@host5.com"
def random_string_email(maxlen):
    symbols = string.ascii_letters + string.digits + "-" + "_"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + \
           "@" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + \
           "." + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname = "", middlename = "", lastname = "", nickname = "",
            title="",company = "", company_address = "",
            home = "", mobile_phone_num = "", work_phone_num = "", fax_num = "",
            email1 = "", email2 = "", email3 = "", homepage = "",
            birthday_d = "", birthday_m = "-", birthday_y = "",
            anniversary_d = "", anniversary_m = "-", anniversary_y = "",
            second_address = "", second_home = "", notes = "")] + [
    Contact(firstname=random_string_name("firstname_", 10), middlename=random_string_name("middlename_", 7), lastname=random_string_name("lastname_", 7), nickname=random_string_name("nickname_", 7),
            title=random_string_common("title_", 40), company=random_string_common("company_", 8), company_address=random_string_common("company_address_", 7),
            home=random_string_phone(12), mobile_phone_num=random_string_phone(12), work_phone_num=random_string_phone(12), fax_num=random_string_phone(12),
            email1=random_string_email(10), email2=random_string_email(10), email3=random_string_email(10),
            birthday_d=str(random_date_tuple()[0]), birthday_m=random_date_tuple()[1], birthday_y=str(random_date_tuple()[2]),
            anniversary_d=str(random_date_tuple()[0]), anniversary_m=random_date_tuple()[1], anniversary_y=str(random_date_tuple()[2]),
            second_address=random_string_common("second address_", 20), second_home=random_string_phone(12)
            )
            for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


