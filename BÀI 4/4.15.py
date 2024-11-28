print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
input_string = input("Nhập một chuỗi các từ tiếng Anh: ")
words = input_string.split()
words.sort()
for word in words:
    print(word)
