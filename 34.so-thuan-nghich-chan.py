def kiem_tra_so_thuan_nghich_chan(n):
    s = str(n)
    l = 0
    r = len(s) - 1

    if(len(s) < 2 or len(s) % 2 != 0): return False

    while(l < r):
        if(s[l] != s[r] or int(s[l]) % 2 != 0 or int(s[r]) % 2 != 0): return False
        else: 
            l+=1
            r-=1

    return True

tc  = int(input())
while tc > 0:

    tc -= 1
    ip = int(input())

    for i in range(2, ip):
      if(kiem_tra_so_thuan_nghich_chan(i)): 
         print(i, end=" ")  
    print() 

