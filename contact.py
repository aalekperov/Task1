__author__ = 'atash'


class Contact:

    def __init__(self, firstname, middlename, lastname, nickname,
                 photo_path, title,
                 company, company_address, home,
                 mobile_phone_num, work_phone_num, fax_num,
                 email1, email2, email3, homepage,
                 birthday_d, birthday_m, birthday_y,
                 anniversary_d, anniversary_m, anniversary_y,
                 second_address, second_home, notes ):
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