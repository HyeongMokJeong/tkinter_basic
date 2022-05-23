from tkinter import *

root = Tk()
root.title("Jeong GUI") #이름
root.geometry("640x480+450+200") #크기 (가로x세로 + x좌표 + y좌표)
root.resizable(True, False) #창 크기 변경 불가

root.mainloop() #루프를 통해 창 닫히지 않게 해줌