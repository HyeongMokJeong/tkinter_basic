from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Jeong GUI")

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill='x', pady=5)

btn_add_file = Button(file_frame, text='파일 추가', padx=5, pady=5, width=12)
btn_add_file.pack(side='left', padx=10)

btn_del_file = Button(file_frame, text='선택 삭제', padx=5, pady=5, width=12)
btn_del_file.pack(side='right', padx=10)

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill='both', padx=10, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side='right', fill='y')

list_file = Listbox(list_frame, selectmode='extended', height=15, yscrollcommand=scrollbar.set)
list_file.pack(side='left', fill='both', expand=True)
scrollbar.config(command=list_file.yview)

# 저장경로 프레임
frame_savelocal = LabelFrame(root, text='저장 경로', height=10)
frame_savelocal.pack(fill='x', padx=10, pady=5)

e = Entry(frame_savelocal)
e.pack(side='left', fill='x', expand=True, ipady=4, padx=5, pady=5)

btn_save_local = Button(frame_savelocal, text='찾아보기')
btn_save_local.pack(side='right', padx=5)

# 옵션 프레임
frame_option = LabelFrame(root, text='옵션')
frame_option.pack(fill='x', padx=10, pady=5)

label_width = Label(frame_option, text='가로넓이')
label_width.pack(side='left', padx=5, pady=10)

values_width = ['원본 유지', '1024', '800', '640']
combobox_width = ttk.Combobox(frame_option, width=10, height=4, values=values_width, state='readonly')
combobox_width.current(0)
combobox_width.pack(side='left', padx=5, pady=5)

label_width = Label(frame_option, text='간격')
label_width.pack(side='left', padx=5, pady=5)

values_interval = ['없음', '좁게', '보통', '넓게']
combobox_interval = ttk.Combobox(frame_option, width=10, height=4, values=values_interval, state='readonly')
combobox_interval.current(0)
combobox_interval.pack(side='left', padx=5, pady=5)

label_format = Label(frame_option, text='포맷')
label_format.pack(side='left', padx=5, pady=5)

values_format = ['PNG', 'JPG', 'BMP']
combobox_format = ttk.Combobox(frame_option, width=10, height=3, values=values_format, state='readonly')
combobox_format.current(0)
combobox_format.pack(side='left', padx=5, pady=5)

# 진행상황 프레임
frame_progressbar = LabelFrame(root, text='진행 상황')
frame_progressbar.pack(fill='x', padx=10, pady=5)

p_var = DoubleVar()
progressbar = ttk.Progressbar(frame_progressbar, maximum=100, variable=p_var)
progressbar.pack(fill='x', padx=5, pady=5)

def start():
    pass


# 하단 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill='x', pady=5)

btn_close = Button(frame_run, text="닫기", command=root.quit, padx=5, pady=5, width=10)
btn_close.pack(side='right', padx=10, pady=5)

btn_start = Button(frame_run, text="시작", command=start, padx=5, pady=5, width=10)
btn_start.pack(side='right', padx=10, pady=5)

root.resizable(False, False)
root.mainloop()