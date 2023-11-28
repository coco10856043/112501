import cv2

# 初始化相機
cap = cv2.VideoCapture(0)

# 讀取要放置的圖片
image_path = 'icon-1.png'  # 替換成你的圖像路徑
image = cv2.imread(image_path, -1)  # 使用 -1 可以讀取包含透明通道的圖片

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # 調整圖片大小以符合視訊畫面
    image_resized = cv2.resize(image, (100, 100))  # 調整圖片大小

    # 設置圖片在相機捕獲的視訊幀的位置
    top_left = (50, 50)  # 圖片在視訊畫面中的左上角位置
    bottom_right = (top_left[0] + image_resized.shape[1], top_left[1] + image_resized.shape[0])  # 計算圖片右下角位置

    # 將圖片放入相機捕獲的視訊幀中（考慮圖片的透明度）
    overlay = frame.copy()
    overlay[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = image_resized
    alpha = 0.5  # 圖片透明度
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

    # 顯示相機捕獲的視訊
    cv2.imshow("Camera", frame)

    # 按下 'q' 鍵退出迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放資源並關閉視窗
cap.release()
cv2.destroyAllWindows()
