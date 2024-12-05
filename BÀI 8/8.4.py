print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
from tkinter import *

window = Tk()
window.title("Ứng dụng Tkinter")
window.geometry('350x200')

lbl = Label(window, text="Chào bạn!", font=("Arial", 14))
lbl.grid(column=0, row=0, pady=20)
def clicked():
    lbl.configure(text="Button đã được nhấn !!")

btn = Button(window, text="Nhấn tôi", command=clicked, bg="blue", fg="white", font=("Arial", 12))
btn.grid(column=1, row=0)

def on_key_press(event):
    lbl.configure(text=f"Bạn đã nhấn phím: {event.char}")
window.bind("<Key>", on_key_press)

window.mainloop()
