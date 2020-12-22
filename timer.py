# import threading
import variables as var
from stop_motor_if_running import stop_motor_if_running


def duration_timer(seconds):
    while seconds < var.counter:
        print('running...')

    stop_motor_if_running()
