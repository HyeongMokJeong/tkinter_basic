from tkinter import *

root = Tk()
root.title("Jeong GUI")

label1 = Label(root, text='안녕하세요')
label1.pack()

photo = PhotoImage(file="C:/Users/jhm10/Desktop/pg/파이썬/gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2
    photo2 = PhotoImage(file="C:/Users/jhm10/Desktop/pg/파이썬/gui_basic/img2.png")
    label2.config(image=photo2)

btn = Button(root, text='클릭', command=change)
btn.pack()

root.mainloop() #루프를 통해 창 닫히지 않게 해줌