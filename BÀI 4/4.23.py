print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
sentence = input("Nhập một câu: ")
letter_count = 0
digit_count = 0
for char in sentence:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():  
        digit_count += 1
print(f"Số chữ cái là: {letter_count}")
print(f"Số chữ số là: {digit_count}")
