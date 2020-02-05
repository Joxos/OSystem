import os
while True:
    path = os.path.abspath('.')
    print(path, "@root $ ", sep='', end='')
    inputedMessage = input()
    resultMessage = inputedMessage.rstrip().lstrip()
    if resultMessage == '':
        pass
    elif resultMessage == "ls":
        for i in os.listdir(os.path.abspath('.')):
            print(i)
    elif resultMessage == "exit":
        break
    elif resultMessage == "dir":
        for i in os.listdir(os.path.abspath('.')):
            print(i)
    else:
        print("Unknown object: ", inputedMessage, sep='')
