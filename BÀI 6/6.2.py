print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong

hcn = Hinhchunhat(5, 3)
dien_tich_hcn = hcn.dien_tich()
print("Diện tích hình chữ nhật là:", dien_tich_hcn)

