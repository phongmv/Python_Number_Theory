


def encode_string(s): 
    cnt  = 1
    arr = []
    for i in range(0, len(s) -1):
        if(s[i] == s[i + 1]):
            cnt +=1
        else:
            arr.append(f"{cnt}{s[i]}")
            cnt = 1

    arr.append(f"{cnt}{s[-1]}")
    return "".join(arr)       

tc  = int(input())
while tc > 0: 
    tc -= 1
    string = input()
    print(encode_string(string))