tc = int(input())


def kiemTraSoThuanNghich(number):
    s = str(number)
    l = 0
    r = len(s) - 1
    while(l < r):
        l+=1
        r-=1
        if(s[l] != s[r]): return False

    return True

while tc > 0:
    tc -= 1
    number = int(input())

    for i in range(10,number):
        if(kiemTraSoThuanNghich(i) and i % 2 == 0): print(i, end=" ")
    print()    

   
