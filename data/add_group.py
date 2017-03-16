from model.group import Group
import random
import string


constant = [
    Group(name="group_name_1", header="header_1", footer="footer_1"),
    Group(name="group_name_2", header="header_2", footer="footer_2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*20
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 30))
    for i in range(5)
]


