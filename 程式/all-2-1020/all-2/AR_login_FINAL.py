from tkinter import*
import tkinter.ttk as tt
from tkcalendar import Calendar
import datetime
import os
import mysql.connector
import subprocess


class basedesk():
    def __init__(self,master):
        self.root = master
        self.root.config()
        self.root.title('Base page')
        self.root.geometry('1200x700+150+50')
        root.resizable(False,False) #視窗縮放(是/否)
        

        initface(self.root)        
                
class initface():
    def __init__(self,master):
        
        self.master = master

        # !!!!!
        # 資料庫連線參數
        self.db_config = {
            'host': '140.131.114.140',  # 修改成你的 MySQL 伺服器 IP
            'port': 3306,         # 修改成你的 MySQL 伺服器 Port
            'user': '112501',        # 修改成你的 MySQL 使用者帳號
            'password': 'SportsWorld_112501',    # 修改成你的 MySQL 使用者密碼
            'database': '112-112501',  # 修改成你的資料庫名稱
        }

        # !!!!!
        # 連接到資料庫
        self.conn = mysql.connector.connect(**self.db_config)

        # 登入底圖
        self.img2 = PhotoImage(file="png/login_bg.png")
        bg = Canvas(width=1200, height=700)
        bg.create_image(0, 0,anchor=NW, image=self.img2)   # 在 Canvas 中放入圖片
        bg.place(x=0,y=0)

        self.initface = Frame(self.master,)
        self.initface.place()
        

        def on_entry_click_a(event):
            if act_in.get() == '請輸入帳號':
                act_in.delete(0, "end")  # 刪除現有文本
                act_in.insert(0, '')  # 插入一個空字符串，以便不顯示灰色文本
                act_in.config(fg='black')  # 將文本顏色設置為黑色

        def on_focus_out_a(event):
            if act_in.get() == '':
                act_in.insert(0, '請輸入帳號')
                act_in.config(fg='grey')  # 將文本顏色設置為灰色

        # !!!!!
        def get_account():
            account_value1 = user_id.get()
            account_value2 = password.get()

            # !!!!!
            # 創建一個游標物件
            self.initface_cursor1= self.conn.cursor()

            # !!!!!
            # 在這裡執行資料庫查詢
            query = "SELECT * FROM user_information WHERE user_name = %s AND password = %s"
            values = (account_value1, account_value2)

            # !!!!!
            # 執行查詢
            self.initface_cursor1.execute(query, values)

            # !!!!!
            # 獲取查詢結果
            result = self.initface_cursor1.fetchall()

            # !!!!!
            # 如果有符合的記錄，result 將包含該記錄的資料，否則為空
            if result:
                # 關閉當前視窗
                root.destroy()

                # 将查询结果作为命令行参数传递给 AR_home.py
                subprocess.run(['python', 'AR_home.py', str(result)])

            # !!!!!
            # 在這裡可以執行相應的操作，例如打開新的視窗等
            else:
                print("帳號或密碼錯誤，請重新輸入。")
                
        # !!!!!
        user_id = StringVar()  # 新增一個StringVar變數

        # !!!!!(修改textvariable=user_id)
        act_in = Entry(root, fg='grey', width=30, textvariable=user_id)
        act_in.insert(0, '請輸入帳號')
        act_in.bind('<FocusIn>', on_entry_click_a)
        act_in.bind('<FocusOut>', on_focus_out_a)
        act_in.place(x=480,y=425,width=300,height=30)
        # act_in = Entry(text="請輸入使用者帳號")
        # act_in.place(x=480,y=450,width=300,height=30)

        def on_entry_click_p(event):
            if psw_in.get() == '請輸入密碼':
                psw_in.delete(0, "end")  # 刪除現有文本
                psw_in.insert(0, '')  # 插入一個空字符串，以便不顯示灰色文本
                psw_in.config(fg='black')  # 將文本顏色設置為黑色

        def on_focus_out_p(event):
            if psw_in.get() == '':
                psw_in.insert(0, '請輸入密碼')
                psw_in.config(fg='grey')  # 將文本顏色設置為灰色

        # !!!!!(修改textvariable=user_id)
        password = StringVar()  # 新增一個StringVar變數

        # !!!!!(修改textvariable=password)
        psw_in = Entry(root, fg='grey', width=30, textvariable= password)
        psw_in.insert(0, '請輸入密碼')
        psw_in.bind('<FocusIn>', on_entry_click_p)
        psw_in.bind('<FocusOut>', on_focus_out_p)
        psw_in.place(x=480,y=485,width=300,height=30)

        # !!!!!(修改command= get_account)
        self.login_img = PhotoImage(file="png/iogin.png")
        login = Button(text="登入",command= get_account)
        login.config(image=self.login_img)
        login.place(x=480,y=575,width=100,height=35)
        self.re_img = PhotoImage(file="png/re.png")
        register = Button(text="我要註冊",command=self.change)
        register.config(image=self.re_img)
        register.place(x=620,y=575,width=100,height=35)
       
        
    def change(self,):       
        self.initface.destroy()
        face1(self.master)

    def login_home(self,):
        self.initface.destroy()
        root.destroy()
        os.system('python AR_home.py')
        

class face1():
    def __init__(self,master):
        self.master = master
        self.face1 = Frame(self.master,)
        self.face1.pack()

        # !!!!!
        # 資料庫連線參數
        self.db_config = {
            'host': '140.131.114.140',  # 修改成你的 MySQL 伺服器 IP
            'port': 3306,         # 修改成你的 MySQL 伺服器 Port
            'user': '112501',        # 修改成你的 MySQL 使用者帳號
            'password': 'SportsWorld_112501',    # 修改成你的 MySQL 使用者密碼
            'database': '112-112501',  # 修改成你的資料庫名稱
        }

        # !!!!!
        # 連接到資料庫
        self.conn = mysql.connector.connect(**self.db_config)

        # 註冊底圖
        self.img2 = PhotoImage(file="png/re_bg.png")
        bg = Canvas(width=1200, height=700)
        bg.create_image(0, 0,anchor=NW, image=self.img2)   # 在 Canvas 中放入圖片
        bg.create_text(440,315,text='性別',font=('華康粗黑體',18),fill='white')
        bg.create_text(440,365,text='身高',font=('華康粗黑體',18),fill='white')
        bg.create_text(635,365,text='體重',font=('華康粗黑體',18),fill='white')
        bg.create_text(440,415,text='生日',font=('華康粗黑體',18),fill='white')
        bg.create_text(440,465,text='暱稱',font=('華康粗黑體',18),fill='white')
        bg.create_text(440,515,text='密碼',font=('華康粗黑體',18),fill='white')
        bg.place(x=0,y=0)
        

        # !!!!!
        def add_account():
            account_value1 = gendervalue.get()
            account_value2 = float(heightvalue.get())
            account_value3 = float(weightvalue.get())
            account_value4 = bornvalue.get()
            account_value5 = user_id.get()
            account_value6 = password.get()
            account_value7 = self.avatar.get()

            print(account_value1,account_value2,account_value3,account_value4,account_value5,account_value6,account_value7)
            # !!!!!
            # 創建一個游標物件
            self.initface_cursor= self.conn.cursor()

            # !!!!!
            # 在這裡執行資料庫查詢
            query = "select count(*)+1 from user_information;"

            # !!!!!
            # 執行查詢
            self.initface_cursor.execute(query)

            # !!!!!
            # 獲取查詢結果
            result = self.initface_cursor.fetchall()

            # !!!!!
            # 在這裡執行資料庫查詢
            query1 = "INSERT INTO user_information (`id`, `user_name`, `password`, `gender`, `height`, `weight`, `born`, `avatar`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
            values = (result[0][0], account_value5,account_value6, account_value1, account_value2, account_value3, account_value4, account_value7)
            
            # !!!!!
            try:
                # 執行查詢
                self.initface_cursor.execute(query1, values)
                self.conn.commit()
                print("建立成功")
                initface(self.master)   

            except mysql.connector.Error as err:
                print("建立失敗")

        gendervalue = StringVar()  # 新增一個StringVar變數
        
        # 這邊性別做三種，如果影響到資料庫可以直接刪成兩個
        stdGrade = ('男','女','保密')

        comGrade = tt.Combobox(width=50, values=stdGrade, textvariable=gendervalue)
        comGrade.place(x=480, y=300, width=50, height=30)

        def on_entry_click_h(event):
            if height_in.get() == '請輸入身高（公分）':
                height_in.delete(0, "end")  # 刪除現有文本
                height_in.insert(0, '')  # 插入一個空字符串，以便不顯示灰色文本
                height_in.config(fg='black')  # 將文本顏色設置為黑色

        def on_focus_out_h(event):
            if height_in.get() == '':
                height_in.insert(0, '請輸入身高（公分）')
                height_in.config(fg='grey')  # 將文本顏色設置為灰色

        # !!!!!
        heightvalue = StringVar()  # 新增一個StringVar變數
        
        # !!!!!(修改textvariable=heightvalue)
        height_in = Entry(root, fg='grey', width=30, textvariable=heightvalue)
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

        # !!!!!
        weightvalue = StringVar()  # 新增一個StringVar變數


        # !!!!!(修改textvariable=weightvalue)
        weight_in = Entry(root, fg='grey', width=30, textvariable=weightvalue)
        weight_in.insert(0, '請輸入體重（公斤）')
        weight_in.bind('<FocusIn>', on_entry_click_w)
        weight_in.bind('<FocusOut>', on_focus_out_w)
        weight_in.place(x=670,y=350,width=110,height=30)
        # weight_in = Entry()
        # weight_in.place(x=670,y=350,width=110,height=30)

        def start_calendar():
            def print_sel():
                selected_date = cal.get_date()
                # selected_time = f"{hour.get()}:{minute.get()}"
                start_time_text.delete(0, END)
                start_time_text.insert(0, f"{selected_date} ")
                top.destroy()  # 關閉日期選擇視窗

            top = Toplevel()
            top.geometry("300x250")

            today = datetime.date.today()

            mindate = datetime.date(year=1900, month=1, day=1)
            maxdate = today + datetime.timedelta(days=5)
            # 日期選擇視窗裡面的配色等外面圖換好可以改
            cal = Calendar(top, font="Arial 14", selectmode='day', locale='zh_CN', mindate=mindate, maxdate=maxdate,
                        background="red", foreground="blue", bordercolor="red", selectbackground="red",
                        selectforeground="red", disabledselectbackground=False)
            cal.place(x=0, y=0, width=300, height=200)
        
            Button(top, text="確定", command=print_sel).place(x=240, y=205)

        # !!!!!
        bornvalue = StringVar()  # 新增一個StringVar變數

        start_time = Button(text="選擇日期", command=start_calendar)
        start_time.place(x=480,y=400)

        # !!!!!(修改textvariable=bornvalue)
        start_time_text = Entry(width=20, textvariable=bornvalue)
        start_time_text.place(x=550,y=400,width=230,height=30)

        def on_entry_click_a(event):
            if act_in.get() == '請輸入帳號':
                act_in.delete(0, "end")  # 刪除現有文本
                act_in.insert(0, '')  # 插入一個空字符串，以便不顯示灰色文本
                act_in.config(fg='black')  # 將文本顏色設置為黑色

        def on_focus_out_a(event):
            if act_in.get() == '':
                act_in.insert(0, '請輸入帳號')
                act_in.config(fg='grey')  # 將文本顏色設置為灰色

        user_id = StringVar()  # 新增一個StringVar變數

        
        act_in = Entry(root, fg='grey', width=30, textvariable=user_id)
        act_in.insert(0, '請輸入帳號')
        act_in.bind('<FocusIn>', on_entry_click_a)
        act_in.bind('<FocusOut>', on_focus_out_a)
        act_in.place(x=480,y=450,width=300,height=30)
        # act_in = Entry()
        # act_in.place(x=480,y=450,width=300,height=30)

        def on_entry_click_p(event):
            if psw_in.get() == '請輸入密碼':
                psw_in.delete(0, "end")  # 刪除現有文本
                psw_in.insert(0, '')  # 插入一個空字符串，以便不顯示灰色文本
                psw_in.config(fg='black')  # 將文本顏色設置為黑色

        def on_focus_out_p(event):
            if psw_in.get() == '':
                psw_in.insert(0, '請輸入密碼')
                psw_in.config(fg='grey')  # 將文本顏色設置為灰色
        
        # !!!!!
        password = StringVar()  # 新增一個StringVar變數

        # !!!!!(修改textvariable=password)
        psw_in = Entry(root, fg='grey', width=30, textvariable=password)
        psw_in.insert(0, '請輸入密碼')
        psw_in.bind('<FocusIn>', on_entry_click_p)
        psw_in.bind('<FocusOut>', on_focus_out_p)
        psw_in.place(x=480,y=500,width=300,height=30)

        self.re_btn = PhotoImage(file="png/re_bt_bg.png")
        register = Button(image=self.re_btn,command=add_account)
        register.place(x=550,y=575,width=100,height=35)

        self.had1 = PhotoImage(file="png/icon-1.png")
        self.had2 = PhotoImage(file="png/icon-2.png")
        self.had3 = PhotoImage(file="png/icon-3.png")

        # !!!!!
        self.avatar = StringVar()  # 新增一個StringVar變數

        self.photo = Button(text="Create new window",command=self.createNewWindow)
        self.photo.place(x=550,y=100,width=100, height=100)

    def one(self):
        self.photo.config(image=self.had1)

        # !!!!!
        self.set_avatar(1)

    def two(self):
        self.photo.config(image=self.had2)

        # !!!!!
        self.set_avatar(2)

    def three(self):
        self.photo.config(image=self.had3)

        # !!!!!
        self.set_avatar(3)

    # !!!!!
    def set_avatar(self, value):
        self.avatar.set(value)
    
    def createNewWindow(self):
        choose_photo = Toplevel(self.face1)
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

        # 以預設方式排版按鈕
        photo1.place(x=0,y=0,width=100,height=100)
        photo2.place(x=100,y=0,width=100,height=100)
        photo3.place(x=200,y=0,width=100,height=100)

    
    def back(self):
        self.face1.destroy()
        initface(self.master)
        
    
if __name__ == '__main__':    
    root = Tk()
    basedesk(root)
    root.mainloop()