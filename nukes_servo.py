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
    SERVO_PULSE_MIN = 150
    SERVO_PULSE_MAX = 590

    @classmethod
    def run(cls, boards):
        while True:
            print('MIN')
            for pwm in boards:
                for channel in pwm.channels:
                    pwm.module.set_pwm(channel, 0, PwmTester.SERVO_PULSE_MIN)
            time.sleep(1)
            print('MAX')
            for pwm in boards:
                for channel in pwm.channels:
                    pwm.module.set_pwm(channel, 0, PwmTester.SERVO_PULSE_MAX)
            time.sleep(1)


if __name__ == '__main__':
    PwmTester.run([Pwm(0x40, [0]), Pwm(0x40, [4]), Pwm(0x40, [7])])
