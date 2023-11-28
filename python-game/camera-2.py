import cv2
import mediapipe as mp
import threading
import numpy as np
import time

# 設定計時器時間（秒）
TIMER_SECONDS = 60

# 初始化 MediaPipe Hand 模型
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# 設定攝像頭
cap = cv2.VideoCapture(0)

# 載入背景圖片
background = cv2.imread("soccer_2.png")

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
        print(timer_count)
        time.sleep(1)

    # 顯示結束畫面
    show_final_screen()

# 啟動計時器
threading.Thread(target=start_timer).start()

with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        # 讀取攝像頭畫面
        success, image = cap.read()
        if not success:
            break

        # 轉換圖片色彩空間為 RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 調整背景圖片大小為攝像頭畫面大小
        background_resized = cv2.resize(background, (image.shape[1], image.shape[0]))

        # 偵測手部位置
        results = hands.process(image)

        # 將 RGB 圖片轉換為 BGR 色彩空間
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # 繪製手部位置
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # 在背景圖片上顯示攝像頭畫面
        combined_image = cv2.addWeighted(background_resized, 0.3, image, 1, 0)
        cv2.imshow('MediaPipe Hands', combined_image)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()