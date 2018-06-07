import config
from utils import get_weekend
from eventme import EventMe

e = EventMe(
    config.BASE_URL,
    config.SEARCH_URL,
    config.SENDGRID["API_KEY"],
    config.SENDGRID["FROM_EMAIL"],
    config.SENDGRID["FROM_NAME"]
)
e.scrap(*get_weekend())
e.send(*config.RECIPIENTS)
