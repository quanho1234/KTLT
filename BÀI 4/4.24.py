print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
sentence = input("Nhập vào một câu: ")

upper_count = 0
lower_count = 0

for char in sentence:
    if char.isupper():  
        upper_count += 1
    elif char.islower():  
        lower_count += 1

print("Chữ hoa:", upper_count)
print("Chữ thường:", lower_count)
