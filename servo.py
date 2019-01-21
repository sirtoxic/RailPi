import time
import Adafruit_PCA9685 # Import the PCA9685 module.

# Specify PWM controllers:
pwm1 = Adafruit_PCA9685.PCA9685(address=0x40)
pwm2 = Adafruit_PCA9685.PCA9685(address=0x41)

# Set frequency to 60hz, good for servos.
pwm1.set_pwm_freq(60)
pwm2.set_pwm_freq(60)

# Configure min and max servo pulse lengths
servo_min = 120  # Min pulse length out of 4096
servo_max = 602  # Max pulse length out of 4096

def swing_servo(pwm, channel, pulse): #Is Good Yes
    pwm.set_pwm(channel, 0 , pulse)


print('Moving servo on channel 0, press Ctrl-C to quit...')
