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
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#случайный номер телефона.
def random_string_date(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#случайная дата.
def random_string_date():
    monthes = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    random_day = random.randint(1,32)
    random_month = random.choice(monthes)
    random_year = random.randint(1850, 2017)
    date_tuple = (random_day, random_month, random_year)
    return date_tuple


#случайный мейл.
def random_string_email(maxlen):
    symbols = string.ascii_letters + string.digits + "-" + "_"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "." + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname = "", middlename = "", lastname = "", nickname = "",
            title="",company = "", company_address = "", home = "",
            mobile_phone_num = "", work_phone_num = "", fax_num = "",
            email1 = "", email2 = "", email3 = "", homepage = "",
            birthday_d = "", birthday_m = "", birthday_y = "",
            anniversary_d = "", anniversary_m = "", anniversary_y = "",
            second_address = "", second_home = "", notes = "")] + [
    Contact(firstname=random_string_common("firstname_", 10), middlename=random_string_common("middlename_", 7), lastname=random_string_common("lastname_", 7))
    #for i in range(5)
    #Group(name=name, header=header, footer=footer)
    #for name in ["", random_string("name", 10)]
    #for header in ["", random_string("header", 20)]
    #for footer in ["", random_string("footer", 30)]
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    pass
    #old_contacts = app.contact.get_contact_list()
    #contact = Contact(firstname = "Homer", middlename = "Jay", lastname = "Simpson", nickname = "simpson",
    #         photo_path = 'c:\\GitHub\\Task1\\res\\homer.jpg', title = "worker",
    #         company = "Springfield Nuclear Power Plant", company_address = "Springfield", home = "+1(123)456-67-00",
    #         mobile_phone_num = "+1(123)456-67-89", work_phone_num = "+1(123)456-67-88", fax_num = "+1(123)456-67-87",
    #         email1 = "homer.simpson@fox.tv", email2 = "homer.simpson2@fox.tv", email3 = "homer.simpson3@fox.tv", homepage = "http://simpsons.com",
    #         birthday_d = "12", birthday_m = "May", birthday_y = "1959",
    #         anniversary_d = "10", anniversary_m = "May", anniversary_y = "1957",
    #         second_address = "Springfield", second_home = "+1(123)456-67-05", notes = "No comments")
    #app.contact.create(contact)
    #assert len(old_contacts) + 1 == app.contact.count()
    #new_contacts = app.contact.get_contact_list()
    #old_contacts.append(contact)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


