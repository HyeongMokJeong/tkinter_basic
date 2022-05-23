from tkinter import *

root = Tk()
root.title("Jeong GUI")
root.geometry("640x480+450+200")

txt = Text(root, width=30, height=5) #text는 여러줄 입력
txt.pack()
txt.insert(END, "글자를 입력하세요")


e = Entry(root,width=30) #entry는 한줄 입력
e.pack()
e.insert(0, '한 줄만 입력하세요.')

def btncmd():
    print(txt.get("1.0", END)) #1:첫번째 라인, 0: 0번째 column 위치
    print(e.get())

    txt.delete("1.0",END)
    e.delete(0,END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() #루프를 통해 창 닫히지 않게 해줌