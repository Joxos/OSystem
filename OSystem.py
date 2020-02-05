import os
while True:
    path = os.path.abspath('.')
    print(path, " $ ", sep='', end='')
    inputedMessage = input()
    resultMessage = inputedMessage.rstrip().lstrip()
    if resultMessage == '':
        pass
    elif resultMessage == "ls":
        print("_________________________")
        print("|     NAME     |  SIZE  |")
        print("—————————————————————————")
        for i in os.listdir(os.path.abspath('.')):
            fileSize = os.path.getsize(os.path.abspath('.')+"\\"+i)
            print('| {:13s}| {:7s}|'.format(str(i), str(fileSize)))
        print("—————————————————————————")
    elif resultMessage == "exit":
        break
    elif resultMessage == "dir":
        for i in os.listdir(os.path.abspath('.')):
            print(i)
    else:
        print("Unknown object: ", inputedMessage, sep='')
