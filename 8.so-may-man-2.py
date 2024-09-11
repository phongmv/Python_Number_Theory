tc = int(input())


def check(str):
    for i in range(0, len(str)):
        
        if int(str[i]) != 4 and int(str[i]) != 7: return "NO"
    
    return "YES"



while tc > 0:
    tc -= 1
    str = input()
    print(check(str))

