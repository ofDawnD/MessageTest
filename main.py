import time
import sys

import msg

from os import getenv
from random import random


def random_sleep(sleep_max: int):
    # sleep for 0~sleep_max*60 seconds
    sleep_rand = int(random() * sleep_max * 60)
    msg.log(f"sleep for {sleep_rand} seconds")
    time.sleep(sleep_rand)


if __name__ == '__main__':
    max_sleep = getenv('MAX_SLEEP_MIN')

    if not max_sleep:
        random_sleep(1)
    else:
        try:
            max_sleep = int(max_sleep)
        except TypeError as e:
            msg.log("MAX_SLEEP_MIN设置错误", str(e))
            sys.exit()

        random_sleep(max_sleep)
    msg.log("woken up")
