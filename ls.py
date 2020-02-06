import os


def ls(path):
    print(" _______________________________")
    print("|       NAME       |    SIZE    |")
    print(" -------------------------------")
    for i in os.listdir(path):
        if os.listdir(path) == []:
            print("| The folder is emty.           |")
        elif os.path.isdir(path+"\\"+i):
            print('| {:17s}|   IS DIR   |'.format(i))
        elif os.path.isfile(path+"\\"+i):
            fileSize = os.path.getsize(os.path.abspath('.')+"\\"+i)
            if fileSize >= 1024:
                sizeString = '%.2f' % (fileSize/1024)+"KB"
            elif fileSize >= 1024**2:
                sizeString = '%.2f' % (fileSize/(1024**2))+"MB"
            elif fileSize >= 1024**3:
                sizeString = '%.1f' % (fileSize/(1024**3))+"GB"
            print('| {:17s}| {:11s}|'.format(i, sizeString))
    print(" -------------------------------")


if __name__ == "__main__":
    path = input("Input the path: ")
    try:
        ls(path)
    except:
        print("Please enter a correctly absolutly path.")
    else:
        print("End.")
