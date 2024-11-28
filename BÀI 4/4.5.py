print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
input_string = input("Nhập các từ (cách nhau bằng dấu cách): ")

words = input_string.split()

reversed_words = words[::-1]

print("Các từ theo thứ tự ngược lại là: " + " ".join(reversed_words))
