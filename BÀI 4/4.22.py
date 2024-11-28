print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
even_digit_numbers = []
for number in range(1000, 3001):
    str_number = str(number)
    if all(int(digit) % 2 == 0 for digit in str_number):
        even_digit_numbers.append(str_number)
print(",".join(even_digit_numbers))
