from datetime import timedelta
from math import ceil


def nice_seconds_string(seconds):
    return str(timedelta(seconds=ceil(seconds)))
