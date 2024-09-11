string = input()

# kiem tra so luong chu so 4, sl chu so 7
def count(string):
    cnt = 0
    for i in range(0, len(string)):
        if int(string[i]) == 4 or int(string[i]) ==7: cnt += 1
    return cnt    


# sum va so sanh
def check(cnt):
    if cnt == 4 or cnt == 7: print("YES")
    else: print("NO")

check(count(string))