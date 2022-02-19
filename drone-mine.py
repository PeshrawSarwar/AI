speed="speed up"
slow="slow down"



def frontLeft(speed):
    frontLeftSpeed = speed
    return 'font left speed '+frontLeftSpeed

def backLeft(speed):
    backLeftSpeed = speed
    return 'back left speed '+backLeftSpeed

def frontRight(speed):
    frontRightSpeed = speed
    return 'front right speed '+frontRightSpeed

def backRight(speed):
    backRightSpeed = speed
    return 'back right speed '+backRightSpeed

def up():
    return frontLeft(speed),frontRight(speed),backLeft(speed),backRight(speed),\
           ' up successfull'

def down():
        return frontLeft(slow),frontRight(slow),backLeft(slow),backRight(slow),\
            ' down successfull'

def right():
    return frontRight(speed),frontRight(speed),\
           ' right successfull'

def left():
    return frontLeft(speed),backLeft(speed),\
           ' left successfull'

def back():
    return backLeft(speed),backRight(speed),\
           ' back successfull'


actions={
    'up': up(),
    'down':down(),
    'right':right(),
    'left':left(),
    'back':back()
}

while True:
    userInput = input("say command : ")
    if userInput in actions :
        print(actions[userInput])
    elif userInput == 'stop':
        break
    else:
        print("wrong command")
        break
