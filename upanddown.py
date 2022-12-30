from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math
from math import *
import time
hub = PrimeHub()
color = ColorSensor('F')
motor_pair = MotorPair('C', 'D')
integral = 0
lastError = 0
FollowLine = False

# Function turn_to_zero()
# Turn robot to startup angle based on gyro.
# Input arguments:
#    None
def turn_to_zero():
    yaw = hub.motion_sensor.get_yaw_angle()
    if yaw != 0:
        motor_pair.set_default_speed(50)
        turn_angle = 360 / yaw
        if turn_angle > 0:
            motor_pair.move(11.5 * math.pi / turn_angle, 'cm', steering=-100)
        else:
            motor_pair.move(11.5 * math.pi / turn_angle, 'cm', steering=100)


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
            motor_pair.move(11.5 * math.pi / turn_angle, 'cm', steering=100)
        else:
            motor_pair.move(11.5 * math.pi / turn_angle, 'cm', steering=-100)

# Function stop_on_black()
# Stops the robot from moving when the reflected light is equal to or less than 20%
# Input arguments:
#    None
def stop_on_black():
    while True:
        ReflectedLight = color.get_reflected_light()
        print(ReflectedLight)
        if ReflectedLight <= 40:
            motor_pair.stop()
            print("braking")
            break

# Function move()
# Moves the robot foward a certain distance
# Input arguments:
#    Amount you want the robot to move in centimeters
def move(Amount):
    motor_pair.set_default_speed(50)
    motor_pair.move(Amount, 'cm')

# Function move_backwards()
# Moves the robot foward a backwards distance
# Input arguments:
#    Amount you want the robot to move in centimeters
def move_backwards(Amount):
    motor_pair.set_default_speed(-50)
    motor_pair.move(Amount, 'cm')

motor = Motor('E')

hub.motion_sensor.reset_yaw_angle()
motor_pair.start()
stop_on_black()
turn_to_angle(0)
move_backwards(4)
turn_to_angle(-90)
motor_pair.start()
stop_on_black()
move(4)
motor.run_for_rotations(0.50)
move_backwards(10)
turn_to_angle(0)
move(5)
turn_to_angle(-90)
move(9)
motor.run_for_rotations(-0.50)
motor_pair.set_default_speed(-50)
motor_pair.start()
stop_on_black()
turn_to_angle(0)
move_backwards(10)
motor_pair.set_default_speed(-50)
motor_pair.start()





