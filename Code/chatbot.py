QA={
    "hi":"hello how can i help you",
    "hello": "hello",
    "choni":"bashy",
    "whats your name?":"Im Waldoooo"
}

while True:
    userInput = input("Your Question : ");
    if userInput in QA:
        print("Bots Answer is : "+ QA[userInput])
    elif userInput == "bye":
        print("Bye")
        break
    else:
        print("I didn't understand sorry!'");
    
