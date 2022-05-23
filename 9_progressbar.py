import tkinter.ttk as ttk
import time
from tkinter import *

root = Tk()
root.title("Jeong GUI")
root.geometry("640x480+450+200")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") #indeterminate 끝이 정해지지 않음
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) #10ms마다 움직임
# progressbar.pack()
#
# def btncmd():
#     progressbar.stop() #작동 중지
#
# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) #0.01초 대기

        p_var2.set(i) #progressbar의 값 설정
        progressbar2.update()
        print(p_var2.get())

btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()

root.mainloop() #루프를 통해 창 닫히지 않게 해줌