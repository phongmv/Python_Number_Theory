tc = int(input())


def decode(string):
    result = ""
    for i in range(0, len(string), 2):
        char  = string[i]
        count  = int(string[i+1])
        result += char * count
    return result    

while tc > 0:
    tc -= 1
    string = input()
    print(decode(string))