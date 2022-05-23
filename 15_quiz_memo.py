from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장") #이름
root.geometry("640x480+450+200") #크기 (가로x세로 + x좌표 + y좌표)

menu = Menu(root)

# 스크롤 바
scrollbar = Scrollbar(root)
scrollbar.pack(side='right', fill='y')

# 텍스트 영역
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side='left', fill='both', expand=True) #fill은 요구된 공간 채우기, expand는 요구되지 않은 공간 채우기

scrollbar.config(command=txt.yview)

def open_file():
    f = open("mynote.txt", 'r')
    txt.insert(END, f.read())
    f.close()

def save_file():
    f = open("mynote.txt", 'w')
    user_write = txt.get("1.0", END)
    f.write(user_write)
    f.close()

#파일 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="%-25s %25s" %('새로 만들기(N)', 'Ctrl+N'))
menu_file.add_command(label="%-27s %27s" %('새 창(W)', 'Ctrl+Shift+N'))
menu_file.add_command(label="%-28s %28s" %('열기(O)...', 'Ctrl+O'), command=open_file)
menu_file.add_command(label="%-28s %28s" %('저장(S)', 'Ctrl+S'), command=save_file)
menu_file.add_command(label="%-21s %21s" %('다른 이름으로 저장(A)', 'Ctrl+Shift+S'))
menu_file.add_separator()
menu_file.add_command(label='페이지 설정(U)...')
menu_file.add_command(label="%-28s %28s" %('인쇄(P)...', 'Ctrl+P'))
menu_file.add_separator()
menu_file.add_command(label="끝내기(X)", command=root.quit)

menu.add_cascade(label='파일(F)', menu=menu_file)
menu.add_cascade(label='편집(E)')
menu.add_cascade(label='서식(O)')
menu.add_cascade(label='보기(V)')
menu.add_cascade(label='도움말(H)')


root.config(menu=menu)
root.mainloop() #루프를 통해 창 닫히지 않게 해줌
