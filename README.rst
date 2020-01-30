Marionette
==========

Flask API to control hardware integrations remotely.

Based on the Flask `tutorial`_.

.. _tutorial: https://flask.palletsprojects.com/tutorial/


Install
-------

Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Install requirements::

    $ pip install -r requirements.txt


Run
---

::

    $ export FLASK_APP=marionette
    $ export FLASK_ENV=development
    $ flask run

Open http://127.0.0.1:5000 in a browser.
