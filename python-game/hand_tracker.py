import cv2
import mediapipe as mp

# 初始化 MediaPipe Hand 模型
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# 打開攝像頭
cap = cv2.VideoCapture(0)

# 設定初始視窗大小
initial_width, initial_height = 800, 600
cv2.namedWindow('Hand Tracking', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Hand Tracking', initial_width, initial_height)

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

    # 初始化手部位置
    hand_position = 0  # 0表示未檢測到手部

    # 判斷手的位置
    if results.multi_hand_landmarks:
        landmarks = results.multi_hand_landmarks[0].landmark
        hand_x = landmarks[0].x  # 這裡假設使用第一個手的第一個關節位置來判斷手的位置

        if hand_x < 0.33:
            hand_position = 1
        elif hand_x > 0.67:
            hand_position = 3
        else:
            hand_position = 2

    # 在視窗中畫兩條直線
    line1_start, line1_end = (initial_width // 4, 0), (initial_width // 4, initial_height)
    line2_start, line2_end = (2 * initial_width // 3 - 100, 0), (2 * initial_width // 3 - 100, initial_height)
    cv2.line(frame_flipped, line1_start, line1_end, (255, 0, 0), 2)
    cv2.line(frame_flipped, line2_start, line2_end, (255, 0, 0), 2)

    # 在畫面上顯示手的位置
    cv2.putText(frame_flipped, str(hand_position), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 顯示結果
    cv2.imshow('Hand Tracking', frame_flipped)

    # 按 'q' 鍵退出循環
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放攝像頭並關閉所有窗口
cap.release()
cv2.destroyAllWindows()
