# import libriary
from controller import Robot, Motor

# constant variable
TIME_STEP = 64
MAX_SPEED = 6.25

# create the Robot instance.
robot: Robot = Robot()

# get a handler to the motors and set target position to infinity (speed control)
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(10.0)
rightMotor.setPosition(10.0)

# set up the motor speeds at 10% of the MAX_SPEED.
leftMotor.setVelocity(0.1 * MAX_SPEED)
rightMotor.setVelocity(0.1 * MAX_SPEED)

while robot.step(TIME_STEP) != -1: pass