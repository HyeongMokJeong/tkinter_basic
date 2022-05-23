from tkinter import *

root = Tk()
root.title("Jeong GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼3") #pad는 버튼 여백
btn2.pack()

btn3 = Button(root, width=10, height=3, text="버튼3") #width는 버튼 크기
btn3.pack()

btn4 = Button(root, fg='red', bg='yellow', text="버튼4")
btn4.pack()

photo = PhotoImage(file="C:/Users/jhm10/Desktop/pg/파이썬/gui_basic/img.png")
btn5 = Button(root, image=photo)
btn5.pack()

def btncmd():
    print("버튼이 클릭되었습니다.")
btn6 = Button(root, text="동작 버튼", command=btncmd)
btn6.pack()

root.mainloop() #루프를 통해 창 닫히지 않게 해줌