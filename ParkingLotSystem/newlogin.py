# -*- coding:utf-8 -*-
"""
作者：bug君
日期：2023年 07月 03日
标题：
作用：
思路：
"""
from tkinter import *
import tkinter.messagebox as msgbox
from db import Mysql_Object
# from NewSignUP import SignUp
# from User_page import User_page
import os


class Login:
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

        # 欢迎使用
        l_wlc = Label(self.win, text="您好，欢迎光临天上人间停车场！", font=("宋体", 18))
        l_wlc.pack()

        # 用户名、密码标签框
        l_usr = Label(self.win, text="用户名：")
        l_usr.place(x=65, y=60)
        l_key = Label(self.win, text="密码：")
        l_key.place(x=65, y=100)

        # 用户名、密码输入框

        self.var1 = StringVar()
        self.var2 = StringVar()
        e_usr = Entry(self.win, textvariable=self.var1)
        e_key = Entry(self.win, textvariable=self.var2, show="*")
        e_usr.place(x=145, y=60)
        e_key.place(x=145, y=100)

        # 身份选项
        self.sel_var = IntVar()
        self.sel_var.set(1)
        id_tag = Label(self.win, text='选择您的身份： ')
        id_tag.place(x=65, y=140)

        id_val1 = Radiobutton(self.win, text='车主', value=1, variable=self.sel_var)
        id_val2 = Radiobutton(self.win, text='操作员', value=2, variable=self.sel_var)
        id_val3 = Radiobutton(self.win, text='管理员', value=3, variable=self.sel_var)
        id_val1.place(x=160, y=140)
        id_val2.place(x=220, y=140)
        id_val3.place(x=290, y=140)

        # 登录 与 退出
        btn_login = Button(self.win, text="登录", width=8, command=self.login)
        btn_login.place(x=100, y=180)
        # 退出
        btn_exit = Button(self.win, text="退出", width=8, command=self.win.quit)
        btn_exit.place(x=220, y=180)

        # 显示停车场空闲车位
        freespot = Label(self.win, text='停车场空闲车位：')
        freespot.pack(side='left', anchor='sw')

        # free_num = getfreespot()
        show_free = Label(self.win, text=self.getfreespot())
        show_free.pack(side='left', anchor='sw')

        # 跳转到注册页面
        btn_sign = Button(self.win, text="注册", fg="green", borderwidth=0, command=self.sign_up)
        btn_sign.pack(side='right', anchor="se")

    def getfreespot(self):
        '''
        # 在左下脚打印空闲车位数
        :return:
        '''
        return self.sql.select_sql("select count(Sno) from parkingspot where Slabel = '临时' and Sstate = '未占用'")[1]

    def next_window(self):
        id = self.sel_var.get()  # 得到数字
        id_dict = {1: 'User_page.py', 2: 'manager_page.py', 3: 'Admin_page.py'}
        # next_win = 'ower_window.py'
        os.system(f'python {id_dict[id]}')
        # win = Tk()
        # User_page(win)
        # win.mainloop()
        # os.system('python User_page.py')
        # self.win.quit()

    # 登录验证
    def login(self):
        '''
         在点击登录选项后执行的操作
        :return:
        '''

        # 获得登录用户名、密码，身份。
        name = self.var1.get()
        pwd = self.var2.get()
        # id = sel_var
        id = self.sel_var.get()  # 得到数字
        id_dict = {1: "select * from owner", 2: "select * from worker", 3: "select * from worker"}

        # 线程程设置
        # t1 = threading.Thread(target=win.quit(), daemon=True)
        # t2 = threading.Thread(target=next_window())

        # 登入前检查：判断输入框是否为空
        if name != '':
            if pwd != '':

                # 从数据库中得到相关身份的注册信息
                listAll = self.sql.select_sql(id_dict[id])[1]

                # 将输入数据与数据库进行比对
                for person in listAll:
                    if person[0] == name and person[1] == pwd:
                        with open('current_user.text', 'w+') as file:
                            file.write(str(person))
                        self.win.quit()
                        self.next_window()
                        # t2.start()
                        # t1.start()
                        break
                else:
                    msgbox.showerror(message='用户名或者密码错误！')
            else:
                msgbox.showerror("⚠", "请输入密码")
        else:
            msgbox.showerror("⚠", "请输入用户名")

    def sign_up(self):
        '''
        在点击注册选项后所执行的操作
        :return:
        '''
        os.system('python NewSignUP.py')
        # new_win = Tk()
        # SignUp(new_win)
        # new_win.mainloop()


if __name__ == '__main__':
    window = Tk()
    Login(window)
    window.mainloop()
