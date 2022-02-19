Q_A={
    "hi":"hello how can i help you",
    "choni":"bashi",
    "are u okey":"i am fine",
    "how are you":"i am fine",
}

while True:
    ask = input("Your question : ")
    if ask in Q_A:
        print("Bot answer : "+Q_A[ask])
    elif ask not in Q_A and ask!='bye':
        print("I don\'t understand")
    else:
        print("Bye")
        break