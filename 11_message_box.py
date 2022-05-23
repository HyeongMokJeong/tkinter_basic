import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Jeong GUI") #이름
root.geometry("640x480+450+200") #크기 (가로x세로 + x좌표 + y좌표)
root.resizable(True, False) #창 크기 변경 불가

def info():
    msgbox.showinfo('알림', '정상적으로 예매 완료되었습니다.')

def warn():
    msgbox.showwarning('경고', '해당 좌석은 매진되었습니다.')

def error():
    msgbox.showerror('경고', '결제 오류가 발생했습니다.')

def okcancel():
    msgbox.askokcancel('확인 / 취소', '해당 좌석은 유아동반석입니다. 예매하시겠습니까?')

def retrycancel():
    msgbox.askretrycancel('재시도 / 취소', '일시적인 오류입니다. 다시 시도하시겠습니까?')

def yesno():
    msgbox.askyesno('예 / 아니오', '해당 좌석은 역방향입니다. 예매하시겠습니까?') #메세지박스 이름, 내용

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message='예매 내역이 저장되지 않았습니다.\n저장 후 프로그램을 종료하시겠습니까?') #메세지박스 이름, 내용
    #True, False, None -> 예 1, 아니오 0, 그 외
    if response == 1: #예
        print("예")
    elif response == 0: #아니오
        print("아니오")
    else:
        print("취소")
Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="경고").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop() #루프를 통해 창 닫히지 않게 해줌