import time
from PIL import ImageGrab

time.sleep(5) # 프로그램 실행 후 5초 대기
for i in range(1, 11): # 총 10장
    img = ImageGrab.grab() # 스크린샷 촬영하여 저장
    img.save(f"Image{i}.png")
    time.sleep(2) # 2초마다 촬영