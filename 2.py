QA = {
    "hi":"hello how can i help you",
    "choni":"bashi"
}

print('hello please type some thing')
while True:
    ask = input('you :')

    if ask in QA :
        print('bot answer :'+QA[ask])
        # ask=input()

    elif ask not in QA and ask!='bye' :
        print('i don understand')
        ans = input('answer :')
        QA[ask] = ans
    elif ask == 'bye':

        break