import logging
from Adafruit_PCA9685 import PCA9685

# Init logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create console handler and set level to debug 
ch = logging.StreamHandler() 
ch.setLevel(logging.DEBUG)
         
# Create logging formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# Add ch to logger
logger.addHandler(ch) 

class Block:
    
    uid = ''
    points = []

    def __init__(self,uid):
        uid = self.uid

    def addPoint(self,point):
        if type(point) != Point:
            raise TypeError('Must be Point class')
        for i in self.points:
            if i.uid == point.uid:
                raise ValueError('Point UID already exists')
            elif i.servo_channel == point.servo_channel and i.servo_i2c_addr == point.servo_i2c_addr:
                raise ValueError('Point servo controller and channel already in use')
        self.points.append(point)

    def getPointFromID(self,id):
        for point in self.points:
            if point.uid == id:
                return point
        else:
            return False

class Point:
    count = 0

    def __init__(self,i2c_addr,channel,pos1,pos2):
        Point.count = Point.count + 1
        self.uid = Point.count
        self.servo_pos1 = pos1
        self.servo_pos2 = pos2
        self.servo_i2c_addr = i2c_addr
        self.servo_channel = channel
        self.servo_PWMfreq = 60
        self.postition = False

    def __str__(self):
        return "Point UID {} PWM Controler 0x{:x} PWM Channel {}".format(self.uid,self.servo_i2c_addr,self.servo_channel)

    def setPosition(self,pos):
        self.module = PCA9685(self.servo_i2c_addr)
        self.module.set_pwm_freq(60)
        self.module.channels = [self.servo_channel]

    def togglePosition(self):
        return memes


b1 = Block('b1')

p1 = Point(0x40,4,150,250)
b1.addPoint(p1)

#b1.addPoint(Point(0x41,1,150,250))

for i in b1.points:
    print(i)

