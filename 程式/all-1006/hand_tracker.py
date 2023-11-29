import cv2
import mediapipe as mp
import numpy as np
import cvzone
import time
import subprocess
import sys

# -----------------------------------------
# 跳轉程式
# -----------------------------------------

# 初始化 MediaPipe Hand 模型
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# 打開攝像頭
cap = cv2.VideoCapture(0)

# 設定初始視窗大小
initial_width, initial_height = 800, 600
cv2.namedWindow('Hand Tracking', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Hand Tracking', initial_width, initial_height)

# 載入要顯示的圖片
image_path1 = 'game_png/Rat-1.png'  
image_path2 = 'game_png/baseball.png'  
image_path3 = 'game_png/cat_1.png'  
image1 = cv2.imread(image_path1, -1)  # -1 可以讀取包含透明通道的圖片
image2 = cv2.imread(image_path2, -1)  
image3 = cv2.imread(image_path3, -1)  
# 載入通知
image_path4 = 'game_png/text-1.png' 
image4 = cv2.imread(image_path4, -1)
image_path5 = 'game_png/text-2.png' 
image5 = cv2.imread(image_path5, -1) 
image_path6 = 'game_png/text-3.png'  
image6 = cv2.imread(image_path6, -1) 

# 開始計時
start_time = None

while cap.isOpened():
    # 讀取一幀圖像
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break

    # 將圖像水平翻轉
    frame_flipped = cv2.flip(frame, 1)

    # 將翻轉後的圖像轉換為 RGB 格式
    frame_rgb = cv2.cvtColor(frame_flipped, cv2.COLOR_BGR2RGB)

    # 進行手部檢測
    results = hands.process(frame_rgb)

    # 判斷手的位置
    hand_position = 0

    if results.multi_hand_landmarks:
        landmarks = results.multi_hand_landmarks[0].landmark
        hand_x = landmarks[0].x  # 假設使用第一個手的第一個關節位置來判斷手的位置

        # 判斷手的位置
        if hand_x < 0.33:
            hand_position = 1
            image_to_display = image1  # 圖片1
            #-----------------------------------------
            image_resized_4 = cv2.resize(image4, (640, 100))  # 調整圖片大小

            # 設置第四張圖片在相機捕獲的視訊幀的位置（放在底部中心）
            bottom_left = (0, 380)
            bottom_right = (bottom_left[0] + image_resized_4.shape[1], bottom_left[1] + image_resized_4.shape[0])

            # 將第四張圖片放入相機捕獲的視訊幀中（考慮圖片的透明度）
            overlay_4 = frame_flipped.copy()
            overlay_4[bottom_left[1]:bottom_right[1], bottom_left[0]:bottom_right[0]] = image_resized_4

            alpha = 1  # 圖片透明度
            cv2.addWeighted(overlay_4, alpha, frame_flipped, 1 - alpha, 0, frame_flipped)
            #-----------------------------------------
            # 如果 start_time 是 None，則啟動計時器
            if start_time is None:
                start_time = time.time()

            # 超過五秒 觸發跳轉
            if time.time() - start_time > 5:

                result_from_get_account = sys.argv[1]
                result_list = result_from_get_account.strip('[()]').split(', ')

                # 並關閉所有視窗
                cap.release()
                cv2.destroyAllWindows()
                
                # 執行另一個 Python 檔案
                subprocess.run(["python", "whack-a-mole.py", str(result_list)])
                #subprocess.run(["python", "whack-a-mole.py"])
            #-----------------------------------------

        elif hand_x > 0.67:
            hand_position = 3
            image_to_display = image3  # 圖片3
            #-----------------------------------------
            image_resized_6 = cv2.resize(image6, (640, 100))  # 圖片大小

            # 設置第四張圖片在相機捕獲的視訊幀的位置（放在底部中心）
            bottom_left = (0, 380)
            bottom_right = (bottom_left[0] + image_resized_6.shape[1], bottom_left[1] + image_resized_6.shape[0])

            # 將第四張圖片放入相機捕獲的視訊幀中（考慮圖片的透明度）
            overlay_6 = frame_flipped.copy()
            overlay_6[bottom_left[1]:bottom_right[1], bottom_left[0]:bottom_right[0]] = image_resized_6

            alpha = 1  # 圖片透明度
            cv2.addWeighted(overlay_6, alpha, frame_flipped, 1 - alpha, 0, frame_flipped)
            #-----------------------------------------
            # 如果 start_time 是 None，則啟動計時器
            if start_time is None:
                start_time = time.time()

            # 超過五秒 觸發跳轉
            if time.time() - start_time > 5:
                result_from_get_account = sys.argv[1]
                result_list = result_from_get_account.strip('[()]').split(', ')
                # 並關閉所有視窗
                cap.release()
                cv2.destroyAllWindows()

                # 執行另一個 Python 檔案
                subprocess.run(["python", "run.py", str(result_list)])
                #subprocess.run(["python", "run.py"])
            #-----------------------------------------
        else:
            hand_position = 2
            image_to_display = image2  # 位置2對應圖片2
            #-----------------------------------------
            image_resized_5 = cv2.resize(image5, (640, 100))  # 調整圖片大小

            # 設置第四張圖片在相機捕獲的視訊幀的位置（放在底部中心）
            bottom_left = (0, 380)
            bottom_right = (bottom_left[0] + image_resized_5.shape[1], bottom_left[1] + image_resized_5.shape[0])

            # 將第四張圖片放入相機捕獲的視訊幀中（考慮圖片的透明度）
            overlay_5 = frame_flipped.copy()
            overlay_5[bottom_left[1]:bottom_right[1], bottom_left[0]:bottom_right[0]] = image_resized_5

            alpha = 1  # 圖片透明度
            cv2.addWeighted(overlay_5, alpha, frame_flipped, 1 - alpha, 0, frame_flipped)
            #-----------------------------------------
            # 如果 start_time 是 None，則啟動計時器
            if start_time is None:
                start_time = time.time()

            # 超過五秒 觸發跳轉
            if time.time() - start_time > 5:
                result_from_get_account = sys.argv[1]
                result_list = result_from_get_account.strip('[()]').split(', ')
                # result_list = [item.strip("'") for item in result_list]
                print(result_list)
                # 並關閉所有視窗
                cap.release()
                cv2.destroyAllWindows()

                # 執行另一個 Python 檔案
                subprocess.run(["python", "Pose.py", str(result_list)])
                #subprocess.run(["python", "Pose.py"])

            else:
                # 手不被偵測到時，重置計時器
                start_time = None
            #-----------------------------------------


        # 調整圖片大小以符合視訊畫面
        image_resized = cv2.resize(image_to_display, (100, 100))  # 調整圖片大小

        # 設置圖片在相機捕獲的視訊幀的位置
        top_left = ((hand_position - 1) * 250 + (100 - image_resized.shape[1]) // 2, 0)
        bottom_right = (top_left[0] + image_resized.shape[1], top_left[1] + image_resized.shape[0])  # 計算圖片右下角位置

        # 將圖片放入相機捕獲的視訊幀中（考慮圖片的透明度）
        # if image_resized.shape[2] == 3:
        #     alpha_channel = np.ones((image_resized.shape[0], image_resized.shape[1]), dtype=image_resized.dtype) * 255
        #     image_resized = cv2.merge((image_resized, alpha_channel))
        # overlay = frame_flipped.copy()
        # overlay[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = image_resized
        # frame_flipped = cvzone.overlayPNG(frame_flipped, image_resized, (top_left, bottom_right))
        # 设置图像在相机捕获的视频帧的位置（考虑图像的透明度）
        alpha_channel = image_resized[:, :, 3] / 255.0  # 提取透明通道并归一化
        overlay = image_resized[:, :, :3]  # 提取RGB通道

        # 设置图像位置
        roi = frame_flipped[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

        # 将图像叠加到视频帧上
        for c in range(3):
            roi[:, :, c] = (1 - alpha_channel) * roi[:, :, c] + alpha_channel * overlay[:, :, c]
        
        alpha = 1  # 圖片透明度
        # cv2.addWeighted(overlay, alpha, frame_flipped, 1 - alpha, 0, frame_flipped)

    # 在畫面上顯示手的位置
    # cv2.putText(frame_flipped, str(hand_position), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 在視窗中畫兩條直線
    line1_start, line1_end = (initial_width // 4, 0), (initial_width // 4, initial_height - 220)
    line2_start, line2_end = (2 * initial_width // 3 - 100, 0), (2 * initial_width // 3 - 100, initial_height - 220)
    cv2.line(frame_flipped, line1_start, line1_end, (255, 255, 255), 1)
    cv2.line(frame_flipped, line2_start, line2_end, (255, 255, 255), 1)

    # 顯示結果
    cv2.imshow('Hand Tracking', frame_flipped)

    # 按 'ESC' 鍵退出循環
    if cv2.waitKey(1) & 0xFF == 27:
        # 並關閉所有視窗(失敗)
        cap.release()
        cv2.destroyAllWindows()                
        # 執行另一個 Python 檔案
        subprocess.run(["python", "AR_home.py"])

# 釋放攝像頭並關閉所有窗口
cap.release()
cv2.destroyAllWindows()
