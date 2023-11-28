import cv2
import mediapipe as mp
import pygame
import random
import time

pygame.init()

# 初始化 MediaPipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# 打开摄像头
cap = cv2.VideoCapture(0)

# 設定視窗大小
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Running")

# 載入遊戲圖片
player_img = pygame.image.load("running/player.png")
player_width, player_height = 50, 50
player_x, player_y = WINDOW_WIDTH // 2, WINDOW_HEIGHT - player_height - 10

obstacle_speed = 2.5
score = 0
detect_counter = 0  # 控制頭部偵測的頻率

# 載入三種不同的隨機掉落物
obstacle_images = [pygame.image.load("running/cat_1.png")]

# 初始化障礙物
obstacle_width, obstacle_height = 70, 70
obstacle_x, obstacle_y = random.randint(0, WINDOW_WIDTH - obstacle_width), -50
obstacle_img = random.choice(obstacle_images)

# 背景圖片
background_img = pygame.image.load("running/background.png")

clock = pygame.time.Clock()

# 遊戲主迴圈
running = True
while running:

    # 設定背景顏色
    win.fill((255, 255, 255))

    # 繪製背景
    win.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 頭部偵測
    if detect_counter == 0:
        # 读取一帧图像
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        # 将图像水平翻转
        frame_flipped = cv2.flip(frame, 1)

        # 将图像转换为 RGB 格式
        frame_rgb = cv2.cvtColor(frame_flipped, cv2.COLOR_BGR2RGB)

        # 进行面部检测
        results = face_mesh.process(frame_rgb)

        # 判斷面部的左右偏轉
        if results.multi_face_landmarks:
            face_landmarks = results.multi_face_landmarks[0]

            # 获取左右眼的相對位置
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
                    player_x += 20
            else:
                # 頭部左偏
                keys = pygame.key.get_pressed()
                if player_x > 0:
                    player_x -= 20

        detect_counter = 5  # 設置為一個偵測周期後再次進行偵測
    else:
        detect_counter -= 1

    # 移動障礙物
    obstacle_y += obstacle_speed
    if obstacle_y > WINDOW_HEIGHT:
        obstacle_x = random.randint(0, WINDOW_WIDTH - obstacle_width)
        obstacle_y = -obstacle_height
        obstacle_img = random.choice(obstacle_images)  # 隨機選擇一種障礙物
        score += 1
        obstacle_speed += 0.25

    # 使用矩形碰撞偵測
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

    if player_rect.colliderect(obstacle_rect):
        if obstacle_img.get_height() == 68:
            obstacle_img = pygame.image.load("running/ghost_2.png")

        if obstacle_img.get_height() == 86:
            obstacle_img = pygame.image.load("running/slime_2.png")
        
        if obstacle_img.get_height() == 96:
            obstacle_img = pygame.image.load("running/cat_2.png")

        print("Game Over!")
        print("Score:", score)
        
        running = False
        

    # 繪製遊戲物件
    win.blit(player_img, (player_x, player_y))
    win.blit(obstacle_img, (obstacle_x, obstacle_y))

    pygame.display.update()
    clock.tick(144)  # 設定幀數

# 释放摄像头并关闭所有窗口
cap.release()
pygame.quit()
