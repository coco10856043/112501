import cv2
import numpy as np
import threading

# 建立攝像頭對象
cap = cv2.VideoCapture(0)

def start_timer():
    # 在這裡放置計時器的相關邏輯
    pass

def show_final_screen():
    # 設定畫面大小和顏色
    final_screen = np.zeros((300, 500, 3), np.uint8)
    final_screen[:] = (0, 255, 255)

    # 在畫面上顯示文字
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(final_screen, "Time's up!", (140, 100), font, 2, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(final_screen, "Play again", (60, 200), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(final_screen, "Exit", (330, 200), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

    while cap.isOpened():
        # 讀取攝像頭畫面
        success, image = cap.read()
        if not success:
            # 顯示錯誤視窗
            cv2.imshow('Error', np.zeros((100, 300, 3), np.uint8))
            cv2.putText(np.zeros((100, 300, 3), np.uint8), "Error: Camera not available", (10, 50), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

            # 加入確認按鈕
            cv2.putText(np.zeros((100, 300, 3), np.uint8), "Press 'R' to Retry", (10, 80), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imshow('Error', np.zeros((100, 300, 3), np.uint8))
            
            key = cv2.waitKey(0)
            
            if key == ord('r'):
                cv2.destroyWindow('Error')
                break
            else:
                cv2.destroyAllWindows()
                return

        # 顯示攝像頭畫面
        cv2.imshow('Camera', image)

    # 顯示結束畫面
    while True:
        cv2.imshow('Final Screen', final_screen)
        key = cv2.waitKey(0)

        # 如果按下 'p' 鍵，重新開始遊戲
        if key == ord('p'):
            threading.Thread(target=start_timer).start()
            break

        # 如果按下 'q' 鍵，離開程式
        elif key == ord('q'):
            # 檢查視窗是否被關閉
            if cv2.getWindowProperty('Final Screen', cv2.WND_PROP_VISIBLE) >= 1:
                cap.release()
                cv2.destroyAllWindows()
            break

# 執行顯示結束畫面的函數
show_final_screen()
