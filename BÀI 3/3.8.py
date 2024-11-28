print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
import math
      
pos = [0, 0]

while True:
    s = input("Nhập hướng và số bước (ví dụ: UP 5). Nhấn Enter để dừng: ")
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]  
    steps = int(movement[1])  

    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps

distance = math.sqrt(pos[0]**2 + pos[1]**2)

print("Khoảng cách từ vị trí hiện tại đến vị trí ban đầu là:", int(round(distance)))
