speed_up = "speed up"
slow_down = "slow down"

def frontRight(speed) :
    frontRightSpeed = speed
    return 'front right fan '+frontRightSpeed

def frontLeft(speed):
    frontLeftSpeed = speed
    return 'front left fan '+frontLeftSpeed

def backRight(speed):
    backRightSpeed = speed
    return 'back right fan '+backRightSpeed

def backLeft(speed):
    backLeftSpeed = speed
    return 'back left fan '+backLeftSpeed

def up():
    return frontLeft(speed_up),frontRight(speed_up),backLeft(speed_up),backRight(speed_up),\
           'up successfull'

def down():

    return frontLeft(slow_down),frontRight(slow_down),backLeft(slow_down),backRight(slow_down),\
           'down successfull'

def front():
    return frontLeft(speed_up),frontRight(speed_up),\
           'front successfull'

def back():
    return backLeft(speed_up),backRight(speed_up),\
           'back successfull'

def left():
    return frontLeft(speed_up),backLeft(speed_up),\
           'left successfull'

def right():
    return frontRight(speed_up),backRight(speed_up),\
           'right successfull'


actions={
    'up': up(),
    'down':down(),
    'front':front(),
    'back':back(),
    'right':right(),
    'left':left()
}

while True:
    userInput = input('say comand :')
    if userInput in actions :
        print(actions[userInput])
    elif userInput=='stop' :
        break
    else:
        print("sorry i can not recognize it")