import random

def display(room):
    print (room)


# create a 4*4 array and put number one in all the places
room = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]

print("All the room are dirty")
display(room)

x=0
y=0

while x<4:
    while y<4:
        room[x][y] = random.choice([0,1])
        y+=1
    x+=1
    y=0

print("before cleaning the room I detected that the room is dirty")    
display(room)

x=0
y=0
z=0

while x<4:
    while y<4:
        if room[x][y] == 1:
            print("Vaccum in this location now,",x, y)
            room[x][y] == 0
            print("cleaned", x,y)
            z+=1
        y+=1
    x+=1
    y=0

pro=(100-((z/16)*100))
print("Room is clean now, Thanks for using : 3710933")
display(room)
print("performance=",pro,"%")