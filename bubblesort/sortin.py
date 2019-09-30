import re
import os
import time

APP_PATH = os.path.dirname(__file__)
os.system('cls' if os.name == 'nt' else 'clear')  # clear console

def printgraph (inlist):
    for entry in inlist:
        print("-"*int(int(entry)/5))


def UnsortedDict(file):
    dict = {}
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            name, value = re.split(":", line)
            dict[value] = name
    return dict


def sorted(numbers):
    switch = True
    while switch is True:
        switch = False
        for i in range(len(numbers) - 1):
            os.system('cls' if os.name == 'nt' else 'clear')
            printgraph(numbers)
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                switch = True
                #printgraph(numbers)
                time.sleep(.5)
    return numbers


def main():

    newlist = []
    dict = UnsortedDict(APP_PATH + "//testfile.txt")

    for key in dict:
        newlist.append(key)

    newlist = sorted(newlist)

    #newlist = sorted([key for key in dict])
    printgraph("\n")
    for i in newlist:
        print(dict[i] + ":" + i)


if __name__ == "__main__":
    main()
