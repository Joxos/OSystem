import os

import ls

exitWords = ["exit", "quit"]
while True:
    path = os.path.abspath('.')
    print(path, "$ ", end='')
    inputedMessage = input()
    resultList = inputedMessage.rstrip().lstrip().split(" ")
    resultDirection = resultList[0]
    if resultDirection == '':
        pass
    elif resultDirection == "ls":
        ls.ls(path)
    elif resultDirection in exitWords:
        break
    elif resultDirection == "dir":
        for i in os.listdir(os.path.abspath('.')):
            print(i)
    else:
        print("Unknown direction:", resultDirection)
