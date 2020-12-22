import threading
import pigpio
from time import sleep as sl
from datetime import datetime

import variables as var
from background import bla

# counter = 0


def count_up():
    # global counter
    while True:
        var.counter += 1
        sl(0.5)


def blink():
    start_time = datetime.now()
    while var.counter < 20:
        pi.write(led, 1)
        sl(0.5)
        pi.write(led, 0)
        sl(0.5)

    end_time = datetime.now()
    delta_time = end_time - start_time
    print('delta:', delta_time)


if __name__ == "__main__":
    pi = pigpio.pi()
    led = 17
    pi.set_mode(led, pigpio.OUTPUT)
    pi.set_pull_up_down(led, pigpio.PUD_DOWN)
    if not pi:
        print('pigpio daemon not running...')
    else:
        for i in range(3):
            pi.write(led, 0)
            sl(1)
            pi.write(led, 1)
            sl(1)
    # test = threading.Thread(target=count_up)
    # test.daemon = True
    # test.start()
    #
    # blinker = threading.Thread(target=blink)
    # blinker.start()
    #
    # test1 = threading.Thread(target=bla)
    # test1.daemon = True
    # test1.start()
