print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
def bubbleSort(nlist):
    for i in range(len(nlist)-1):
        for j in range(len(nlist)-1-i):
            if nlist[j] > nlist[j+1]:
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]

if __name__ == "__main__":
    nlist = list(map(int, input("Nhập một danh sách các số nguyên cách nhau bởi dấu cách: ").split()))
    bubbleSort(nlist)
    print("Danh sách sau khi sắp xếp:", nlist)
