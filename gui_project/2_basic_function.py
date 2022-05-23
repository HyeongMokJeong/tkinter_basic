from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

root = Tk()
root.title("Jeong GUI")

# 파일 추가, 선택 삭제 함수
def add_file():
    files = filedialog.askopenfilenames(title='이미지 파일을 선택하세요.', \
                                        filetypes=(("이미지 파일", '*.png, *.jpg, *.jpeg'), ('모든 파일', '*.*')), \
                                        initialdir=r"C:\Users\jhm10\Downloads") # 최초 경로

    #사용자가 선택한 파일 목록 출력
    for file in files:
        list_file.insert(END, file)

def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 저장 경로 함수 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory(title='저장할 폴더를 선택하세요.')
    if folder_selected is None: # 사용자가 취소를 눌렀을 떄
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# 시작 함수
def start():
    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", '이미지 파일을 추가하세요')
        return
    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", '저장 경로를 선택하세요.')
        return

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill='x', pady=5)

btn_add_file = Button(file_frame, text='파일 추가', padx=5, pady=5, width=12, command=add_file)
btn_add_file.pack(side='left', padx=10)

btn_del_file = Button(file_frame, text='선택 삭제', padx=5, pady=5, width=12, command=del_file)
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

txt_dest_path = Entry(frame_savelocal)
txt_dest_path.pack(side='left', fill='x', expand=True, ipady=4, padx=5, pady=5)

btn_save_local = Button(frame_savelocal, text='찾아보기', command=browse_dest_path)
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

# 하단 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill='x', pady=5)

btn_close = Button(frame_run, text="닫기", command=root.quit, padx=5, pady=5, width=10)
btn_close.pack(side='right', padx=10, pady=5)

btn_start = Button(frame_run, text="시작", command=start, padx=5, pady=5, width=10)
btn_start.pack(side='right', padx=10, pady=5)

root.resizable(False, False)
root.mainloop()