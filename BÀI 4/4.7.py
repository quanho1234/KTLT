print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
input_string = input("Nhập chuỗi: ")
result_string = ''.join([char for char in input_string if not char.isdigit()])
print("Chuỗi sau khi loại bỏ các chữ số:", result_string)
