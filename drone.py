agent = [];

def right_side():
    f1=10;
    f2=10;
    f3=5;
    f4=5;
    agent.append(f1)
    agent.append(f2)
    agent.append(f3)
    agent.append(f4)
    return agent;

def left_side():
    f1=5;
    f2=5;
    f3=10;
    f4=10;
    agent.append(f1)
    agent.append(f2)
    agent.append(f3)
    agent.append(f4)
    return agent;


def up():
    f1 = 15;
    f2 = 15;
    f3 = 15;
    f4 = 15;
    agent.append(f1)
    agent.append(f2)
    agent.append(f3)
    agent.append(f4)
    return agent


def down():
    f1 = 5;
    f2 = 5;
    f3 = 5;
    f4 = 5;
    agent.append(f1)
    agent.append(f2)
    agent.append(f3)
    agent.append(f4)
    return agent

def shutdown():
    f1 = 10;
    f2 = 10;
    f3 = 10;
    f4 = 10;
    agent.append(f1)
    agent.append(f2)
    agent.append(f3)
    agent.append(f4)
    # create a for loop to iterate through the list
    for i in range(len(agent)):
        agent[i]-=1;
    return agent;

up()
print(agent)