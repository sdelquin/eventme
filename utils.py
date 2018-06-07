import datetime


def get_weekend():
    today = datetime.date.today()
    friday = today + datetime.timedelta((4 - today.weekday()) % 7)
    sunday = friday + datetime.timedelta(2)
    return friday, sunday
