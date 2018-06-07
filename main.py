import config
from eventme import EventMe

date1 = "09/06/2018"
date2 = "09/06/2018"

e = EventMe(
    config.BASE_URL,
    config.SEARCH_URL,
    config.SENDGRID["API_KEY"],
    config.SENDGRID["FROM_EMAIL"],
    config.SENDGRID["FROM_NAME"]
)
e.scrap(date1, date2)
e.send("sdelquin@gmail.com")
