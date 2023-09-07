from tkinter import *
import os
from db import Mysql_Object


class manager_page:
    def __init__(self, master):
        # 连接数据库
        self.sql = Mysql_Object('localhost', 'root', '123456', 'parkinglot_management')

        self.win = master
        self.win.resizable(0, 0)
        # 窗口居中
        ww, wh = 400, 250
        sw, sh = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        x, y = (sw - ww) / 2, (sh - wh) / 2
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

        # 添加显示工号
        Userid = Label(self.win, text='工号:')
        Userid.pack(side='left', anchor="nw")
        User_id = Label(self.win, text=self.show_id().strip("'"))
        User_id.pack(side='left', anchor="nw")

        # 添加显示空余车位
        Empty_num = Label(self.win, text=self.show_Emptynum())
        Empty_num.pack(side='right', anchor='sw')
        Empty = Label(self.win, text='空余车位:')
        Empty.pack(side='right', anchor='sw')

        # 添加按钮
        getin_button = Button(self.win, text="入场管理", width=14, command=self.manage_in)
        getin_button.place(x=150, y=30)

        exit_button = Button(self.win, text="出场管理", width=14, command=self.manage_out)
        exit_button.place(x=150, y=70)

        quit_button = Button(self.win, text="退出", command=self.win.quit)
        quit_button.place(x=200, y=190)

    def manage_in(self):
        # 这里可以实现入场管理功能
        os.system('python managein_page.py')

    def manage_out(self):
        # 这里可以实现车辆离场的功能
        os.system('python manageout_page.py')

    def show_id(self):
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
    Win.title("操作员界面")
    manager_page(Win)
    Win.mainloop()
