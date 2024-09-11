t = int(input())
while t > 0:
    t -= 1
    
    for c in input():
        if c!='4' and c!='7':
            print("NO")
            break
    else: print("YES")
