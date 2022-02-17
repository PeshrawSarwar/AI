qa={
    "hi":"hi",
    "choni":"bashi"
}

while True:
    ask = input("you : ")
    if ask in qa:
        print("bot answer : "+qa[ask])
    elif ask not in qa and ask!='bye':
        print("i don't understand")
        ans = input("answer : ")
        qa[ask] = ans
    elif ask == 'bye':
        print("bye")
        break
