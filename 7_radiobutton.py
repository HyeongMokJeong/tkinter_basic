from tkinter import *

root = Tk()
root.title("Jeong GUI")
root.geometry("640x480+450+200")

Label(root, text='메뉴를 선택하세요.').pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text='햄버거', value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text='치즈버거', value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text='불고기버거', value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


Label(root, text='음료를 선택하세요.').pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text='콜라', value='콜라', variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text='사이다', value='사이다', variable=drink_var)
btn_drink3 = Radiobutton(root, text='환타', value='환타', variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get()) #선택된 햄버거의 value
    print(drink_var.get()) #선택된 음료의 value

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop() #루프를 통해 창 닫히지 않게 해줌