# EventMe

Tool made in Python to notify me events in Tenerife.

## How it works

It makes a post request over the url http://lagenda.org/programacion/hoy and scraps the content looking for entries of events. Then it sends an email to the specified recipients with the events within a tabular layout.

## Launch it!

~~~console
$ pip install -r requirements.txt
$ cp config.tmpl.py config.py
$ vim config.py
~~~

> Set the corresponding values for each variable

~~~console
$ python main.py
~~~
