from tkinter import *
import cv2
from PIL import Image, ImageTk
import os
import matplotlib.pyplot as plt
import sys, mysql.connector
import subprocess

class basedesk():
    def __init__(self, master):
        self.rot = master
        self.rot.title('AR SPORTS WORLD')
        self.rot.geometry('1200x700+150+50')
        self.rot.resizable(False, False)

        self.initface = initface(self.rot)

class initface():
    def __init__(self, master):
        self.master = master

        result_from_get_account = sys.argv[1]
        result_list = result_from_get_account.strip('[()]').split(', ')
        result_list = [item.strip("'") for item in result_list]

        # 資料庫連線參數
        self.db_config = {
            'host': '140.131.114.140',  # 修改成你的 MySQL 伺服器 IP
            'port': 3306,         # 修改成你的 MySQL 伺服器 Port
            'user': '112501',        # 修改成你的 MySQL 使用者帳號
            'password': 'SportsWorld_112501',    # 修改成你的 MySQL 使用者密碼
            'database': '112-112501',  # 修改成你的資料庫名稱
        }

        # 連接到資料庫
        self.conn = mysql.connector.connect(**self.db_config)

        # 創建一個游標物件
        self.initface_cursor= self.conn.cursor()
        self.initface_cursor1= self.conn.cursor()
        self.initface_cursor2= self.conn.cursor()
        self.initface_cursor3= self.conn.cursor()
        self.initface_cursor4= self.conn.cursor()

        # 在這裡執行資料庫查詢
        query = "select user_name, avatar from daily_score as dc, user_information as ui where dc.user = ui.id order by score desc limit 5;"

        # 執行查詢
        self.initface_cursor.execute(query)

        # 獲取查詢結果
        result1 = self.initface_cursor.fetchall()
        print(result1)

        self.surface = PhotoImage(file="png/home.png")
        bg = Canvas(master, width=1200, height=700)
        bg.create_image(0, 0, anchor=NW, image=self.surface)
        
        bg.create_text(750,240,text=result1[0][0],font=('微軟正黑體',30,'bold'),fill='white')
        bg.create_text(750,305,text=result1[1][0],font=('微軟正黑體',30,'bold'),fill='white')
        bg.create_text(750,375,text=result1[2][0],font=('微軟正黑體',30,'bold'),fill='white')
        bg.create_text(750,445,text=result1[3][0],font=('微軟正黑體',30,'bold'),fill='white')
        bg.create_text(750,520,text=result1[4][0],font=('微軟正黑體',30,'bold'),fill='white')

        bg.place(x=0, y=0)

        self.initface = Frame(master)
        self.initface.place(x=0, y=0)

        self.had1 = PhotoImage(file="png/icon-1_40.png")
        self.had2 = PhotoImage(file="png/icon-2_40.png")
        self.had3 = PhotoImage(file="png/icon-3_40.png")

        if result1[0][1] == 1: self.av1 = self.had1
        elif result1[0][1] == 2: self.av1 = self.had2
        else: self.av1 = self.had3

        if result1[1][1] == 1: self.av2 = self.had1
        elif result1[1][1] == 2: self.av2 = self.had2
        else: self.av2 = self.had3

        if result1[2][1] == 1: self.av3 = self.had1
        elif result1[2][1] == 2: self.av3 = self.had2
        else: self.av3 = self.had3

        if result1[3][1] == 1: self.av4 = self.had1
        elif result1[3][1] == 2: self.av4 = self.had2
        else: self.av4 = self.had3

        if result1[4][1] == 1: self.av5 = self.had1
        elif result1[4][1] == 2: self.av5 = self.had2
        else: self.av5 = self.had3

        # 排行榜入榜頭像(這邊需要40*40版的頭像)
        r_had1 = Canvas()
        r_had1.create_image(0, 0, anchor=NW, image=self.av1)
        r_had1.place(x=620, y=220, width=40, height=40)
        r_had2 = Canvas()
        r_had2.create_image(0, 0, anchor=NW, image=self.av2)
        r_had2.place(x=620, y=285, width=40, height=40)
        r_had3 = Canvas()
        r_had3.create_image(0, 0, anchor=NW, image=self.av3)
        r_had3.place(x=620, y=355, width=40, height=40)
        r_had4 = Canvas()
        r_had4.create_image(0, 0, anchor=NW, image=self.av4)
        r_had4.place(x=620, y=425, width=40, height=40)
        r_had5 = Canvas()
        r_had5.create_image(0, 0, anchor=NW, image=self.av5)
        r_had5.place(x=620, y=495, width=40, height=40)

        self.had1 = PhotoImage(file="png/icon-1.png")
        self.had2 = PhotoImage(file="png/icon-2.png")
        self.had3 = PhotoImage(file="png/icon-3.png")
        
        if result_list[9] == '1':
            self.picture = self.had1
        elif result_list[9] == '2':
            self.picture = self.had2
        else:
            self.picture = self.had3
        user_had = Canvas()
        user_had.create_image(0, 0, anchor=NW, image=self.picture)
        user_had.place(x=10, y=10, width=100, height=100)
        user_name = Label(text=result_list[1], font=('Arial', 20), bg='black', fg='white')
        user_name.place(x=120, y=40)


        # 商店按鈕
        self.shop_btn = PhotoImage(file="png/shop.png")
        shop = Button(text='Shop', command=self.shopping)
        shop.config(image=self.shop_btn)
        shop.place(x=1096, y=129, width=72, height=72)

        # 設定按鈕
        self.setting_btn = PhotoImage(file="png/setting.png")
        setting = Button(text='Settings', command=self.change)
        setting.config(image=self.setting_btn)
        setting.place(x=1096, y=39, width=72, height=72)
        
        # PLAY按鈕
        self.play_btn = PhotoImage(file="png/PLAY.png")
        play = Button(image=self.play_btn, command=self.PLAY)
        play.place(x=840, y=570, width=350, height=100)

        # 圖表部分  https://medium.com/@yuhsuan_chou/python-%E5%9F%BA%E7%A4%8E%E8%B3%87%E6%96%99%E8%A6%96%E8%A6%BA%E5%8C%96-matplotlib-401da7d14e04
        def show_chart():
            query = "SELECT age_ranges.age_range, COALESCE(SUM(sa.score), 0) AS total_score FROM ( SELECT '0-20' AS age_range UNION SELECT '21-40' UNION SELECT '41-60' UNION SELECT '61-80' UNION SELECT 'Other' ) AS age_ranges LEFT JOIN (select * from daily_score as ds, user_age as ua where ds.user = ua.id) as sa ON age_ranges.age_range = CASE WHEN sa.age BETWEEN 0 AND 20 THEN '0-20' WHEN sa.age BETWEEN 21 AND 40 THEN '21-40' WHEN sa.age BETWEEN 41 AND 60 THEN '41-60' WHEN sa.age BETWEEN 61 AND 80 THEN '61-80' ELSE 'Other' END GROUP BY age_ranges.age_range ORDER BY age_ranges.age_range;"
            self.initface_cursor.execute(query)
            result = self.initface_cursor.fetchall()

            # 提取資料
            age_ranges, total_scores = zip(*result)

            # 繪製條形圖
            plt.bar(age_ranges, total_scores, width=0.5, align='center', color=['lightsteelblue', 'cornflowerblue', 'royalblue', 'midnightblue', 'navy', 'darkblue', 'mediumblue'])

            # 設置x軸標籤旋轉
            plt.xticks(rotation='vertical')

            # 添加標題
            plt.title("Total Score by Age Range Today", fontsize=16, fontweight='bold')

            # 顯示圖表
            plt.show()

        # 圖表顯示鈕(缺底圖)
        self.chart_btn = PhotoImage(file="png/chart.png")
        show_chart = Button(image=self.chart_btn, command=show_chart)
        show_chart.place(x=1096, y=222, width=72, height=72)

        # 在這裡執行資料庫查詢
        query1 = "select task1,t.* from daily_tasks as dt, task as t where dt.task1 = t.id and user = %s;"
        query2 = "select task2,t.* from daily_tasks as dt, task as t where dt.task2 = t.id and user = %s;"
        query3 = "select task3,t.* from daily_tasks as dt, task as t where dt.task3 = t.id and user = %s;"
        values = (result_list[0],)

        # 執行查詢並獲取查詢結果
        self.initface_cursor1.execute(query1,values)
        result2 = self.initface_cursor1.fetchall()

        self.initface_cursor2.execute(query2,values)
        result3 = self.initface_cursor2.fetchall()

        self.initface_cursor3.execute(query3,values)
        result4 = self.initface_cursor3.fetchall()
        
        a = '打地鼠'
        b = '無敵守門員'
        c = '當心天外來物'
        def test1():
            if result2[0][2] == 1: #遊戲分數
                if '在一局' in result2[0][3]:
                    # 玩打地鼠
                    if a in result2[0][3]:
                        query6 = "select * from game where user_id = %s and game_type = 2 and scores >= (select `values` from task where id = %s);"
                        values3 = (result_list[0],result2[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query6, values3)

                        # 獲取查詢結果
                        result8 = self.initface_cursor4.fetchall()

                    #玩無敵守門員
                    if b in result2[0][3]:
                        query6 = "select * from game where user_id = %s and game_type = 1 and scores >= (select `values` from task where id = %s);"
                        values3 = (result_list[0],result2[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query6, values3)

                        # 獲取查詢結果
                        result8 = self.initface_cursor4.fetchall()

                    #玩當心天外來物
                    if c in result2[0][3]:
                        query6 = "select * from game where user_id = %s and game_type = 3 and scores >= (select `values` from task where id = %s);"
                        values3 = (result_list[0],result2[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query6, values3)

                        # 獲取查詢結果
                        result8 = self.initface_cursor4.fetchall()

                if '累計' in result2[0][3]:
                    # 玩打地鼠
                    if a in result2[0][3]:
                        query6 = "select user_id, game_type, sum(scores) from game where user_id = %s and game_type = 2 and (select sum(scores) from game where  user_id = %s and game_type = 3 group by user_id, game_type) >= (select `values` from task where id = %s) group by user_id, game_type;"
                        values3 = (result_list[0],result_list[0],result2[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query6, values3)

                        # 獲取查詢結果
                        result8 = self.initface_cursor4.fetchall()
                    
                    # 玩無敵守門員
                    if b in result2[0][3]:
                        query6 = "select user_id, game_type, sum(scores) from game where user_id = %s and game_type = 1 and (select sum(scores) from game where  user_id = %s and game_type = 3 group by user_id, game_type) >= (select `values` from task where id = %s) group by user_id, game_type;"
                        values3 = (result_list[0],result_list[0],result2[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query6, values3)

                        # 獲取查詢結果
                        result8 = self.initface_cursor4.fetchall()

                    # 玩當心天外來物
                    if c in result2[0][3]:
                        query6 = "select user_id, game_type, sum(scores) from game where user_id = %s and game_type = 3 and (select sum(scores) from game where  user_id = %s and game_type = 3 group by user_id, game_type) >= (select `values` from task where id = %s) group by user_id, game_type;"
                        values3 = (result_list[0],result_list[0],result2[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query6, values3)

                        # 獲取查詢結果
                        result8 = self.initface_cursor4.fetchall()

            else: #遊戲時長
                query6 = "select user_id from game where user_id = %s and (select count(*) from game where  user_id = %s group by user_id) >= (select `values` from task where id = %s) group by user_id;"
                values3 = (result_list[0],result_list[0],result2[0][0])
                        
                # 執行查詢
                self.initface_cursor4.execute(query6, values3)

                # 獲取查詢結果
                result8 = self.initface_cursor4.fetchall()

            if not result8:
                task1.set(0)
            else:
                task1.set(1)

        def test2():
            if result3[0][2] == 1: #遊戲分數
                if '在一局' in result3[0][3]:
                    # 玩打地鼠
                    if a in result3[0][3]:
                        query5 = "select * from game where user_id = %s and game_type = 2 and scores >= (select `values` from task where id = %s);"
                        values2 = (result_list[0],result3[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query5, values2)

                        # 獲取查詢結果
                        result7 = self.initface_cursor4.fetchall()

                    #玩無敵守門員
                    if b in result3[0][3]:
                        query5 = "select * from game where user_id = %s and game_type = 1 and scores >= (select `values` from task where id = %s);"
                        values2 = (result_list[0],result3[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query5, values2)

                        # 獲取查詢結果
                        result7 = self.initface_cursor4.fetchall()

                    #玩當心天外來物
                    if c in result3[0][3]:
                        query5 = "select * from game where user_id = %s and game_type = 3 and scores >= (select `values` from task where id = %s);"
                        values2 = (result_list[0],result3[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query5, values2)

                        # 獲取查詢結果
                        result7 = self.initface_cursor4.fetchall()

                if '累計' in result3[0][3]:
                    # 玩打地鼠
                    if a in result3[0][3]:
                        query5 = "select user_id, game_type, sum(scores) from game where user_id = %s and game_type = 2 and (select sum(scores) from game where  user_id = %s and game_type = 3 group by user_id, game_type) >= (select `values` from task where id = %s) group by user_id, game_type;"
                        values2 = (result_list[0],result_list[0],result3[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query5, values2)

                        # 獲取查詢結果
                        result7 = self.initface_cursor4.fetchall()
                    
                    # 玩無敵守門員
                    if b in result3[0][3]:
                        query5 = "select user_id, game_type, sum(scores) from game where user_id = %s and game_type = 1 and (select sum(scores) from game where  user_id = %s and game_type = 3 group by user_id, game_type) >= (select `values` from task where id = %s) group by user_id, game_type;"
                        values2 = (result_list[0],result_list[0],result3[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query5, values2)

                        # 獲取查詢結果
                        result7 = self.initface_cursor4.fetchall()

                    # 玩當心天外來物
                    if c in result3[0][3]:
                        query5 = "select user_id, game_type, sum(scores) from game where user_id = %s and game_type = 3 and (select sum(scores) from game where  user_id = %s and game_type = 3 group by user_id, game_type) >= (select `values` from task where id = %s) group by user_id, game_type;"
                        values2 = (result_list[0],result_list[0],result3[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query5, values2)

                        # 獲取查詢結果
                        result7 = self.initface_cursor4.fetchall()

            else: #遊戲時長
                query5 = "select user_id from game where user_id = %s and (select count(*) from game where  user_id = %s group by user_id) >= (select `values` from task where id = %s) group by user_id;"
                values2 = (result_list[0],result_list[0],result3[0][0])
                        
                # 執行查詢
                self.initface_cursor4.execute(query5, values2)

                # 獲取查詢結果
                result7 = self.initface_cursor4.fetchall()

            if not result7:
                task2.set(0)
            else:
                task2.set(1)

        def test3():
            if result4[0][2] == 1: #遊戲分數
                if '在一局' in result4[0][3]:
                    # 玩打地鼠
                    if a in result4[0][3]:
                        query6 = "select * from game where user_id = %s and game_type = 2 and scores >= (select `values` from task where id = %s);"
                        values3 = (result_list[0],result4[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query6, values3)

                        # 獲取查詢結果
                        result8 = self.initface_cursor4.fetchall()

                    #玩無敵守門員
                    if b in result4[0][3]:
                        query6 = "select * from game where user_id = %s and game_type = 1 and scores >= (select `values` from task where id = %s);"
                        values3 = (result_list[0],result4[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query6, values3)

                        # 獲取查詢結果
                        result8 = self.initface_cursor4.fetchall()

                    #玩當心天外來物
                    if c in result4[0][3]:
                        query6 = "select * from game where user_id = %s and game_type = 3 and scores >= (select `values` from task where id = %s);"
                        values3 = (result_list[0],result4[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query6, values3)

                        # 獲取查詢結果
                        result8 = self.initface_cursor4.fetchall()

                if '累計' in result4[0][3]:
                    # 玩打地鼠
                    if a in result4[0][3]:
                        query6 = "select user_id, game_type, sum(scores) from game where user_id = %s and game_type = 2 and (select sum(scores) from game where  user_id = %s and game_type = 3 group by user_id, game_type) >= (select `values` from task where id = %s) group by user_id, game_type;"
                        values3 = (result_list[0],result_list[0],result4[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query6, values3)

                        # 獲取查詢結果
                        result8 = self.initface_cursor4.fetchall()
                    
                    # 玩無敵守門員
                    if b in result4[0][3]:
                        query6 = "select user_id, game_type, sum(scores) from game where user_id = %s and game_type = 1 and (select sum(scores) from game where  user_id = %s and game_type = 3 group by user_id, game_type) >= (select `values` from task where id = %s) group by user_id, game_type;"
                        values3 = (result_list[0],result_list[0],result4[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query6, values3)

                        # 獲取查詢結果
                        result8 = self.initface_cursor4.fetchall()

                    # 玩當心天外來物
                    if c in result4[0][3]:
                        query6 = "select user_id, game_type, sum(scores) from game where user_id = %s and game_type = 3 and (select sum(scores) from game where  user_id = %s and game_type = 3 group by user_id, game_type) >= (select `values` from task where id = %s) group by user_id, game_type;"
                        values3 = (result_list[0],result_list[0],result4[0][0])
                        
                        # 執行查詢
                        self.initface_cursor4.execute(query6, values3)

                        # 獲取查詢結果
                        result8 = self.initface_cursor4.fetchall()

            else: #遊戲時長
                query6 = "select user_id from game where user_id = %s and (select count(*) from game where  user_id = %s group by user_id) >= (select `values` from task where id = %s) group by user_id;"
                values3 = (result_list[0],result_list[0],result4[0][0])
                        
                # 執行查詢
                self.initface_cursor4.execute(query6, values3)

                # 獲取查詢結果
                result8 = self.initface_cursor4.fetchall()

            if not result8:
                task3.set(0)
            else:
                task3.set(1)

        # 任務內容
        task1 = BooleanVar() 
        task1.set(0)
        task2 = BooleanVar()
        task2.set(0)
        task3 = BooleanVar()
        task3.set(0)
        mycheckbutton1 = Checkbutton(text=result2[0][3], font=('Arial', 15), bg='cornflowerblue', var=task1, command=test1)
        mycheckbutton1.place(x=135, y=195)
        mycheckbutton2 = Checkbutton(text=result3[0][3], font=('Arial', 15), bg='cornflowerblue', var=task2, command=test2)
        mycheckbutton2.place(x=135, y=267)
        mycheckbutton3 = Checkbutton(text=result4[0][3], font=('Arial', 15), bg='cornflowerblue', var=task3, command=test3)
        mycheckbutton3.place(x=135, y=345)

        #小叮嚀
        query = "SELECT `context` FROM ding ORDER BY RAND() LIMIT 1;"
        self.initface_cursor1.execute(query)
        result = self.initface_cursor1.fetchall()
        original_text = str(result[0])
        # 移除原始文字中的括號
        original_text = original_text.replace("('", '').replace("',)", '')
        line_length = 30

        formatted_text = [original_text[i:i+line_length] for i in range(0, len(original_text), line_length)]
        # 將列表中的文字連接成帶有換行符號的字串
        formatted_text = "\n".join(formatted_text)

        tip = Label(text='Tips')
        tip.place(x=50, y=570)
        tip_con = Label(text=formatted_text)
        tip_con.place(x=50, y=600)

    # 商店跳轉
    def shopping(self,):       
        self.initface.destroy()
        face2(self.master)

    # 設定跳轉
    def change(self,):       
        self.initface.destroy()
        face1(self.master)
    # PLAY跳轉
    def PLAY(self,):       
        rot.destroy()
        # os.system('hand_tracker.py') 
        subprocess.run(["python", "hand_tracker.py"])
# 商店頁
class face2():
    def __init__(self,master):
        self.master = master
        self.face1 = Frame(self.master,)
        self.face1.pack()

        result_from_get_account = sys.argv[1]
        result_list = result_from_get_account.strip('[()]').split(', ')
        result_list = [item.strip("'") for item in result_list]

        # 資料庫連線參數
        self.db_config = {
            'host': '140.131.114.140',  # 修改成你的 MySQL 伺服器 IP
            'port': 3306,         # 修改成你的 MySQL 伺服器 Port
            'user': '112501',        # 修改成你的 MySQL 使用者帳號
            'password': 'SportsWorld_112501',    # 修改成你的 MySQL 使用者密碼
            'database': '112-112501',  # 修改成你的資料庫名稱
        }

        # 連接到資料庫
        self.conn = mysql.connector.connect(**self.db_config)

        # 底圖
        self.img2 = PhotoImage(file="png/buy_bg_2.png")
        bg = Canvas(width=1200, height=700)
        bg.create_image(0, 0, anchor=NW, image=self.img2)   # 在 Canvas 中放入圖片
        bg.place(x=0,y=0)

        # 商品圖
        self.shop_1 = PhotoImage(file="png/shop-1.png")
        self.shop_2 = PhotoImage(file="png/shop-2.png")
        self.shop_3 = PhotoImage(file="png/shop-3.png")
        pd1 = Canvas(width=260, height=260)
        pd1.create_image(0, 0,anchor=NW, image=self.shop_1)
        pd1.place(x=70,y=60)
        pd2 = Canvas(width=260, height=260)
        pd2.create_image(0, 0,anchor=NW, image=self.shop_2)
        pd2.place(x=470,y=60)
        pd3 = Canvas(width=260, height=260)
        pd3.create_image(0, 0,anchor=NW, image=self.shop_3)
        pd3.place(x=870,y=60)
        # 返回鈕
        self.goback = PhotoImage(file="png/back.png")
        register = Button(text="返回",command=self.back)
        register.config(image=self.goback)
        register.place(x=550,y=600,width=100,height=35)
        # 購買鈕

        def buys1():
            # 創建一個游標物件
            self.initface_cursor= self.conn.cursor()

            # 在這裡執行資料庫查詢
            query_1 = "SELECT * FROM scores where user = %s and score = 2000;"
            values_1 = (result_list[0],)
            # 執行查詢
            self.initface_cursor.execute(query_1, values_1)

            # 獲取查詢結果
            result = self.initface_cursor.fetchall()

            if result:
            
                query = "insert into user_have (user_id, game_type, `group`) SELECT (select id from user_information where id = %s) as user_id , gt.game_type, gt.`group` FROM game_pictures as gt where game_type = 3 and `group` <> 1;"
                values = (result_list[0],)

                # 執行查詢
                self.initface_cursor.execute(query, values)

                # 獲取查詢結果
                self.initface_cursor.fetchall()
                self.conn.commit()

                query = "update scores set score = score - 2000 where user = %s;"
                values = (result_list[0],)

                # 執行查詢
                self.initface_cursor.execute(query, values)

                # 獲取查詢結果
                self.initface_cursor.fetchall()
                self.conn.commit()

            else:
                print('無法購買')



        def buys2():
            # 創建一個游標物件
            self.initface_cursor= self.conn.cursor()

            # 在這裡執行資料庫查詢
            query_1 = "SELECT * FROM scores where user = %s and score = 2000;"
            values_1 = (result_list[0],)
            # 執行查詢
            self.initface_cursor.execute(query_1, values_1)

            # 獲取查詢結果
            result = self.initface_cursor.fetchall()

            if result:
                # 在這裡執行資料庫查詢
                query = "insert into user_have (user_id, game_type, `group`) SELECT (select id from user_information where id = %s) as user_id , gt.game_type, gt.`group` FROM game_pictures as gt where game_type = 2 and `group` <> 1;"
                values = (result_list[0],)

                # 執行查詢
                self.initface_cursor.execute(query, values)

                # 獲取查詢結果
                self.initface_cursor.fetchall()
                self.conn.commit()

                query = "update scores set score = score - 2000 where user = %s;"
                values = (result_list[0],)

                # 執行查詢
                self.initface_cursor.execute(query, values)

                # 獲取查詢結果
                self.initface_cursor.fetchall()
                self.conn.commit()

            else:
                print('無法購買')

        def buys3():
            # 創建一個游標物件
            self.initface_cursor= self.conn.cursor()

            # 在這裡執行資料庫查詢
            query_1 = "SELECT * FROM scores where user = %s and score = 2000;"
            values_1 = (result_list[0],)
            # 執行查詢
            self.initface_cursor.execute(query_1, values_1)

            # 獲取查詢結果
            result = self.initface_cursor.fetchall()

            if result:
                # 在這裡執行資料庫查詢
                query = "insert into user_have (user_id, game_type, `group`) SELECT (select id from user_information where id = %s) as user_id , gt.game_type, gt.`group` FROM game_pictures as gt where game_type = 1 and `group` <> 1;"
                values = (result_list[0],)
                
                # 執行查詢
                self.initface_cursor.execute(query, values)

                # 獲取查詢結果
                self.initface_cursor.fetchall()
                self.conn.commit()

                query = "update scores set score = score - 2000 where user = %s;"
                values = (result_list[0],)

                # 執行查詢
                self.initface_cursor.execute(query, values)

                # 獲取查詢結果
                self.initface_cursor.fetchall()
                self.conn.commit()

            else:
                print('無法購買')

        self.buy_img = PhotoImage(file="png/buy.png")
        buy1 = Button(text="購買", command=buys1)
        buy1.config(image=self.buy_img)
        buy1.place(x=70,y=485,width=260,height=35)
        buy2 = Button(text="購買", command=buys2)
        buy2.config(image=self.buy_img)
        buy2.place(x=470,y=485,width=260,height=35)
        buy3 = Button(text="購買", command=buys3)
        buy3.config(image=self.buy_img)
        buy3.place(x=870,y=485,width=260,height=35)

    # 反回主頁方法
    def back(self):
        self.face1.destroy()
        initface(self.master)
# 設定頁
class face1():
    def __init__(self,master):
        self.master = master
        self.face1 = Frame(self.master,)
        self.face1.pack()

        result_from_get_account = sys.argv[1]
        result_list = result_from_get_account.strip('[()]').split(', ')
        result_list = [item.strip("'") for item in result_list]
        print(result_list)
        # 資料庫連線參數
        self.db_config = {
            'host': '140.131.114.140',  # 修改成你的 MySQL 伺服器 IP
            'port': 3306,         # 修改成你的 MySQL 伺服器 Port
            'user': '112501',        # 修改成你的 MySQL 使用者帳號
            'password': 'SportsWorld_112501',    # 修改成你的 MySQL 使用者密碼
            'database': '112-112501',  # 修改成你的資料庫名稱
        }

        self.conn = mysql.connector.connect(**self.db_config)

        # 底圖
        self.img2 = PhotoImage(file="png/re_bg.png")
        bg = Canvas(width=1200, height=700)
        bg.create_image(0, 0,anchor=NW, image=self.img2)   # 在 Canvas 中放入圖片
        bg.create_text(440,365,text='身高',font=('華康粗黑體',18),fill='white')
        bg.create_text(635,365,text='體重',font=('華康粗黑體',18),fill='white')
        bg.create_text(440,415,text='暱稱',font=('華康粗黑體',18),fill='white')
        bg.create_text(440,465,text='密碼',font=('華康粗黑體',18),fill='white')
        bg.place(x=0,y=0)

        # !!!!!
        def updateset():
            set_value1 = heightvalue.get()
            set_value2 = weightvalue.get()
            set_value3 = namevalue.get()
            set_value4 = passwordvalue.get()
            set_value5 = self.avatar.get()
            set_value6 = self.game1.get()
            set_value7 = self.game2.get()
            set_value8 = self.game3.get()
            set_count = 0
            
            if not set_value5:
                set_value5 = 0
            if not set_value6:
                set_value6 = 0
            if not set_value7:
                set_value7 = 0
            if not set_value8:
                set_value8 = 0

            print(set_value1,set_value2,set_value3,set_value4,set_value5, set_value6, set_value7, set_value8, result_list[0])
            if ('請輸入' in set_value1) and ('請輸入' in set_value2) and ('請輸入' in set_value3) and ('請輸入' in set_value4) and (set_value5 == 0) and (set_value6 == 0) and (set_value7 == 0) and (set_value8 == 0):
                initface(self.master) 
            # 創建一個游標物件
            self.initface_cursor= self.conn.cursor()

            if '請輸入' not in set_value1:
                query1 = "UPDATE user_information SET height = %s WHERE (`id` = %s);"
                values = (float(set_value1), result_list[0])

                # 執行查詢
                self.initface_cursor.execute(query1, values)
                self.conn.commit()
                set_count += 1

            if '請輸入' not in set_value2:
                query2 = "UPDATE user_information SET weight = %s WHERE (`id` = %s);"
                values = (float(set_value2), result_list[0])

                # 執行查詢
                self.initface_cursor.execute(query2, values)
                self.conn.commit()
                set_count += 1

            if '請輸入' not in set_value3:
                query3 = "UPDATE user_information SET `user_name` = %s WHERE (`id` = %s);"
                values = (set_value3, result_list[0])

                # 執行查詢
                self.initface_cursor.execute(query3, values)
                self.conn.commit()
                set_count += 1

            if '請輸入' not in set_value4:
                query4 = "UPDATE user_information SET `password` = %s WHERE (`id` = %s);"
                values = (set_value4, result_list[0])

                # 執行查詢
                self.initface_cursor.execute(query4, values)
                self.conn.commit()
                set_count += 1  

            if set_value5 != 0:
                query5 = "UPDATE user_information SET `avatar` = %s WHERE (`id` = %s);"
                values = (set_value5, result_list[0])

                # 執行查詢
                self.initface_cursor.execute(query5, values)
                self.conn.commit()
                set_count += 1 

            if set_value6 != 0:
                query6 = "select * from user_have where user_id = %s and game_type = 1 and `group` = %s;"
                values = (result_list[0],set_value6)

                # 執行查詢
                self.initface_cursor.execute(query6, values)
                # 獲取查詢結果
                result = self.initface_cursor.fetchall()

                if result:
                    query7 = "UPDATE user_information SET `game1` = %s WHERE (`id` = %s);"
                    values = (int(set_value6), result_list[0])

                    # 執行查詢
                    self.initface_cursor.execute(query7, values)
                    self.conn.commit()
                    set_count += 1   
                else:
                    print('無法使用1')

            if set_value7 != 0:
                query8 = "select * from user_have where user_id = %s and game_type = 2 and `group` = %s;"
                values = (result_list[0],set_value7)

                # 執行查詢
                self.initface_cursor.execute(query8, values)
                # 獲取查詢結果
                result = self.initface_cursor.fetchall()

                if result:
                    query9 = "UPDATE user_information SET `game2` = %s WHERE (`id` = %s);"
                    values = (set_value7, result_list[0])

                    # 執行查詢
                    self.initface_cursor.execute(query9, values)
                    self.conn.commit()
                    set_count += 1  
                else:
                    print('無法使用2')

            if set_value8 != 0:
                query10 = "select * from user_have where user_id = %s and game_type = 2 and `group` = %s;"
                values = (result_list[0],set_value8)

                # 執行查詢
                self.initface_cursor.execute(query10, values)
                # 獲取查詢結果
                result = self.initface_cursor.fetchall()

                if result:
                    query11 = "UPDATE user_information SET `game3` = %s WHERE (`id` = %s);"
                    values = (set_value8, result_list[0])

                    # 執行查詢
                    self.initface_cursor.execute(query11, values)
                    self.conn.commit()
                    set_count += 1 

                else:
                    print('無法使用3')

            if set_count != 0:
                print('更新成功')
                initface(self.master) 

        def on_entry_click_h(event):
            if height_in.get() == '請輸入身高（公分）':
                height_in.delete(0, "end")  # 刪除現有文本
                height_in.insert(0, '')  # 插入一個空字符串，以便不顯示灰色文本
                height_in.config(fg='black')  # 將文本顏色設置為黑色

        def on_focus_out_h(event):
            if height_in.get() == '':
                height_in.insert(0, '請輸入身高（公分）')
                height_in.config(fg='grey')  # 將文本顏色設置為灰色

        heightvalue = StringVar()  # 新增一個StringVar變數
        height_in = Entry(rot, fg='grey', width=30, textvariable=heightvalue)
        height_in.insert(0, '請輸入身高（公分）')
        height_in.bind('<FocusIn>', on_entry_click_h)
        height_in.bind('<FocusOut>', on_focus_out_h)
        height_in.place(x=480,y=350,width=110,height=30)

        def on_entry_click_w(event):
            if weight_in.get() == '請輸入體重（公斤）':
                weight_in.delete(0, "end")  # 刪除現有文本
                weight_in.insert(0, '')  # 插入一個空字符串，以便不顯示灰色文本
                weight_in.config(fg='black')  # 將文本顏色設置為黑色

        def on_focus_out_w(event):
            if weight_in.get() == '':
                weight_in.insert(0, '請輸入體重（公斤）')
                weight_in.config(fg='grey')  # 將文本顏色設置為灰色

        weightvalue = StringVar()  # 新增一個StringVar變數
        weight_in = Entry(rot, fg='grey', width=30, textvariable=weightvalue)
        weight_in.insert(0, '請輸入體重（公斤）')
        weight_in.bind('<FocusIn>', on_entry_click_w)
        weight_in.bind('<FocusOut>', on_focus_out_w)
        weight_in.place(x=670,y=350,width=110,height=30)

        def on_entry_click_n(event):
            if name_in.get() == '請輸入暱稱':
                name_in.delete(0, "end")  # 刪除現有文本
                name_in.insert(0, '')  # 插入一個空字符串，以便不顯示灰色文本
                name_in.config(fg='black')  # 將文本顏色設置為黑色

        def on_focus_out_n(event):
            if name_in.get() == '':
                name_in.insert(0, '請輸入暱稱')
                name_in.config(fg='grey')  # 將文本顏色設置為灰色

        namevalue = StringVar()  # 新增一個StringVar變數
        name_in = Entry(rot, fg='grey', width=30, textvariable=namevalue)
        name_in.insert(0, '請輸入暱稱')
        name_in.bind('<FocusIn>', on_entry_click_n)
        name_in.bind('<FocusOut>', on_focus_out_n)
        name_in.place(x=480,y=400,width=300,height=30)

        def on_entry_click_p(event):
            if psw_in.get() == '請輸入密碼':
                psw_in.delete(0, "end")  # 刪除現有文本
                psw_in.insert(0, '')  # 插入一個空字符串，以便不顯示灰色文本
                psw_in.config(fg='black')  # 將文本顏色設置為黑色

        def on_focus_out_p(event):
            if psw_in.get() == '':
                psw_in.insert(0, '請輸入密碼')
                psw_in.config(fg='grey')  # 將文本顏色設置為灰色

        passwordvalue = StringVar()  # 新增一個StringVar變數
        psw_in = Entry(rot, fg='grey', width=30, textvariable=passwordvalue)
        psw_in.insert(0, '請輸入密碼')
        psw_in.bind('<FocusIn>', on_entry_click_p)
        psw_in.bind('<FocusOut>', on_focus_out_p)
        psw_in.place(x=480,y=450,width=300,height=30)

        self.save_img = PhotoImage(file="png/save.png")
        register = Button(text="儲存",command=updateset)
        register.config(image=self.save_img)
        register.place(x=480,y=550,width=100,height=35)

        self.log_out_img = PhotoImage(file="png/logout.png")
        log_out = Button(text="登出",command=self.log_out)
        log_out.config(font=15)
        log_out.place(x=620,y=550,width=100,height=35)

        self.had1 = PhotoImage(file="png/icon-1.png")
        self.had2 = PhotoImage(file="png/icon-2.png")
        self.had3 = PhotoImage(file="png/icon-3.png")
        self.game11 = PhotoImage(file="png/baseball.png")
        self.game12 = PhotoImage(file="png/basketball.png")
        self.game13 = PhotoImage(file="png/masterball.png")
        self.game21 = PhotoImage(file="png/Rat-1.png")
        self.game22 = PhotoImage(file="png/Ratt-1.png")
        self.game23 = PhotoImage(file="png/Rattt-1.png")
        self.game31 = PhotoImage(file="png/cat_1.png")
        self.game32 = PhotoImage(file="png/ghost_1.png")
        self.game33 = PhotoImage(file="png/slime_1.png")

        # !!!!!
        self.avatar = StringVar()  # 新增一個StringVar變數
        self.game1 = StringVar()  # 新增一個StringVar變數
        self.game2 = StringVar()  # 新增一個StringVar變數
        self.game3 = StringVar()  # 新增一個StringVar變數

        self.photo = Button(text="Create new window",command=self.createNewWindow)
        self.photo.place(x=550,y=100,width=100, height=100)

        self.g_photo1 = Button(text="choose game1 photo",command=self.g1_photo)
        self.g_photo1.place(x=430,y=220,width=100, height=100)
        self.g_photo2 = Button(text="choose game2 photo",command=self.g2_photo)
        self.g_photo2.place(x=550,y=220,width=100, height=100)
        self.g_photo3 = Button(text="choose game3 photo",command=self.g3_photo)
        self.g_photo3.place(x=670,y=220,width=100, height=100)
        
    def one(self):
        self.photo.config(image=self.had1)
        self.set_avatar(1)
    def two(self):
        self.photo.config(image=self.had2)
        self.set_avatar(2)
    def three(self):
        self.photo.config(image=self.had3)
        self.set_avatar(3)
    # def login_home(self,):
    #     self.initface.destroy()
    #     os.system('python AR_login_FINAL.py')
    #     rot.destroy()

    # !!!!!
    def set_avatar(self, value):
        self.avatar.set(value)
    def set_game1(self, value):
        self.game1.set(value)
    def set_game2(self, value):
        self.game2.set(value)
    def set_game3(self, value):
        self.game3.set(value)
    #頭像 
    def createNewWindow(self):
        choose_photo = Toplevel(self.face1)
        choose_photo.title = ('choose_photo')
        choose_photo.geometry("300x100+600+250")

        photo1 = Button(choose_photo,          # 按鈕所在視窗
                        image=self.had1,  # 顯示文字
                        command = self.one) # 按下按鈕所執行的函數
        photo2 = Button(choose_photo,          # 按鈕所在視窗
                        image=self.had2,  # 顯示文字
                        command = self.two) # 按下按鈕所執行的函數
        photo3 = Button(choose_photo,          # 按鈕所在視窗
                        image=self.had3,  # 顯示文字
                        command = self.three) # 按下按鈕所執行的函數

        # 頭像選擇按鈕
        photo1.place(x=0,y=0,width=100,height=100)
        photo2.place(x=100,y=0,width=100,height=100)
        photo3.place(x=200,y=0,width=100,height=100)

#遊戲一
    def g1_one(self):
        self.g_photo1.config(image=self.game11)
        self.set_game1(1)
    def g1_two(self):
        self.g_photo1.config(image=self.game12)
        self.set_game1(2)
    def g1_three(self):
        self.g_photo1.config(image=self.game13)
        self.set_game1(3)

    
    def g1_photo(self):
        choose_photog1 = Toplevel(self.face1)
        choose_photog1.title = ('choose_photo')
        choose_photog1.geometry("300x100+600+250")

        photo1 = Button(choose_photog1,          # 按鈕所在視窗
                        image=self.game11,  # 顯示文字
                        command = self.g1_one) # 按下按鈕所執行的函數
        photo2 = Button(choose_photog1,          # 按鈕所在視窗
                        image=self.game12,  # 顯示文字
                        command = self.g1_two) # 按下按鈕所執行的函數
        photo3 = Button(choose_photog1,          # 按鈕所在視窗
                        image=self.game13,  # 顯示文字
                        command = self.g1_three) # 按下按鈕所執行的函數

        # 頭像選擇按鈕
        photo1.place(x=0,y=0,width=100,height=100)
        photo2.place(x=100,y=0,width=100,height=100)
        photo3.place(x=200,y=0,width=100,height=100)

#遊戲二      
    def g2_one(self):
        self.g_photo2.config(image=self.game21)
        self.set_game2(1)
    def g2_two(self):
        self.g_photo2.config(image=self.game22)
        self.set_game2(2)
    def g2_three(self):
        self.g_photo2.config(image=self.game23)
        self.set_game2(3)


    def g2_photo(self):
        choose_photog2 = Toplevel(self.face1)
        choose_photog2.title = ('choose_photo')
        choose_photog2.geometry("300x100+600+250")

        photo1 = Button(choose_photog2,          # 按鈕所在視窗
                        image=self.game21,  # 顯示文字
                        command = self.g2_one) # 按下按鈕所執行的函數
        photo2 = Button(choose_photog2,          # 按鈕所在視窗
                        image=self.game22,  # 顯示文字
                        command = self.g2_two) # 按下按鈕所執行的函數
        photo3 = Button(choose_photog2,          # 按鈕所在視窗
                        image=self.game23,  # 顯示文字
                        command = self.g2_three) # 按下按鈕所執行的函數

        # 頭像選擇按鈕
        photo1.place(x=0,y=0,width=100,height=100)
        photo2.place(x=100,y=0,width=100,height=100)
        photo3.place(x=200,y=0,width=100,height=100)
        
#遊戲三 
    def g3_one(self):
        self.g_photo3.config(image=self.game31)
        self.set_game3(1)
    def g3_two(self):
        self.g_photo3.config(image=self.game32)
        self.set_game3(2)
    def g3_three(self):
        self.g_photo3.config(image=self.game33)
        self.set_game3(3)


    def g3_photo(self):
        choose_photog3 = Toplevel(self.face1)
        choose_photog3.title = ('choose_photo')
        choose_photog3.geometry("300x100+600+250")

        photo1 = Button(choose_photog3,          # 按鈕所在視窗
                        image=self.game31,  # 顯示文字
                        command = self.g3_one) # 按下按鈕所執行的函數
        photo2 = Button(choose_photog3,          # 按鈕所在視窗
                        image=self.game32,  # 顯示文字
                        command = self.g3_two) # 按下按鈕所執行的函數
        photo3 = Button(choose_photog3,          # 按鈕所在視窗
                        image=self.game33,  # 顯示文字
                        command = self.g3_three) # 按下按鈕所執行的函數

        # 頭像選擇按鈕
        photo1.place(x=0,y=0,width=100,height=100)
        photo2.place(x=100,y=0,width=100,height=100)
        photo3.place(x=200,y=0,width=100,height=100)

    # 回首頁方法
    def back(self):
        self.face1.destroy()
        initface(self.master)
    # 登出(回到登入頁面)
    def log_out(self):
        rot.destroy()
        os.system('python AR_login_FINAL.py')

# PLAY頁面
class face3():
    def __init__(self,master):
        self.master = master
        self.face1 = Frame(self.master,)
        self.face1.pack()

        result_from_get_account = sys.argv[1]
        result_list = result_from_get_account.strip('[()]').split(', ')
        result_list = [item.strip("'") for item in result_list]

        # 将查询结果作为命令行参数传递给 AR_home.py
        subprocess.run(['python', 'hand_tracker.py', str(result_list[0])])

        print(result_list)
        # 這個canva是放來隔著的，之後如果相機開得起來的話可以刪掉應該沒關西
        bg = Canvas(width=1200, height=700)
        bg.place(x=0,y=0)

    # 反回主頁方法，記得做按鈕
    def back(self):
        self.face3.destroy()
        initface(self.master)


if __name__ == '__main__':
    rot = Tk()
    app = basedesk(rot)
    rot.mainloop()
