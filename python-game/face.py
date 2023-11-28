import cv2
import mediapipe as mp

# 初始化 MediaPipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# 打开摄像头
cap = cv2.VideoCapture(0)

while cap.isOpened():
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
            direction = "Right"
        else:
            direction = "Left"

        # 在图像上显示方向
        cv2.putText(frame_flipped, f"Head Direction: {direction}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 显示结果
    cv2.imshow('Head Direction Detection', frame_flipped)

    # 按 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头并关闭所有窗口
cap.release()
cv2.destroyAllWindows()
