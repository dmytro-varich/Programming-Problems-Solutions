from controller import Robot, Motor

# defenition time step
TIME_STEP = 64

# create the Robot instance.
robot = Robot()

# initialize sensors
ds = []
dsNames = ['ds_left', 'ds_right']
for i in range(2):
    ds.append(robot.getDevice(dsNames[i]))
    ds[i].enable(TIME_STEP)
  
# initialize motors
speed = 0.0  # [rad/s]
wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
for i in range(4):
    wheels.append(robot.getDevice(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(speed)

avoidObstacleCounter = 0
while robot.step(TIME_STEP) != -1:
    leftSpeed = -1.0
    rightSpeed = -1.0
    if avoidObstacleCounter > 0:
        avoidObstacleCounter -= 1
        leftSpeed = 1.0
        rightSpeed = -1.0
    else:  # read sensors
        for i in range(2):
            if ds[i].getValue() < 950.0:
                avoidObstacleCounter = 50  
                
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
    
