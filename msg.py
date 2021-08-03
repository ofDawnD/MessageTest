from os import getenv
from requests import get

url = getenv('MSG_URL')
DEBUG = getenv('DEBUG')


def send_to_url(msg: str, fr: str):
    if not url:
        return

    params = {
        "message": msg,
        "from": fr,
    }

    res = get(url, params=params, timeout=100)
    print(res)


def log(msg: str):
    if not DEBUG:
        send_to_url(msg, "log")
    else:
        print(msg)
