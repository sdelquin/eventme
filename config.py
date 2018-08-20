from prettyconf import config

BASE_URL = 'http://lagenda.org'
SEARCH_URL = BASE_URL + '/programacion/hoy'
RECIPIENTS = config('RECIPIENTS', default='recipients.txt')

SENDGRID_APIKEY = config('SENDGRID_APIKEY')
SENDGRID_FROM_EMAIL = config('SENDGRID_FROM_EMAIL')
SENDGRID_FROM_NAME = config('SENDGRID_FROM_NAME')
