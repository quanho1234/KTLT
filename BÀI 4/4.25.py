print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
input_str = input("Nhập các số cách nhau bằng dấu phẩy: ")
numbers = [int(num) for num in input_str.split(',')]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Các số lẻ là:", odd_numbers)
