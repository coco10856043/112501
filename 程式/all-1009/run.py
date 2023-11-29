import cv2
import mediapipe as mp
import pygame
import random
import time
import subprocess
import sys, mysql.connector

# ------------------------------
# 按Esc退出遊戲 (X)
# ------------------------------
pygame.init()


result_from_get_account = sys.argv[1]
result_list = result_from_get_account.strip('[()]').split(', ')
result_list = [item.strip("'") for item in result_list]
print(result_list)
# 初始化 MediaPipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# 打开摄像头
cap = cv2.VideoCapture(0)

# 設定視窗大小
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Running")

#抓前一畫面資料
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

# 載入遊戲圖片
player_img = pygame.image.load("player.png")
player_width, player_height = 50, 50
player_x, player_y = WINDOW_WIDTH // 2, WINDOW_HEIGHT - player_height - 10

obstacle_speed = 5
score = 0
detect_counter = 0  # 控制頭部偵測的頻率

# ------------------------------
# 載入掉落物
# ------------------------------
obstacle_images = [pygame.image.load("cat_1.png")]

# 初始化障礙物
obstacle_width, obstacle_height = 70, 70
obstacle_x, obstacle_y = random.randint(0, WINDOW_WIDTH - obstacle_width), -50
obstacle_img = random.choice(obstacle_images)

clock = pygame.time.Clock()

# 遊戲
running = True
while running:

    # 读取一帧图像
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break

    # 鏡頭水平翻转
    frame_flipped = cv2.flip(frame, 1)

    # 圖像轉換成RBG格式
    frame_rgb = cv2.cvtColor(frame_flipped, cv2.COLOR_BGR2RGB)

    # 臉部偵測
    results = face_mesh.process(frame_rgb)

    # 判斷面部的左右偏轉
    if results.multi_face_landmarks:
        face_landmarks = results.multi_face_landmarks[0]

        # 左右眼的相對位置
        left_eye = (face_landmarks.landmark[33].x * frame_flipped.shape[1],
                    face_landmarks.landmark[33].y * frame_flipped.shape[0])
        right_eye = (face_landmarks.landmark[263].x * frame_flipped.shape[1],
                     face_landmarks.landmark[263].y * frame_flipped.shape[0])

        # 計算中央點
        mid_point = ((left_eye[0] + right_eye[0]) // 2, (left_eye[1] + right_eye[1]) // 2)

        # 比較中央點的水平位置
        if mid_point[0] > frame_flipped.shape[1] // 2:
            # 頭部右偏
            keys = pygame.key.get_pressed()
            if player_x < WINDOW_WIDTH - player_width:
                player_x += 10
        else:
            # 頭部左偏
            keys = pygame.key.get_pressed()
            if player_x > 0:
                player_x -= 10

    # 移動障礙物
    obstacle_y += obstacle_speed
    if obstacle_y > WINDOW_HEIGHT:
        obstacle_x = random.randint(0, WINDOW_WIDTH - obstacle_width)
        obstacle_y = -obstacle_height
        obstacle_img = random.choice(obstacle_images)  # 選擇障礙物
        score += 1
        obstacle_speed += 1

    # 使用矩形碰撞偵測
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

    if player_rect.colliderect(obstacle_rect):
        if obstacle_img.get_height() == 100:  # 高度
            # 碰撞之後改變圖示
            obstacle_img = pygame.image.load("cat_2.png")

        print("Game Over!")
        print("Score:", score)

        running = False

    # 顯示相機畫面
    frame = cv2.rotate(frame_flipped, cv2.ROTATE_90_COUNTERCLOCKWISE)  # 將畫面順時針旋轉90度
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = pygame.surfarray.make_surface(frame)
    frame = pygame.transform.scale(frame, (WINDOW_WIDTH, WINDOW_HEIGHT))  # 調整相機畫面大小以符合視窗大小
    win.blit(frame, (0, 0))

    # 繪製遊戲物件
    win.blit(player_img, (player_x, player_y))
    win.blit(obstacle_img, (obstacle_x, obstacle_y))

    pygame.display.update()
    clock.tick(60)  # 設定幀數

# 關閉相機
cap.release()
pygame.quit()

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

# 創建一個游標物件
initface_cursor1= conn.cursor()
query = "INSERT INTO game (`user_id`, `game_type`, `game_time`, `scores`) VALUES (%s, '3', current_time, %s);"
values = (result_list[0], score)
# 執行查詢
initface_cursor1.execute(query, values)
conn.commit()

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
