from datetime import datetime


def get_birthdays_per_week(users):
    current_datetime = datetime.now()
    res = []
    mon = []
    tue = []
    wed = []
    thu = []
    fri = []
    today = current_datetime.date()
    for person_dict in users:
        b_day = person_dict.get("birthday")
        difference = b_day-today
        str_dif = str(difference)
        s = str_dif.split(" ")
        if int(s[0]) <= 7:
            if b_day.weekday() == 0 or b_day.weekday() == 5 or b_day.weekday() == 6:
                mon.append(person_dict.get("name"))
            if b_day.weekday() == 1:
                tue.append(person_dict.get("name"))
            if b_day.weekday() == 2:
                wed.append(person_dict.get("name"))
            if b_day.weekday() == 3:
                thu.append(person_dict.get("name"))
            if b_day.weekday() == 4:
                fri.append(person_dict.get("name"))
    if len(mon) > 0:
        res.append("Monday: ")
        m = ", ".join(mon)
        res.append(m)
        res.append("\n")
    if len(tue) > 0:
        res.append("Tuesday: ")
        t1 = ", ".join(tue)
        res.append(t1)
        res.append("\n")
    if len(wed) > 0:
        res.append("Wednesday: ")
        w = ", ".join(wed)
        res.append(w)
        res.append("\n")
    if len(thu) > 0:
        res.append("Thursday: ")
        t2 = ", ".join(thu)
        res.append(t2)
        res.append("\n")
    if len(fri) > 0:
        res.append("Friday: ")
        f = ", ".join(fri)
        res.append(f)
        res.append("\n")

    cong = "".join(res)
    print(cong)
