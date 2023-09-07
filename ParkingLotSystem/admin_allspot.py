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

class Allspot:
    def __init__(self, master):
        self.sql = Mysql_Object('localhost', 'root', '123456', 'parkinglot_management')
        self.win = master
        self.win.resizable(0, 0)
        self.win.title('车位管理界面')

        # 窗口居中
        ww, wh = 800, 400
        sw, sh = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        x, y = (sw - ww) / 2, (sh - wh) / 2
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

        # 搭建存储文本框的frame
        self.f1 = tk.Frame(self.win, width=ww - 20, height=wh - 80, bg="lightgreen")
        self.f1.pack(padx=10, pady=10)

        # 创建多行文本框
        self.t1 = tk.Text(self.f1, width=ww - 40, height=21)
        self.t1.pack(side="top", padx=10, pady=10)

        btn_search = tk.Button(self.win, text='查询已停车信息', command=self.search_spot)
        btn_search.pack(side="left", padx=10, anchor="nw")

        btn_exit = tk.Button(self.win, text="退出", command=self.win.destroy)
        btn_exit.pack(side="right", padx=10, pady=10, anchor="se")



    def search_spot(self):
        msg = "select * from parkingspot where Sstate ='占用'"
        msg = self.sql.select_sql(msg)[1]
        self.t1.delete(1.0, tk.END)
        self.t1.insert(1.0, "车位号\t\t车辆标签\t\t车位类型\t\t占用状态\t\t车牌号\t\t预约时间\t\t预约状态\n")
        print(msg)
        for msg in msg:
            self.t1.insert('end', "{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\n".format(msg[0], msg[1], msg[2], msg[3], msg[4], msg[5], msg[7]))


if __name__ == '__main__':
    window = tk.Tk()
    Allspot(window)
    window.mainloop()
