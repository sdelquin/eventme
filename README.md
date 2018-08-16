# EventMe

Tool made in Python to notify me events in Tenerife.

## How it works

It makes a post request over the url http://lagenda.org/programacion/hoy and scraps the content looking for entries of events. Then it sends an email to the specified recipients with the events within a tabular layout.

## Launch it!

~~~console
$ pipenv install
$ cp config.tmpl.py config.py
$ vim config.py
~~~

> Set the corresponding values for each variable

Create `recipients.txt` and add the emails of the recipients (one per line):

~~~console
$ echo "example@example.com" > recipients.txt
~~~

Launch the script:

~~~console
$ pipenv run python main.py --when=today
~~~

## Asking for some help

If you need more help:

~~~console
$ pipenv run python main.py --help
~~~
