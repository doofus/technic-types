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
        if ReflectedLight <= 20:
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

hub.light_matrix.show_image('HAPPY')


hub.motion_sensor.reset_yaw_angle()

yaw = hub.motion_sensor.get_yaw_angle()
motor_power = 40

# -------------------------------------
# Task #1: Push sofa
# -------------------------------------

# Push sofa
move(30)

# Straighten out
turn_to_zero()

# Back up
move_backwards(13)

# Straighten out
turn_to_zero()

# -------------------------------------
# Task #2: Windmill
# -------------------------------------

# turn -45 degrees
turn_to_angle(-45)

# move to closer to the windmill
move(41)

# turn to 45 degrees
turn_to_angle(45)

# move to windmill base and push once
move(30)


for looper in [1, 2, 3]: # push the windmill thrice
    move_backwards(2)
    turn_to_angle(45)
    move_backwards(2)
    move(16)

# Move back and correct course
move_backwards(2)
turn_to_angle(45)
move_backwards(18)
#Turn towards road to the left
turn_to_angle(-90)

# -------------------------------------
# Task #3: solar panels
# -------------------------------------

# Start moving
motor_pair.set_default_speed(50)
motor_pair.start()

wait_for_seconds(0.5) # Wait to clear off windmill road

# Keep moving until sensor detects "black"
stop_on_black()

# Straighten out to -90 degrees
turn_to_angle(-90)

# Clear off first Intersection
move(5)

# Start motor and stop at Intersection across from the high fiving hand
motor_pair.start()
stop_on_black()

# Move off of black line
move(3.5)

# Correct Course
turn_to_angle(-90)

# Move past high five thingy
move(16)

# Turn to 0 degrees (Towards the solar panels)
turn_to_angle(0)

# Go to the main line and stop
motor_pair.set_default_speed(50)
motor_pair.start()
stop_on_black()

# Correct course
turn_to_angle(0)

# Move into first solar panel
move(27)

# Move away from wall
move_backwards(3)

# Turn towards the other two energy units
turn_to_angle(-90)

# Move the energy units off thier respective circles
move(40)

# Move back away from the energy storage
move_backwards(3)

# Move back on to main road
turn_to_angle(-179)
motor_pair.start()
stop_on_black()

# Turn towards end
turn_to_angle(-135)

# Land on line to correct course
motor_pair.start()
wait_for_seconds(0.3)
stop_on_black()

# Correct course
turn_to_angle(-145)

# Drive to the finish!
motor_pair.set_default_speed(100)
motor_pair.start()

