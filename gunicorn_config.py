import logging

loglevel = 'debug'
logfile = '/opt/project2/logs/gunicorn.log'

bind = "127.0.0.1:8000"
workers = 4
