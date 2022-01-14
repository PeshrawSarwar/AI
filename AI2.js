const agent = [];

const right_side = () => {
    f1 = 10;
    f2 = 10;
    f3 = 5;
    f4 = 5;
    agent.push(f1, f2, f3, f4);
    return agent;
}

const left_side = () => {
    f1 = 5;
    f2 = 5;
    f3 = 10;
    f4 = 10;
    agent.push(f1, f2, f3, f4);
    return agent;
}

const up = () => {
    f1 = 15;
    f2 = 15;
    f3 = 15;
    f4 = 15;
    agent.push(f1, f2, f3, f4);
    return agent;
}

const down = () => {
    f1 = 5;
    f2 = 5;
    f3 = 5;
    f4 = 5;
    agent.push(f1, f2, f3, f4);
    return agent;
}

const shutdown = () => {
    // decrement the value of the array -1 in a second
    // if the value is 0, then the agent is dead
    f1 = 10;
    f2 = 10;
    f3 = 10;
    f4 = 10;
    agent.push(f1, f2, f3, f4);
    for (let i = 0; i < agent.length; i++) {
        // console.log(agent[i])
        agent[i] -= 1;
        console.log(agent[i])
        if (agent[i] === 0) {
            console.log("Agent is dead");
        }
    }
    // console.log("error")
}

const setDirection = (direct) => {
    if (direct === "right") {
        console.log(right_side());
    } else if (direct === "left") {
        console.log(left_side())
    } else if (direct === "up") {
        console.log(up())
    } else if (direct === "down") {
        console.log(down())
    } else {
        shutdown();
    }
}

setDirection("shut")

const map = [
    [1, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 1]
];

map.forEach((element) => {
    element.forEach((element2) => {
        if (element2 === 1) {
            console.log("*")
        } else {
            console.log(" ")
        }
        console.log("")
    })
})