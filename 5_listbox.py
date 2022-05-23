from tkinter import *

root = Tk()
root.title("Jeong GUI")
root.geometry("640x480+450+200")

listbox = Listbox(root, selectmode="extended", height=0) #height 표시할 값 개수
listbox.insert(0,"사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END,"수박")
listbox.insert(END,"포도")
listbox.pack()

def btncmd():
    #삭제
    #listbox.delete(END) #맨 뒤 항목 삭제 / 0은 앞 항목

    #개수 확인
    #print("리스트에는",listbox.size(),"개가 있어요")

    #항목 확인
    #print("1번째부터 3번째까지의 항목: ", plistlib.get(0,2))

    #선택된 항목 확인(idx값으로 반환)
    print("선택된 항목: ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() #루프를 통해 창 닫히지 않게 해줌