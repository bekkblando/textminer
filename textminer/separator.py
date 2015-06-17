import re


def words(test):
    if len(re.findall(r"[a-zA-Z]", test)) > 0:
        return test.split()


def date(test):
    pass


def zipcode(test):
    pass


def money(test):
    if len(test) < 2:
        return None
    if re.fullmatch(r"\$.*\.\d{1}|\$.*\.\d{3}|\${2}\d.*|\$\d*,\d{1,2}|\d+", test):
        return None
    else:
        cleantext = ''.join((re.findall(r"[\d\.]", test)))
        print(cleantext)
        return{"currency": "$", "amount": float(cleantext)}


def phone_number(test):
    if len(re.findall(r"[\d]", test)) == 10:
        cleantext = ''.join((re.findall(r"[\d]", test)))
        print(cleantext)
        area = re.findall(r"^\d{3}", cleantext)
        number = cleantext[3:6] + '-' + cleantext[6:]
        return {"area_code": ''.join(area), "number": number}
