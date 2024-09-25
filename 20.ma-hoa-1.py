tc  = int(input())

def decoded(string): 
    cnt  = 1
    
    for i in range(0, len(string) - 1):
        if(string[i] ==  string[i + 1]):
            cnt += 1
        else:
            print(cnt,string[i],end="")
            print()
            cnt = 1    

    


while tc > 0: 
    tc -= 1
    string  = input()
    decoded(string)