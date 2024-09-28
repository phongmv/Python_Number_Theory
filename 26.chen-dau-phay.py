def format_number_with_commas(N):
    # Sử dụng định dạng chuỗi có sẵn của Python để chèn dấu phẩy
    return f"{N:,}"

# Input: số nguyên dương N
N = int(input())

# Output: số đã được định dạng
print(format_number_with_commas(N))
