import os
while True:
    path = os.path.abspath('.')
    print(path, " $ ", sep='', end='')
    inputedMessage = input()
    resultList = inputedMessage.rstrip().lstrip().split(" ")
    resultDirection = resultList[0]
    if resultDirection == '':
        pass
    elif resultDirection == "ls":
        print("_____________________________")
        print("|      NAME      |   SIZE   |")
        print("—————————————————————————————")
        for i in os.listdir(os.path.abspath('.')):
            fileSize = os.path.getsize(os.path.abspath('.')+"\\"+i)
            print('| {:15s}| {:9s}|'.format(str(i), str(fileSize)))
        print("—————————————————————————————")
    elif resultDirection == "exit" or resultDirection == "quit":
        break
    elif resultDirection == "dir":
        for i in os.listdir(os.path.abspath('.')):
            print(i)
    else:
        print("Unknown direction:", resultDirection)
