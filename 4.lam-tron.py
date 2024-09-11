import math
tc = int(input())

def roundNumber(number, string):

    string_len = len(string)

    factor = pow(10, string_len - 1)

    roundedNumber = round(number/factor)

    if(int(string[string_len -1]) == 5):  roundedNumber = math.ceil(number/factor)

    return roundedNumber * factor

while tc > 0:
    tc -= 1
    string = input()
    number = int(string)
    print(roundNumber(number, string))
