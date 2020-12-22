import pigpio
from time import sleep

pi = pigpio.pi()


def stop_motor_if_running():
    """Stop motor if its speed isn't already at 0"""
    # speed = pi.get_servo_pulsewidth(13)
    pi.write(17, 1)  # For testing at home with 5V motor
    # if int(speed) != 1500:
    #     pi.set_servo_pulsewidth(13, 1500)
    #     sleep(1)
    #     pi.stop()
