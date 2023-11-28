import cv2
import mediapipe as mp
import threading
import numpy as np
import time
import random
import pygame
import subprocess

# ------------------------------
# 換圖片(X)
# 視窗大小800x600(X)
# ------------------------------

# 定義圈
circle_last_time = time.time()
TIMER_SECONDS = 60
circle_interval = 3

# 初始化 MediaPipe Hand 模型
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# 設定攝像頭
cap = cv2.VideoCapture(0)
initial_width, initial_height = 800, 600

# 載入背景圖片
background = cv2.imread("soccer_2.png")

# 載入替代圓形的圖片
replacement_image = cv2.imread("basketball.png")  # Replace with the path to your image

# 設定替代圓形的位置和大小
replacement_pos = (0, 0)
replacement_size = (50, 50)

# 設定計時器
def start_timer():
    # 設定計時器初始值
    global timer_count
    timer_count = TIMER_SECONDS

    # 每秒減少計時器值，直到計時器為 0
    while timer_count > 0:
        timer_count -= 1
        print('Time:', timer_count)
        time.sleep(1)

# 出現替代圓形的函式
def draw_replacement_image(image, pos, size):
    # 調整替代圓形的圖片大小以匹配指定的尺寸
    resized_replacement = cv2.resize(replacement_image, (size[0], size[1]))

    # 在圖片上貼上調整大小後的替代圓形的圖片
    image[pos[1]:pos[1] + size[1], pos[0]:pos[0] + size[0]] = resized_replacement


# 啟動計時器
threading.Thread(target=start_timer).start()
score = 0

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

        # 在右上角顯示倒數計時
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, f'Score: {score}', (0, 30), font, 1, (0, 0, 0), 3, cv2.LINE_AA)
        # 在右上角顯示倒數計時
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, f'Time left: {timer_count}', (image.shape[1] - 210, 30), font, 1, (0, 0, 0), 3, cv2.LINE_AA)

        # 透過 MediaPipe Hand 模型偵測手部關鍵點
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # 如果偵測到手部關鍵點
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # 取得食指指尖的位置
                index_finger_tip = tuple(np.multiply(
                    (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x,
                    hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y),
                    [image.shape[1], image.shape[0]]
                ).astype(int))

                # 檢查食指指尖是否在替代圓形內
                if (replacement_pos[0] <= index_finger_tip[0] <= replacement_pos[0] + replacement_size[0] and
                        replacement_pos[1] <= index_finger_tip[1] <= replacement_pos[1] + replacement_size[1]):
                    # 設定新的替代圓形位置
                    score += 1
                    replacement_pos = (random.randint(0, background.shape[1] - replacement_size[0]),
                                       random.randint(0, background.shape[0] - replacement_size[1]))

        # 每隔一段時間出現一個替代圓形
        if time.time() - circle_last_time > circle_interval:
            circle_last_time = time.time()
            replacement_pos = (random.randint(0, background.shape[1] - replacement_size[0]),
                               random.randint(0, background.shape[0] - replacement_size[1]))

        # 繪製背景圖片和替代圓形
        draw_replacement_image(image, replacement_pos, replacement_size)

        # 重新設定 background 大小為 image 大小
        background = cv2.resize(background, (image.shape[1], image.shape[0]))

        # 繪製背景圖片和替代圓形
        cv2.addWeighted(background, 1, image, 0.5, 0, image)
        draw_replacement_image(image, replacement_pos, replacement_size)

        # 顯示圖片
        cv2.imshow('Hand Tracking', image)

        # 檢查遊戲時間
        if timer_count == 0:
            print("遊戲結束，總分：", score)
            break

        # 按下Esc鍵結束遊戲
        if cv2.waitKey(1) == 27:
            timer_count = 0
            break

# 關閉相機&計時器
cap.release()
cv2.destroyAllWindows()

# ------------------------------
# 分數頁面
# ------------------------------
pygame.init()

end_window = pygame.display.set_mode((800, 600))
background_img = pygame.image.load("score_bg.png")  # 替换为您的背景图像路径
end_window.blit(background_img, (0, 0))

end_font = pygame.font.SysFont(None, 60)
end_text = end_font.render(f"Game Over! Your Score: {score}", True, (255, 255, 255))
text_rect = end_text.get_rect(center=end_window.get_rect().center)  # 至中
end_window.blit(end_text, text_rect)

pygame.display.update()
# ------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 關閉頁面
cap.release()
pygame.quit()
subprocess.run(["python", "AR_home.py"])  # 跳轉
# ------------------------------
