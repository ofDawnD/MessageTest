from os import getenv
from requests import get

url = getenv('MSG_URL')


def notify(msg: str):
    if not url:
        return

    params = {
        "message": msg,
        "from": "MessageTest",
    }

    res = get(url, params=params, timeout=100)
    print(res)
