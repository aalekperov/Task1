import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    merge = merge_phones_like_on_home_page(contact_from_edit_page)
    print(contact_from_home_page.all_phones_from_home_page)
    print(merge)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)



def test_phone_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile_phone_num == contact_from_edit_page.mobile_phone_num
    assert contact_from_view_page.work_phone_num == contact_from_edit_page.work_phone_num
    assert contact_from_view_page.second_home == contact_from_edit_page.second_home


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "/n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile_phone_num, contact.work_phone_num, contact.second_home]))))