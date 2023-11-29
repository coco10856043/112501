import cv2
import mediapipe as mp
import threading
import cvzone
import numpy as np
import time
import random
import pygame
import subprocess
import sys, mysql.connector
# ------------------------------
# 換圖片(X)
# 視窗大小800x600(X)
# ------------------------------

# 定義圈
circle_last_time = time.time()
TIMER_SECONDS = 60

# 初始化 MediaPipe Hand 模型
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# 設定攝像頭
cap = cv2.VideoCapture(0)
initial_width, initial_height = 800, 600

result_from_get_account = sys.argv[1]
result_list = result_from_get_account.strip('[()]').split(', ')
result_list = [item.strip("'") for item in result_list]

# 資料庫連線參數
db_config = {
    'host': '140.131.114.140',  # 修改成你的 MySQL 伺服器 IP
    'port': 3306,         # 修改成你的 MySQL 伺服器 Port
    'user': '112501',        # 修改成你的 MySQL 使用者帳號
    'password': 'SportsWorld_112501',    # 修改成你的 MySQL 使用者密碼
    'database': '112-112501',  # 修改成你的資料庫名稱
}

# 連接到資料庫
conn = mysql.connector.connect(**db_config)


# 載入背景圖片
background = cv2.imread("soccer_2.png")

# 設定黃色圓形
circle_pos = (0, 0) # 初始位置
circle_radius = 25  # 半徑
circle_interval = 4 # 出現間隔

# 載入圖片
image_net = cv2.imread('net.png', cv2.IMREAD_UNCHANGED)
if image_net.shape[2] == 3:  # 如果是三通道，加入透明通道
    alpha_channel = np.ones((image_net.shape[0], image_net.shape[1]), dtype=image_net.dtype) * 255
    image_net = cv2.merge((image_net, alpha_channel))
# 載入圖片
image_ball = cv2.imread('baseball.png', cv2.IMREAD_UNCHANGED)

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

# 出現黃色圓形的函式
def draw_yellow_circle(image, image_ball, pos):
    # 在圖片上繪製黃色圓形
    # cv2.circle(image, pos, radius, (0, 255, 255), -1)
    if image_ball is not None:
        if image_ball.shape[2] == 3:  # 如果是三通道，加入透明通道
            alpha_channel = np.ones((image_ball.shape[0], image_ball.shape[1]), dtype=image_ball.dtype) * 255
            image_ball = cv2.merge((image_ball, alpha_channel))
        image = cvzone.overlayPNG(image, image_ball, pos)

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
                image = cvzone.overlayPNG(image, image_net, index_finger_tip)

                # 檢查食指指尖是否在黃色圓形內
                # if (index_finger_tip[0]-circle_pos[0])**2 + (index_finger_tip[1]-circle_pos[1])**2 <= circle_radius**2:
                #     # 設定新的黃色圓形位置
                #     score += 1
                #     circle_pos = (random.randint(circle_radius, background.shape[1]-circle_radius), 
                #                 random.randint(circle_radius, background.shape[0]-circle_radius))
                # 檢查食指指尖是否在黃色圓形內
                if circle_pos[0] < index_finger_tip[0] < circle_pos[0] + image_ball.shape[1] and circle_pos[1] < index_finger_tip[1] < circle_pos[1] + image_ball.shape[0]:
                    # 設定新的黃色圓形位置
                    score += 1
                    circle_pos = (random.randint(circle_radius, background.shape[1]-circle_radius), 
                                random.randint(circle_radius, background.shape[0]-circle_radius))

        # 每隔一段時間出現一個黃色圓形
        if time.time() - circle_last_time > circle_interval:
            circle_last_time = time.time()
            circle_pos = (random.randint(circle_radius, background.shape[1]-circle_radius), 
                        random.randint(circle_radius, background.shape[0]-circle_radius))

        # 繪製背景圖片和黃色圓形
        draw_yellow_circle(image, image_ball, circle_pos)

        # 重新設定 background 大小為 image 大小
        background = cv2.resize(background, (image.shape[1], image.shape[0]))

        # 繪製背景圖片和黃色圓形
        # cv2.addWeighted(background, 1, image, 0.5, 0, image)
        # draw_yellow_circle(image, circle_pos, circle_radius)

        # 顯示圖片
        cv2.imshow('Hand Tracking', image)

        # 檢查遊戲時間
        if timer_count == 0:
            print("遊戲結束，總分：", score)

            initface_cursor= conn.cursor()
            query1 = "INSERT INTO game (`user_id`, `game_type`, `game_time`, `scores`) VALUES (%s, '1', current_timestamp(), %s);"
            values = (result_list[0], score)
            
            initface_cursor.execute(query1, values)
            conn.commit()
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
background_img = pygame.image.load("game_png/score_bg.png")  # 替换为您的背景图像路径
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
subprocess.run(["python", "AR_home.py", result_from_get_account])  # 跳轉
# ------------------------------
