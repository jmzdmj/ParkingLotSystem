# -*- coding:utf-8 -*-
"""
作者：bug君
日期：2023年 07月 04日
标题：
作用：
思路：
"""
import tkinter as tk
from db import Mysql_Object
from tkinter import ttk
import tkinter.messagebox as msgbox

class Addmanager:
    def __init__(self, master):
        # 连接数据库
        self.sql = Mysql_Object('localhost', 'root', '123456', 'parkinglot_management')

        self.win = master
        self.win.resizable(0, 0)
        self.win.title("添加操作员界面")

        # 窗口居中
        ww, wh = 450, 200
        sw, sh = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        x, y = (sw - ww) / 2, (sh - wh) / 2
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

        # 用户名
        l_usr = tk.Label(self.win, text="工号:")
        l_usr.place(x=30, y=30)
        # 密码
        l_key = tk.Label(self.win, text="密码:")
        l_key.place(x=30, y=60)
        # 密码确认
        l_cf = tk.Label(self.win, text="确认密码:")
        l_cf.place(x=30, y=90)
        # 员工类型
        l_type = tk.Label(self.win, text='员工类型')
        l_type.place(x=30, y=120)

        # 姓名
        l_name = tk.Label(self.win, text="员工姓名:")
        l_name.place(x=230, y=30)
        # 入职时间
        l_time = tk.Label(self.win, text="入职时间:")
        l_time.place(x=230, y=60)
        # 联系电话
        l_ph = tk.Label(self.win, text="联系电话:")
        l_ph.place(x=230, y=90)
        # 管理入口
        l_road = tk.Label(self.win, text='路口号')
        l_road.place(x=230, y=120)

        # 单行文本框
        self.var_usr = tk.StringVar()
        self.var_key = tk.StringVar()
        self.var_cf = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_time = tk.StringVar()
        self.var_ph = tk.StringVar()
        self.var_type = tk.StringVar()
        self.var_road = tk.StringVar()

        e_usr = tk.Entry(self.win, width=15, textvariable=self.var_usr)
        e_key = tk.Entry(self.win, width=15, textvariable=self.var_key)
        e_cf = tk.Entry(self.win, width=15, textvariable=self.var_cf)
        e_name = tk.Entry(self.win, width=15, textvariable=self.var_name)
        e_time = tk.Entry(self.win, width=15, textvariable=self.var_time)
        e_ph = tk.Entry(self.win, width=15, textvariable=self.var_ph)
        e_type = ttk.Combobox(self.win, width=12, textvariable=self.var_type)
        e_type['value'] = (
            '',
            '管理员',
            '操作员',
        )
        e_road = tk.Entry(self.win, width=15, textvariable=self.var_road)

        e_usr.place(x=100, y=30)
        e_key.place(x=100, y=60)
        e_cf.place(x=100, y=90)
        e_type.place(x=100, y=120)
        # e_name.place(x=100, y=160)

        e_name.place(x=300, y=30)
        e_time.place(x=300, y=60)
        e_ph.place(x=300, y=90)
        e_road.place(x=300, y=120)

        btn_save = tk.Button(self.win, text="保存", width=10, command=self.save)
        btn_exit = tk.Button(self.win, text="取消", width=10, command=self.win.quit)
        btn_save.place(x=140, y=160)
        btn_exit.place(x=240, y=160)

    def save(self):
        if self.var_key.get() != self.var_cf.get():
            msgbox.showerror(message='两次密码输入不一致！')

        msg = "insert into worker values ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.var_usr.get(), self.var_key.get(), self.var_name.get(), self.var_ph.get(), self.var_type.get(), self.var_road.get(), self.var_time.get())
        # print(msg)ds
        self.sql.excute_sql(msg)

        self.win.quit()
if __name__ == '__main__':
    window = tk.Tk()
    Addmanager(window)
    window.mainloop()