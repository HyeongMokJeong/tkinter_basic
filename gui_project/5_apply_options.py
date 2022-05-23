from tkinter import *
from tkinter import filedialog
from PIL import Image
import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

root = Tk()
root.title("Jeong GUI")

# 파일 추가, 선택 삭제 함수
def add_file():
    files = filedialog.askopenfilenames(title='이미지 파일을 선택하세요.', \
                                        filetypes=(("이미지 파일", '*.png'), ('모든 파일', '*.*')), \
                                        initialdir=r"C:\Users\jhm10\Desktop\pg\파이썬\gui_basic") # 최초 경로

    #사용자가 선택한 파일 목록 출력
    for file in files:
        list_file.insert(END, file)

def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 저장 경로 함수 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory(title='저장할 폴더를 선택하세요.')
    if folder_selected is '': # 사용자가 취소를 눌렀을 떄
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# 이미지 통합 함수
def merge_image():
    try:
        images = [Image.open(x) for x in list_file.get(0, END)]
        # size -> size[0] : width, size[1] : height
        # 사이즈를 계산하여 가장 큰 사진을 기준으로 통합함

        # 가로 넓이
        img_widths = combobox_width.get()
        if img_widths == '원본유지':
            img_width = -1 # -1일때는 원본 기준
        else:
            img_width = int(img_widths)

        # 간격
        img_space = combobox_interval.get()
        if img_space == '좁게':
            img_space = 30
        if img_space == '보통':
            img_space = 60
        if img_space == '넓게':
            img_space = 90
        if img_space == '없음':
            img_space = 0

        # 포맷
        img_format = combobox_format.get().lower() # 확장자 명 받아와서 소문자로 변경


        # 이미지 사이즈 리스트에 넣어서 하나씩 처리
        image_sizes = []
        if img_width > -1:
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
        else:
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        widths, heights = zip(*(image_sizes))

        # 최대 넓이, 전체 높이 구하기
        max_width, total_height = max(widths), sum(heights)

        # 스케치북 준비
        if img_space >0: # 이미지 간격 옵션 정보
            total_height += (img_space * len(images) -1)
        result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255)) #흰색
        y_offset = 0 # y 위치정보
        for idx, img in enumerate(images):
            # 가로크기 옵션은 image_sizes 에만 반영이 되었으므로 img 에서도 크기 조정 필요
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space) # 복사한 사진 높이만큼 더해주기

            progress = (idx+1) / len(images) * 100 # 실제 퍼센트 정보 계산
            p_var.set(progress)
            progressbar.update()

        # 포맷 옵션 처리
        dest_path = os.path.join(txt_dest_path.get(), f'photo.{img_format}')
        result_img.save(dest_path)
        msgbox.showinfo("알림", '작업이 완료되었습니다.')
    except Exception as err:
        msgbox.showerror("에러", err)

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

    # 이미지 통합 작업
    merge_image()

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

values_width = ['원본유지', '1024', '800', '640']
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