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


def random_sleep(sleep_max: int):
    # sleep for 0~sleep_max*60 seconds
    sleep_rand = int(random() * sleep_max * 60)
    print(f"sleep for {sleep_rand} minutes")
    time.sleep(sleep_rand)


if __name__ == '__main__':
    max_sleep = os.getenv('MAX_SLEEP_MIN')
    if not max_sleep:
        random_sleep(10)
    else:
        try:
            random_sleep(int(max_sleep))
        except TypeError as e:
            notify("MAX_SLEEP_MIN设置错误", str(e))
            sys.exit()
    notify(f"cron job at github action sleeped for {max_sleep} min")
