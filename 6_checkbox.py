from tkinter import *

root = Tk()
root.title("Jeong GUI")
root.geometry("640x480+450+200")

chkvar = IntVar() #chkvar에 int 형으로 값을 저장한다
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
chkbox.select() #자동 선택 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text='일주일 동안 보지 않기', variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) #0은 체크 해재, 1은 체크
    print(chkvar2.cget('text'))

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() #루프를 통해 창 닫히지 않게 해줌