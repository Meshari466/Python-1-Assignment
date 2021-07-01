import string 
import random

def gen():
    source1 = string.ascii_uppercase
    source2 = string.ascii_lowercase
    source3 = string.digits

    lenth = int(10)

    s = []
    s.extend(list(source1))
    s.extend(list(source2))
    s.extend(list(source3))

    random.shuffle(s)

    pas = ("".join(s[0:lenth]))
    print(pas)

gen()