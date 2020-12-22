# import threading
from time import sleep
import variables as var


def bla():
    # global var.counter
    while True:
        var.counter += 1
        sleep(0.5)
