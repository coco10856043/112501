import cv2
import mediapipe as mp
import threading
import time
import random
import pygame
import subprocess
import sys, mysql.connector
# ------------------------------
# 換圖片(X)
# 視窗大小800x600(X)
# ------------------------------
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# 遊戲參數
score = 0
TIMER_SECONDS = 60  # 設定計時器時間（秒）
start_time = time.time()
last_change_time = time.time()

# 遊戲圖片參數
circle_radius = 50
circle_color = (0, 255, 255)  # 黃色
circle_position = (0, 0)

# 要蓋上的圖片
image_to_overlay = cv2.imread('Gophers.png')  # 替換成您的圖片路徑
image_to_overlay = cv2.resize(image_to_overlay, (100, 100))  # 調整圖片大小

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

# 開啟攝像頭
camera = 0
cap = cv2.VideoCapture(camera)

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

    # 顯示結束畫面
    # show_final_screen()

# 啟動計時器
threading.Thread(target=start_timer).start()

# 初始化MediaPipe手部檢測工具
with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        success, image = cap.read()

        if not success:
            print("Ignoring empty camera frame.")
            continue

        # 水平翻轉畫面，形成鏡像效果
        image = cv2.flip(image, 1)

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # 在右上角顯示分數
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, f'Score: {score}', (0, 30), font, 1, (0, 0, 0), 3, cv2.LINE_AA)
        # 在右上角顯示倒數計時
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, f'Time left: {timer_count}', (image.shape[1] - 210, 30), font, 1, (0, 0, 0), 3, cv2.LINE_AA)
        
        cv2.circle(image, circle_position, circle_radius, circle_color, -1)
        # 每 3 秒換一次圖片位置
        if time.time() - last_change_time > 3:
            last_change_time = time.time()
            circle_position = (random.randint(0, image.shape[1] - 2 * circle_radius),
                               image.shape[0] - circle_radius)
            
         # 繪製圖片
        if image_to_overlay is not None:
            # 計算圖片的位置
            img_y, img_x = circle_position[1] - 50, circle_position[0] - 50
            # 確保圖片不會超出畫面邊界
            img_y = max(0, min(img_y, image.shape[0] - 100))
            img_x = max(0, min(img_x, image.shape[1] - 100))
            
            # 將圖片蓋在畫面上
            image[img_y:img_y+100, img_x:img_x+100] = image_to_overlay

        if results.multi_hand_landmarks:
            for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
                x = int(hand_landmarks.landmark[9].x * image.shape[1])
                y = int(hand_landmarks.landmark[9].y * image.shape[0])
                cv2.circle(image, (x, y), 5, (0, 0, 255), -1)

                # 檢查是否達到一定高度
                touch_start_time = 0
                if y < circle_position[1] + circle_radius*3:
                    touch_start_time = time.time()
                # 檢查是否確實打到地鼠
                if (y < circle_position[1] + circle_radius and y > circle_position[1] - circle_radius) and (x > circle_position[0] - circle_radius and x < circle_position[0] + circle_radius):
                    if touch_start_time:
                        touch_time = time.time() - touch_start_time
                        if touch_time < 1:
                            score += 1
                            print(f"得分 +1，總分：{score}")
                            circle_position = (random.randint(0, image.shape[1] - 2 * circle_radius),
                                            image.shape[0] - circle_radius)
                            touch_start_time = 0

        # 顯示遊戲畫面
        cv2.imshow('Whack-a-Mole Game', image)

        # 檢查遊戲時間
        if timer_count == 0:
            print("遊戲結束，總分：", score)
                
            break

        # 按下Esc鍵結束遊戲
        if cv2.waitKey(1) == 27:
            timer_count = 0
            break

# 釋放資源
cap.release()
cv2.destroyAllWindows()

# ------------------------------
# 分數頁面
# ------------------------------
pygame.init()

end_window = pygame.display.set_mode((800, 600))
background_img = pygame.image.load("score_bg.png")
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