import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Jeong GUI")
root.geometry("640x480+450+200")

values = [str(i) + '일' for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") #최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state='readonly') #hight는 한번에 보여지는 목록 개수
readonly_combobox.current(0) #0번째 인덱스값 선택
readonly_combobox.pack()

def btncmd():
    idx = list(enumerate(combobox.get()))
    print(idx[0][0])
    print(readonly_combobox.get())

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop() #루프를 통해 창 닫히지 않게 해줌