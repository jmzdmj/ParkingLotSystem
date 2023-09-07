import os
from tkinter import *
from db import Mysql_Object

class User_page:
    def __init__(self, master):
        # 连接数据库
        self.sql = Mysql_Object('localhost', 'root', '123456', 'parkinglot_management')
        self.win = master
        self.win.resizable(0, 0)
        self.win.title("用户界面")

        # 窗口居中
        ww, wh = 400, 250
        sw, sh = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        x, y = (sw - ww) / 2, (sh - wh) / 2
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

        # 添加显示id
        Userid = Label(self.win, text='用户id为:')
        Userid.pack(side='left', anchor="nw")
        User_id = Label(self.win, text=self.show_current().strip("'"))
        User_id.pack(side='left', anchor="nw")

        # 添加显示空余车位
        Empty = Label(self.win, text=self.show_Emptynum())
        Empty.pack(side='right', anchor='sw')

        Empty = Label(self.win, text='空余车位:')
        Empty.pack(side='right', anchor='sw')

        # 添加按钮
        reserve_button = Button(self.win, text="预约车位", width=14, command=self.reserve_parking)
        reserve_button.place(x=150, y=30)

        exit_button = Button(self.win, text="车辆离场", width=14, command=self.vehicle_exit)
        exit_button.place(x=150, y=70)


        quit_button = Button(self.win, text="退出", command=self.win.quit)
        quit_button.place(x=200, y=190)


    def reserve_parking(self):
        # 这里可以实现预约车位的功能
        os.system('python Reserve_page.py')

    def vehicle_exit(self):
        # 这里可以实现车辆离场的功能
        os.system('python out_pay.py')


    def show_current(self):
        # 这里查询当前用户id并返回
        with open('current_user.text', 'r') as f:
            msg = f.read().strip('(').strip(')').split(',')
            # print(msg[0])
        return msg[0]

    def show_Emptynum(self):
        # 这里返回空余车位数
        return self.sql.select_sql("select count(Sno) from parkingspot where Slabel = '临时' and Sstate = '未占用'")[1]


if __name__ == "__main__":
    Win = Tk()
    User_page(Win)
    Win.mainloop()
