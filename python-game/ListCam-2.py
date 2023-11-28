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
circle_interval = 3

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
        print(timer_count)
        time.sleep(1)

    # 顯示結束畫面
    show_final_screen()

# 出現黃色圓形的函式
def draw_yellow_circle(image, pos, radius):
    # 在圖片上繪製黃色圓形
    cv2.circle(image, pos, radius, (0, 255, 255), -1)

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

        # 將圖片從 BGR 轉換成 RGB，因為 MediaPipe Hand 模型需要 RGB 圖片
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # 透過 MediaPipe Hand 模型偵測手部關鍵點
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # 如果偵測到手部關鍵點
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # 取得手部位置
                hand_image = np.zeros_like(image)  # 建立一個與攝像頭畫面大小相同的黑色畫布
                mp_drawing.draw_landmarks(hand_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)  # 繪製手部位置到畫布上

                # 取得食指指尖的位置
                index_finger_tip = tuple(np.multiply(
                    (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x,
                    hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y),
                    [image.shape[1], image.shape[0]]
                ).astype(int))

                # 檢查食指指尖是否在黃色圓形內
                if (index_finger_tip[0]-circle_pos[0])**2 + (index_finger_tip[1]-circle_pos[1])**2 <= circle_radius**2:
                    # 設定新的黃色圓形位置
                    circle_pos = (random.randint(circle_radius, background.shape[1]-circle_radius),
                                  random.randint(circle_radius, background.shape[0]-circle_radius))

        # 每隔一段時間出現一個黃色圓形
        if time.time() - circle_last_time > circle_interval:
            circle_last_time = time.time()
            circle_pos = (random.randint(circle_radius, background.shape[1]-circle_radius),
                          random.randint(circle_radius, background.shape[0]-circle_radius))

        # 重新設定 background 大小為 image 大小
        background = cv2.resize(background, (image.shape[1], image.shape[0]))

        # 合併手部位置的圖像到背景圖片上
        merged_image = cv2.addWeighted(background, 1, hand_image, 0.5, 0)

        # 繪製黃色圓形到合併後的圖像上
        draw_yellow_circle(merged_image, circle_pos, circle_radius)

        # 顯示圖片
        cv2.imshow('Hand Tracking', merged_image)

        # 按下 'q' 鍵可以離開程式
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

# 釋放攝像頭並關閉視窗
cap.release()
cv2.destroyAllWindows()
