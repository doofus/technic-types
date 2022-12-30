from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math
from math import *
import time
hub = PrimeHub()
color1 = ColorSensor('F') #right
color2 = ColorSensor('B') #left
motor_pair = MotorPair('A', 'E')
arm = Motor('C')
motorA = Motor('A')
motorE = Motor('E')
# Function turn_to_angle()
# Turn robot to any angle based on startup gyro angle.
# Input arguments: The angle you want it to turn to relative to your gyro
#    wantedAngle: The angle to turn the robot to in degrees
def turn_to_angle(wantedAngle): # i want this angle (ex: 45)
    currentYaw = hub.motion_sensor.get_yaw_angle() # get ny current angle (ex: -45)
    if currentYaw != wantedAngle:
        motor_pair.set_default_speed(50)
        turn_angle = fabs(360 / (wantedAngle - currentYaw))
        if wantedAngle - currentYaw > 0:
            motor_pair.move(19.2 * math.pi / turn_angle, 'cm', steering=100)
        else:
            motor_pair.move(19.2 * math.pi / turn_angle, 'cm', steering=-100)

# Function stop_on_black()
# Stops the robot from moving when the reflected light is equal to or less than 20%
# Input arguments:
#    None
def stop_on_black():
    motorA.start(speed=-50)
    motorE.start(speed=50)
    foundA = False
    foundE = False
    while (not foundA or not foundE):
        if (color1.get_reflected_light()<50):
            motorE.stop()
            foundE = True
        if (color2.get_reflected_light()<50):
            motorA.stop()
            foundA = True

def stop_on_blackL():
    wait_for_seconds(0.5)
    motor_pair.set_default_speed(50)
    motor_pair.start()
    if color2.get_reflected_light()<50:
        motor_pair.stop()

# Function move()
# Moves the robot foward a certain distance
# Input arguments:
#    Amount you want the robot to move in centimeters
def move(Amount):
    motor_pair.set_default_speed(75)
    motor_pair.move(Amount, 'cm')

def move_slow(Amount):
    motor_pair.set_default_speed(50)
    motor_pair.move(Amount, 'cm')

# Function move_backwards()
# Moves the robot foward a backwards distance
# Input arguments:
#    Amount you want the robot to move in centimeters
def move_backwards(Amount):
    motor_pair.set_default_speed(-75)
    motor_pair.move(Amount, 'cm')

def move_backwards_slow(Amount):
    motor_pair.set_default_speed(-50)
    motor_pair.move(Amount, 'cm')

def lift(a, b):
    arm.run_for_rotations(a, b)

hub.motion_sensor.reset_yaw_angle()
move_slow(30)
move_backwards(2)
turn_to_angle(0)
move_backwards(10)
turn_to_angle(-45)
move(43.5)
turn_to_angle(45)
stop_on_black()
for looper in [1, 2, 3, 4]:
    move_slow(20)
    move_backwards(2)
    turn_to_angle(45)
    move_backwards(5)
    turn_to_angle(45)

move_backwards_slow(3.5)
turn_to_angle(-90)
stop_on_black()
turn_to_angle(-90)
stop_on_blackL()
turn_to_angle(0)
