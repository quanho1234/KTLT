print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
import math

def Tinh(R):
    # Kiểm tra giá trị bán kính
    if R <= 0:
        print("Bán kính không hợp lệ. Vui lòng nhập bán kính dương.")
        return
    
    # Tính chu vi và diện tích
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R**2
    
    # In kết quả
    print(f"Chu vi hình tròn là: {chu_vi:.2f}")
    print(f"Diện tích hình tròn là: {dien_tich:.2f}")

# Nhập bán kính từ bàn phím
try:
    R = float(input("Nhập bán kính hình tròn: "))
    Tinh(R)
except ValueError:
    print("Giá trị nhập vào không hợp lệ. Vui lòng nhập một số.")
