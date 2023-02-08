#!/usr/bin/env python
import os
import sys
import redis
from urllib.parse import urlparse


url = urlparse(os.environ.get("REDIS_URL"))
r = redis.Redis(host=url.hostname, port=url.port, password=url.password, ssl=True, ssl_cert_reqs=None)



if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from otree.management.cli import execute_from_command_line

    execute_from_command_line(sys.argv, script_file=__file__)
