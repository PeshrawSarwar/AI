# create a function
def main(input):
    # create a random array with random texts
    # random_array = ["Hello", "World", "This", "is", "a", "test"]
    output = ""

    # create an array of objects
    objects = [
    {
        "ask": "hello",
        "answer": "hey"
    },
    {
        "ask": "whats your name",
        "answer": "my name is Waldooo!"
    },
    {
        "ask": "whats your favourite color",
        "answer": "blue"
    }]

    # loop through the array of objects and check if the input is in the ask then returen the answer
    for object in objects:
        if input in object["ask"]:
            output = object["answer"]
    
    return output



# call the main function and give it an argument of hello 
print(main("hello"))