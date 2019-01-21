import servo
import time

while True:
    servo.swing_servo(servo.pwm1,0,servo.servo_min)

    time.sleep(1)

    servo.swing_servo(servo.pwm1, 0, servo.servo_max)

    time.sleep(1)


