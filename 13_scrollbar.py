from tkinter import *

root = Tk()
root.title("Jeong GUI") #이름
root.geometry("640x480+450+200") #크기 (가로x세로 + x좌표 + y좌표)
root.resizable(True, False) #창 크기 변경 불가

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

#set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode='extended', height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32):
    listbox.insert(END, str(i) + '일')
listbox.pack(side='left')

scrollbar.config(command=listbox.yview)

root.mainloop() #루프를 통해 창 닫히지 않게 해줌