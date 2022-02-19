speed = "speed up";
slow = "slow down";
left = "left";
right = "right";

def right_front(speed):
    right_speed = speed;
    return "Drone turn to the right and "+right_speed;

def left_front(speed):
    left_speed = speed;
    return "Drone turn to the left and "+left_speed;

def right_back(speed):
    right_speed = speed;
    return "Drone turn to the right and "+right_speed;

def left_back(speed):
    left_speed = speed;
    return "Drone turn to the left and "+left_speed;

def up():
    return right_front(speed), left_front(speed),\
        'Go Forward'

def down():
    return right_back(slow), left_back(slow),\
        'Go Backward'

functions={
    "up":up(),
    "down":down(),

}

while True:
    userInput = input("Say The Command : ")
    if userInput in functions:
        print(functions[userInput])
    elif userInput not in functions and userInput !="exit":
        print("Wrong Command");
    else:
        print("Shutdown")
        break