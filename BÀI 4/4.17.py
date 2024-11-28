print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
n = int(input("Nhập số n: "))
for x in range(1, n):
    sum_divisors = 0
    for i in range(1, x):
        if x % i == 0:
            sum_divisors += i
    if sum_divisors > x:
        print(x)
