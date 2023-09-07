# -*- coding:utf-8 -*-
"""
作者：bug君
日期：2023年 07月 04日
标题：
作用：
思路：
"""
import os
import tkinter as tk

class AdminPage:
    def __init__(self, master):
        self.win = master
        self.win.resizable(0, 0)
        self.win.title("管理员")

        # 窗口居中偏右
        ww, wh = 400, 250
        sw, sh = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        x, y = (sw - ww) / 2, (sh - wh) / 2
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

        # 添加显示id
        # 添加显示工号
        Userid = tk.Label(self.win, text='Operator:', font=("幼圆", 10))
        Userid.pack(side='left', anchor="nw")
        User_id = tk.Label(self.win, text=self.show_id())
        User_id.pack(side='left', anchor="nw")

        # btn_admin = tk.Button(self.win, text="修改信息", fg="green", borderwidth=0, command=admin_modify)
        # btn_admin.pack(side="right", anchor="ne")
        # # 功能面板
        l_functions = tk.Label(self.win, text="功能菜单", bg="lightgreen", font=("黑体", 14))
        l_functions.place(x=20, y=50)

        btn_add = tk.Button(window, text="管理操作员", width=15, font=("宋体", 12), command=self.control_manager)
        btn_select = tk.Button(window, text="管理收费标准", width=15, font=("宋体", 12), command=self.charge_standard)
        btn_findall = tk.Button(window, text="查看所有停车信息", width=18, font=("宋体", 12), command=self.all_spots)
        btn_exit = tk.Button(window, text="退出登录", width=14, font=("黑体", 14), command=window.quit)
        # 放置 间隔40
        btn_add.place(x=40, y=90)
        btn_select.place(x=180, y=90)
        btn_findall.place(x=40, y=130)
        btn_exit.place(x=100, y=200)


    def control_manager(self):
        os.system('python admin_setmanager.py')

    def charge_standard(self):
        os.system('python admin_fixcharge.py')

    def all_spots(self):
        os.system('python admin_allspot.py')


    def show_id(self):
        # 这里查询当前用户id并返回
        with open('current_user.text', 'r') as f:
            msg = f.read().strip('(').strip(')').split(',')
            # print(msg[0])
        return msg[0].strip("'")



if __name__ == '__main__':
    window = tk.Tk()
    AdminPage(window)
    window.mainloop()

