def tinh_tong_phan_thuc(number):
    sum = 0
    if(number % 2 != 0):
        for i in range(1, number + 1, 2):
            sum += 1 / i
    else: 
        for i in range(2, number + 1, 2):
            sum += 1 / i
    return sum


tc = int(input())

while tc > 0:
    tc -= 1
    number  = int(input())
    print("{:0.6f}".format(tinh_tong_phan_thuc(number)))
                

      