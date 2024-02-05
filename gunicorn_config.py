import logging

loglevel = 'debug'
logfile = './logs/gunicorn.log'

bind = "0.0.0.0:8000"
workers = 4
