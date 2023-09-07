# -*- coding:utf-8 -*-
"""
作者：bug君
日期：2023年 07月 04日
标题：
作用：
思路：
"""
import os

from db import Mysql_Object
import tkinter as tk


class admin_setmanager:
    def __init__(self, master):
        # 连接数据库
        self.sql = Mysql_Object('localhost', 'root', '123456', 'parkinglot_management')
        self.win = master
        self.win.resizable(0, 0)
        self.win.title('管理操作员界面')

        # 窗口居中
        ww, wh = 600, 400
        sw, sh = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        x, y = (sw - ww) / 2, (sh - wh) / 2
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

        # 搭建存储文本框的frame
        self.f1 = tk.Frame(self.win, width=ww - 20, height=wh - 80, bg="lightgreen")
        self.f1.pack(padx=10, pady=10)

        # 创建多行文本框
        self.t1 = tk.Text(self.f1, width=ww - 40, height=21)
        self.t1.pack(side="top", padx=10, pady=10)


        # e1 = tk.Entry(window, textvariable=var_num)
        # e1.pack(side="left", padx=10, pady=10, anchor="sw")

        lb2 = tk.Label(self.win, text='输入操作员编号：')
        lb2.place(relx=0.2, rely=0.9)

        self.manage_no = tk.StringVar()
        e_spot = tk.Entry(self.win, textvariable=self.manage_no, width=5)
        e_spot.place(relx=0.4, rely=0.9)

        btn_sel = tk.Button(self.win, text="查询所有操作员", command=self.select_manager)
        btn_sel.pack(side="left", padx=10, anchor="nw")

        btn_cf = tk.Button(self.win, text="删除操作员", command=self.del_mannager)
        btn_cf.place(relx=0.55, rely=0.9)
        btn_del = tk.Button(self.win, text="增加操作员", command=self.create_manager)

        btn_exit = tk.Button(self.win, text="退出", command=self.win.destroy)
        # 放置
        btn_exit.place(relx=0.9, rely=0.9)
        btn_del.place(relx=0.7, rely=0.9)


    # 查看所有操作员
    def select_manager(self):
        self.t1.delete(1.0, tk.END)
        self.t1.insert(1.0, "员工号\t密码\t姓名\t联系电话\t\t管理路口\t\t入职日期\n")
        msg = self.sql.select_sql("select * from worker where Wtype='操作员'")[1]
        print(msg)
        for worker in msg:
            self.t1.insert('end', "{}\t{}\t{}\t{}\t\t{}\t\t{}\n".format(worker[0], worker[1], worker[2], worker[3], worker[5], worker[6]))

    # 这里删除操作员
    def del_mannager(self):
       #根据操作员编号删除操作员
        msg = "delete from worker where Wno='{}'".format(self.manage_no.get())
        self.sql.excute_sql(msg)
        self.select_manager()

    #这里增加操作员
    def create_manager(self):
        #跳转到增加操作员界面
        os.system('python admin_addmanager.py')



if __name__ == '__main__':
    window = tk.Tk()
    admin_setmanager(window)
    window.mainloop()
