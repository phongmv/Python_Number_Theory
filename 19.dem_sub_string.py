tc  = int(input())


def subStringCounter(string, subString):
    return string.count(subString)

while tc > 0:
    tc -= 1
    string =  input()
    subString = input()
    print(subStringCounter(string, subString))