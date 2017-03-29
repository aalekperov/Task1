import mysql
import pymysql
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, "
                           "company, title, address, "
                           "home, mobile, work, fax, "
                           "email, email2, email3, homepage, "
                           "bday, bmonth, byear, "
                           "aday, amonth, ayear, "
                           "address2, phone2, notes from `addressbook` WHERE `deprecated` = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname,
                 company, title, address,
                 home, mobile, work, fax,
                 email, email2, email3, homepage,
                 bday, bmonth, byear,
                 aday, amonth, ayear,
                 address2, phone2, notes) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname,
                                   company=company, title=title, company_address=address,
                                    home=home, mobile_phone_num=mobile, work_phone_num=work, fax_num=fax,
                                    email1=email, email2=email2, email3=email3,
                                    birthday_d=bday, birthday_m=bmonth, birthday_y=byear,
                                    anniversary_d=aday, anniversary_m=amonth, anniversary_y=ayear,
                                    second_address=address2, second_home=phone2, notes=notes))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()
