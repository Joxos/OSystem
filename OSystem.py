import os

while True:
    path = os.path.abspath('.')
    print(path, "$ ", end='')
    inputedMessage = input()
    resultList = inputedMessage.rstrip().lstrip().split(" ")
    resultDirection = resultList[0]
    if resultDirection == '':
        pass
    elif resultDirection == "ls":
        print(" _______________________________")
        print("|       NAME       |    SIZE    |")
        print(" ———————————————————————————————")
        for i in os.listdir(os.path.abspath('.')):
            if os.path.isdir(os.path.abspath('.')+"\\"+i):
                print('| {:17s}|   IS DIR   |'.format(i))
            elif os.path.isfile(os.path.abspath('.')+"\\"+i):
                fileSize = os.path.getsize(os.path.abspath('.')+"\\"+i)
                if fileSize >= 1024:
                    sizeString = '%.2f' % (fileSize/1024)+"KB"
                elif fileSize >= 1024**2:
                    sizeString = '%.2f' % (fileSize/(1024**2))+"MB"
                elif fileSize >= 1024**3:
                    sizeString = '%.1f' % (fileSize/(1024**3))+"GB"
                print('| {:17s}| {:11s}|'.format(i, sizeString))
        print(" ———————————————————————————————")
    elif resultDirection == "exit" or resultDirection == "quit":
        break
    elif resultDirection == "dir":
        for i in os.listdir(os.path.abspath('.')):
            print(i)
    else:
        print("Unknown direction:", resultDirection)
