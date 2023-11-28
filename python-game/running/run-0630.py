import cv2
import mediapipe as mp
import pygame
import random

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

obstacle_img = pygame.image.load("running/obstacle.png")
obstacle_width, obstacle_height = 100, 100
obstacle_x, obstacle_y = random.randint(0, WINDOW_WIDTH - obstacle_width), -50
obstacle_speed = 2.5

# 背景圖片
background_img = pygame.image.load("running/background.png")

clock = pygame.time.Clock()