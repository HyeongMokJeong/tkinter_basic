from tkinter import *

root = Tk()
root.title("Jeong GUI") #이름
root.geometry("640x480+450+200") #크기 (가로x세로 + x좌표 + y좌표)
root.resizable(True, False) #창 크기 변경 불가

Label(root,text='메뉴를 선택해 주세요').pack(side='top')

Button(root, text='주문하기').pack(side='bottom')

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side='left', fill='both', expand=True)

Button(frame_burger, text='햄버거').pack()
Button(frame_burger, text='치즈버거').pack()
Button(frame_burger, text='치킨버거').pack()

frame_drink = LabelFrame(root, text='음료')
frame_drink.pack(side='right')

Button(frame_drink, text='콜라').pack()
Button(frame_drink, text='사이다').pack()

root.mainloop() #루프를 통해 창 닫히지 않게 해줌