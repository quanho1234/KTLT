print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
full_name = input("Nhập tên người (họ và tên): ")
name_parts = full_name.split()
if len(name_parts) >= 2:
    first_name = name_parts[0]
    last_name = name_parts[1]
    print(f"Họ: {first_name}")
    print(f"Tên riêng: {last_name}")
else:
    print("Vui lòng nhập đầy đủ họ và tên.")
