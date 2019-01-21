
# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
import time
from Adafruit_PCA9685 import PCA9685


class Pwm:
    CHANNELS = 16
    SERVO_DEFAULT_FREQUENCY = 60

    def __init__(self, address, channels=[]):
        assert address > 0, "Invalid Pwm Address"
        assert isinstance(channels, list), "Channels must be a list"
        for channel in channels:
            assert channel >= 0 and channel < Pwm.CHANNELS

        self.address = address
        self.module = PCA9685(address)
        self.module.set_pwm_freq(Pwm.SERVO_DEFAULT_FREQUENCY)
        self.channels = channels


class PwmTester:
    SERVO_PULSE_MIN = 120
    SERVO_PULSE_MAX = 602

    @classmethod
    def run(cls, boards):
        while True:
            for pwm in boards:
                for channel in pwm.channels:
                    pwm.module.set_pwm(channel, 0, PwmTester.SERVO_PULSE_MIN)
            time.sleep(1)
            for pwm in boards:
                for channel in pwm.channels:
                    pwm.module.set_pwm(channel, 0, PwmTester.SERVO_PULSE_MAX)
            time.sleep(1)


if __name__ == '__main__':
    PwmTester.run([Pwm(0x40, [0]), Pwm(0x41, [0])])
