print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
def benefit(t, n, k):
    # Tính số tiền nhận được sau k tháng
    so_tien = n * (1 + (t / 100) * k)
    return so_tien

# Nhập các giá trị từ bàn phím
try:
    t = float(input("Nhập lãi suất hàng tháng (t%): "))
    n = float(input("Nhập số vốn ban đầu (n): "))
    k = int(input("Nhập số tháng gửi (k): "))
    
    # Tính số tiền nhận được sau k tháng
    tien_nhan_duoc = benefit(t, n, k)
    print(f"Số tiền nhận được sau {k} tháng là: {tien_nhan_duoc:.2f}")
except ValueError:
    print("Dữ liệu nhập vào không hợp lệ. Vui lòng nhập số.")
