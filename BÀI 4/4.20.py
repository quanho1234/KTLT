print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
import math
def binomial_coefficient(n, k):
    return math.comb(n, k)
n = int(input("Nhập số dòng n của tam giác Pascal: "))
for i in range(n):
    row = []
    for j in range(i + 1):
        row.append(binomial_coefficient(i, j))
    print(" ".join(map(str, row)))
