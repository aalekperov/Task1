__author__ = 'atash'
from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None,
                 photo_path=None, title=None,
                 company=None, company_address=None, home=None,
                 all_phones_from_home_page=None,
                 mobile_phone_num=None, work_phone_num=None, fax_num=None,
                 all_mails_from_home_page=None,
                 email1=None, email2=None, email3=None, homepage=None,
                 birthday_d=None, birthday_m=None, birthday_y=None,
                 anniversary_d=None, anniversary_m=None, anniversary_y=None,
                 second_address=None, second_home=None, notes=None, id=None ):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo_path = photo_path
        self.title = title
        self.company = company
        self.company_address = company_address
        self.home = home
        self.mobile_phone_num = mobile_phone_num
        self.work_phone_num = work_phone_num
        self.fax_num = fax_num
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthday_d = birthday_d
        self.birthday_m = birthday_m
        self.birthday_y = birthday_y
        self.anniversary_d = anniversary_d
        self.anniversary_m = anniversary_m
        self.anniversary_y = anniversary_y
        self.second_address = second_address
        self.second_home = second_home
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_mails_from_home_page = all_mails_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.middlename, self.nickname,
                                                                                                self.title, self.company, self.company_address,
                                                                                                self.home, self.mobile_phone_num, self.work_phone_num, self.fax_num,
                                                                                                self.email1, self.email2, self.email3, self.homepage,
                                                                                                self.birthday_d, self.birthday_m, self.birthday_y,
                                                                                                self.anniversary_d, self.anniversary_m, self.anniversary_y,
                                                                                                self.second_address, self.second_home, self.notes)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.lastname == other.lastname \
               and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize