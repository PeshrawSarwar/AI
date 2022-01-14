const display = (room) => {
    console.table(room);
};

// create a 4*4 array with number 1
const room = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
];

console.log("All the room is dirty");
display(room);

let x = 0,
    y = 0;

while (x < 4) {
    while (y < 4) {
        room[x][y] = Math.floor(Math.random() * 2);
        y += 1;
    }
    x += 1;
    y = 0;
}

console.log("Before cleaning the room I detect all of these random dirts");
display(room);

let a = 0,
    b = 0,
    c = 0;

while (a < 4) {
    while (b < 4) {
        if (room[a][b] === 1) {
            console.log("Vaccum in this location now,", a, b)
            room[a][b] = 0;
            console.log("cleaned", a, b)
            c += 1
        }
        b += 1;
    }
    a += 1
    b = 0
}


pro = (100 - ((c / 16) * 100))
console.log("Room is clean now, Thanks for using : Me!")
display(room)
console.log('performance=', pro, '%')