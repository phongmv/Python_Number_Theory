tc = int(input())

def checkSoKhongGiam(str):
    for i in range(0, len(str) - 1):
        if(int(str[i]) > int(str[i+1])): return "NO"
    return "YES"    



while tc > 0: 
    tc -=1
    str  = input()
    print(checkSoKhongGiam(str))