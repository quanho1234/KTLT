print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
#################################################
balance = 0
while True:
    transaction = input("Nhập giao dịch (D số hoặc W số, 'x' để kết thúc): ")

    if transaction.lower() == 'x':
        break
    
    action, amount = transaction.split()
    amount = int(amount)  

    if action == 'D':  
        balance += amount
    elif action == 'W':  
        balance -= amount
    else:
        print("Giao dịch không hợp lệ. Vui lòng nhập lại.")
print("Số tiền thực của tài khoản là:", balance)
