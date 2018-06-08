"""EventMe

Usage:
    main.py --when=WHEN

Options:
    --when=WHEN     Possible values:
                    today
                    next-weekend
                    03/05/2018
                    07/04/2018-12/04/2018
"""
import config
from utils import get_weekend
from eventme import EventMe
from docopt import docopt
import datetime


e = EventMe(
    config.BASE_URL,
    config.SEARCH_URL,
    config.SENDGRID["API_KEY"],
    config.SENDGRID["FROM_EMAIL"],
    config.SENDGRID["FROM_NAME"]
)

arguments = docopt(__doc__)
if arguments["--when"].lower() == "today":
    date1 = date2 = datetime.date.today()
elif arguments["--when"].lower() == "next-weekend":
    date1, date2 = get_weekend()
else:
    dates = arguments["--when"]
    if dates.find("-") == -1:
        dates = [dates, dates]
    else:
        dates = dates.split("-")
    date1, date2 = (datetime.datetime.strptime(d, "%d/%m/%Y") for d in dates)

e.scrap(date1, date2)
e.send(*config.RECIPIENTS)
