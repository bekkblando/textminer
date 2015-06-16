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


def phone_number(test):
    if len(re.findall(r"[\d]", test)) == 10:
        return True
    else:
        return False


def money(test):
    if len(test) < 2:
        return False
    if re.fullmatch(r"\$.*\.\d{1}|\$.*\.\d{3}|\${2}\d.*|\$\d*,\d{1,2}|\d+", test):
        return False
    else:
        return True


def zipcode(test):
    if len(re.findall(r"[\d]", test)) == 5 or len(re.findall(r"[\d]", test)) == 9:
        return True
    else:
        return False


def date(test):
    if len(re.findall(r"\d.*/\d.*/\d.*|\d.*-\d.*-\d.*", test)):
        return True
    else:
        return False
