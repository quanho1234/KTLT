print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
binary_input = input("Nhập chuỗi các số nhị phân (4 chữ số, phân tách bởi dấu phẩy): ")
binary_numbers = binary_input.split(',')
divisible_by_5 = []
for binary in binary_numbers:
    decimal = int(binary, 2)
    if decimal % 5 == 0:
        divisible_by_5.append(binary)
print(",".join(divisible_by_5))
