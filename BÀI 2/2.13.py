print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
print("Giải phương trình bậc 2: ax2 + bx + c = 0 (a, b khác 0)")
print("============")
a = float(input("Mời bạn nhập hệ số a: "))
while True:
    if a == 0:
        a = float(input("Số a phải khác 0. Mời nhập lại số a: "))
    else:
        break
    
b = float(input("Mời bạn nhập hệ số b: "))
while True:
    if b == 0:
        b = float(input("Số b phải khác 0. Mời nhập lại số b: "))
    else:
        break
c = float(input("Mời bạn nhập hệ số c: "))
delta = b**2 - 4 * a * c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
    print("x2 = ", (-(b) - math.sqrt(delta))/(2*a) )
