n = int(input("Nhap so phan tu cua mang: "))
arr = []

# nhap phan tu vao mang
for i in range(0, n):
    el = int(input(f"nhap phan tu thu {i +1}: "))
    arr.append(el)

# swap
def swap(a, b):
    return b, a

# selection sort
for i in range(0, n - 1):
    
    min_pos = i
    
    for j in range(i + 1, n):
        
        if arr[i] > arr[j]:  min_pos = j    
   
    arr[i], arr[min_pos] = swap(arr[i], arr[min_pos])
        


# in phan tu cua mang
for i in range(0, n - 1 ):
    print(arr[i])