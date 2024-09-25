tc = int(input())


def so_phat_loc(str):
    for i in range(0, len(str)):
        if(str[len(str) - 2] == '8' and str[len(str) -1] == '6'):
            return "YES"
    return "NO"    
    

while tc > 0: 
    tc -= 1
    str  = input()
    print(so_phat_loc(str))