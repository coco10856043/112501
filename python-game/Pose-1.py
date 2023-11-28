import cv2
import mediapipe as mp
import threading
import numpy as np
import time
import random

# 定義圈
circle_last_time = time.time()

# 設定計時器時間（秒）
TIMER_SECONDS = 60

# 初始化 MediaPipe Hand 模型
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# 設定攝像頭
cap = cv2.VideoCapture(0)

# 載入背景圖片
background = cv2.imread("soccer_2.png")

# 設定黃色圓形的初始位置
circle_pos = (0, 0)

# 設定黃色圓形的半徑
circle_radius = 25

# 設定黃色圓形出現的時間間隔
circle_interval = 4

# 設定計時器結束後要顯示的畫面
def show_final_screen():
    # 設定畫面大小和顏色
    final_screen = np.zeros((300, 500, 3), np.uint8)
    final_screen[:] = (0, 255, 255)

    # 在畫面上顯示文字
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(final_screen, "Time's up!", (140, 100), font, 2, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(final_screen, "Play again", (60, 200), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(final_screen, "Exit", (330, 200), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

    # 顯示畫面
    while True:
        cv2.imshow('Final Screen', final_screen)
        key = cv2.waitKey(0)

        # 如果按下 'p' 鍵，重新開始遊戲
        if key == ord('p'):
            threading.Thread(target=start_timer).start()
            break

        # 如果按下 'q' 鍵，離開程式
        elif key == ord('q'):
            # 檢查視窗是否被關閉
            if cv2.getWindowProperty('Final Screen', cv2.WND_PROP_VISIBLE) >= 1:
                cap.release()
                cv2.destroyAllWindows()
            break

# 設定計時器
def start_timer():
    # 設定計時器初始值
    timer_count = TIMER_SECONDS

    # 每秒減少計時器值，直到計時器為 0
    while timer_count > 0:
        timer_count -= 1
        print('Time:', timer_count)
        time.sleep(1)


    # 顯示結束畫面
    show_final_screen()

# 出現黃色圓形的函式
def draw_yellow_circle(image, pos, radius):
    # 在圖片上繪製黃色圓形
    cv2.circle(image, pos, radius, (0, 255, 255), -1)