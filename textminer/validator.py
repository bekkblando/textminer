import re


def binary(test):
    if len(test) == 0:
        return False
    search = re.findall(r"[^01]", test)
    if len(search) > 0:
        return False
    else:
        return True


def binary_even(test):
    binar_y = binary(test)
    if not binar_y:
        return False
    elif int(test, 2) % 2 == 0:
        return True
    else:
        return False


def hex(test):
    if len(test) == 0:
        return False
    search = re.findall(r"[^\da-fA-F]", test)
    if len(search) > 0:
        return False
    else:
        return True


def word(test):
    if len(test) == 0:
        return False
    checkforletter = re.findall(r"[a-zA-Z]", test)
    search = re.findall(r"[^\d\w\-]", test)
    if len(search) == 0 and len(checkforletter) > 0:
        return True
    elif len(search) > 0:
        return False


def words(test, count=0):
    print(count)
    if len(test) == 0:
        return False
    checkforletter = re.findall(r"[a-zA-Z]", test)
    search = re.findall(r"[^\d\w\-\s]", test)
    if len(search) == 0 and len(checkforletter) > 0:
        pass
    print(search)
    if len(search) > 0:
        return False
    if len(checkforletter) == 0:
        return False
    else:
        if count == 0:
            return True
        else:
            print("Length", len(re.findall(r"\b[a-z]+\b", test)))
            print(test)
            if len(re.findall(r"\b[a-z]+\b", test)) == count:
                return True
            else:
                return False


def phone_numbers(test):
    pass


def money(test):
    pass


def zipcode(test):
    pass


def date(test):
    pass
