tc = int(input())


def checkIsPrime(number):
    if(number < 2): return False
    for i  in range(2, number):
        if(number % i == 0): return False
    return True    

def primeCounter(number): 
        string = str(number)
        primeCnt = 0
        notPrimeCnt = 0
        for i in string:
             if(checkIsPrime(int(i))): primeCnt+=1
             else: notPrimeCnt+=1
        return primeCnt > notPrimeCnt     

while tc > 0:
    tc -= 1
    number = int(input())
    if(checkIsPrime(len(str(number))) and primeCounter(number)): print("YES")
    else: print("NO")


