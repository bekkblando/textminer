import re


def words(test):
    if len(re.findall(r"[a-zA-Z]", test)) > 0:
        return test.split()


def date(test):
    if len(re.findall(r"\d.*/\d.*/\d.*|\d.*-\d.*-\d.*", test)):
        if len(re.findall(r"[/]", test)) == 2:
            date = re.findall(r"\d*/\d*/\d*", test)
            print(date)
            month = ''.join(re.findall(r"^\d{1,2}", test))
            print(month)
            day = re.findall(r"/\d{1,2}.", test)
            day = ''.join(day)[1:-1]
            year = ''.join(re.findall(r"/\d{4}", test))
            year = year[1:]
            return {"month": int(month), "day": int(day), "year": int(year)}
        if len(re.findall(r"[-]", test)) == 2:
            date = ''.join(re.findall(r"\d*-\d*-\d*", test))

            print(date)

            month = ''.join(re.findall(r"-\d{1,2}-", test))
            month = month[1:-1]

            day = date[8:]

            year = ''.join(re.findall(r"\d{4}", test))

            return {"month": int(month), "day": int(day), "year": int(year)}
    else:
        return None

def zipcode(test):
    if len(re.findall(r"[\d]", test)) == 9 or len(re.findall(r"[\d]", test)) == 5:
        cleantext = ''.join((re.findall(r"[\d]", test)))
        print(cleantext)
        zip = re.findall(r"^\d{5}", cleantext)
        number = cleantext[5:]
        if number == '':
            number = None
        else:
            number = ''.join(number)
        return {"zip": ''.join(zip), "plus4": number}


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
