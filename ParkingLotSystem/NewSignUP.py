# -*- coding:utf-8 -*-
"""
作者：bug君
日期：2023年 07月 03日
标题：
作用：
思路：
"""
import tkinter as tk
from tkinter import ttk
from db import Mysql_Object
import tkinter.messagebox as msgbox

class SignUp:
    def __init__(self, master: tk.Tk):
        # 连接数据库
        self.sql = Mysql_Object('localhost', 'root', '123456', 'parkinglot_management')

        self.window = master
        self.window.resizable(0, 0)
        self.window.title("用户注册界面")

        # 窗口居中
        ww, wh = 450, 250
        sw, sh = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        x, y = (sw - ww) / 2, (sh - wh) / 2
        self.window.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

        # 用户名
        l_usr = tk.Label(self.window, text="用户名:")
        l_usr.place(x=30, y=30)
        # 密码
        l_key = tk.Label(self.window, text="密码:")
        l_key.place(x=30, y=60)
        # 密码确认
        l_cf = tk.Label(self.window, text="确认密码:")
        l_cf.place(x=30, y=90)

        # 车牌
        l_bord = tk.Label(self.window, text="车牌标签:")
        l_bord.place(x=230, y=30)
        # 车辆类型
        l_type = tk.Label(self.window, text="车辆类型:")
        l_type.place(x=230, y=60)
        # 联系电话
        l_ph = tk.Label(self.window, text="联系电话:")
        l_ph.place(x=230, y=90)
        # 信息标签
        l_sm = tk.Label(self.window, text='如需购买车位，请填写以下信息', font=('宋体', 15))
        l_sm.place(x=80, y=125)
        # 固定车位
        l_sn = tk.Label(self.window, text="车位号:")
        l_sn.place(x=30, y=160)
        # 有效期
        l_vt = tk.Label(self.window, text="有效时长:")
        l_vt.place(x=230, y=160)

        # 单行文本框
        self.var_usr = tk.StringVar()
        self.var_key = tk.StringVar()
        self.var_cf = tk.StringVar()
        self.var_bord = tk.StringVar()
        self.var_type = tk.StringVar()
        self.var_ph = tk.StringVar()
        self.var_sn = tk.IntVar()
        self.var_vt = tk.StringVar()
        e_usr = tk.Entry(self.window, width=15, textvariable=self.var_usr)
        e_key = tk.Entry(self.window, width=15, textvariable=self.var_key)
        e_cf = tk.Entry(self.window, width=15, textvariable=self.var_cf)
        e_bord = tk.Entry(self.window, width=15, textvariable=self.var_bord)
        # e_type = tk.Entry(window, width=15, textvariable=var_type)

        e_type = ttk.Combobox(self.window, width=12, textvariable=self.var_type)
        e_type['value'] = (
            '',
            '新能源汽车',
            '传统型油车',
            '其他类型'
        )

        e_ph = tk.Entry(self.window, width=15, textvariable=self.var_ph)

        # 执行查询语句
        Sno = self.sql.select_sql("select Sno from parkingspot where Slabel = '固定' and Sstate = '未占用' and Stype='新能源汽车';")[1]
        Sno = [x[0] for x in Sno]

        Sno.append('以下是油车位')

        Sno1 = self.sql.select_sql("select Sno from parkingspot where Slabel = '固定' and Sstate = '未占用' and Stype='传统型油车';")[1]
        Sno1 = [x[0] for x in Sno1]

        Sno.extend(Sno1)
        e_sn = ttk.Combobox(self.window, width=12, textvariable=self.var_sn)
        e_sn['value'] = Sno

        e_vt = ttk.Combobox(self.window, width=12, textvariable=self.var_vt)
        e_vt['value'] = (
            '',
            '一月',
            '三月',
            '六月',
            '十二月'
        )
        e_usr.place(x=100, y=30)
        e_key.place(x=100, y=60)
        e_cf.place(x=100, y=90)
        e_sn.place(x=100, y=160)

        e_bord.place(x=300, y=30)
        e_type.place(x=300, y=60)
        e_ph.place(x=300, y=90)
        e_vt.place(x=300, y=160)

        btn_save = tk.Button(self.window, text="保存", width=10, command=self.save)
        btn_exit = tk.Button(self.window, text="取消", width=10, command=self.window.quit)
        btn_save.place(x=140, y=200)
        btn_exit.place(x=240, y=200)


    def save(self):
        if self.var_key.get() != self.var_cf.get():
            msgbox.showerror(message='两次密码输入不一致！')

        if self.var_sn.get() and self.var_vt.get():
            var_ot = '固定'
            s = 'update parkingspot set Sstate="占用", Cno="%s", Suse_time="%d" where Sno= "%d"' % (self.var_bord.get(), self.var_sn.get(), 0)
            print(s)
            self.sql.excute_sql(s)
        else:
            var_ot = '临时'
        value = (self.var_usr.get(), self.var_key.get(), self.var_bord.get(), self.var_type.get(), self.var_ph.get(), var_ot, self.var_vt.get(), self.var_sn.get())
        # print(value)
        s = 'insert into owner values' + str(value)
        self.sql.excute_sql(s)

        self.window.quit()




if __name__ == '__main__':
    window = tk.Tk()
    SignUp(window)
    window.mainloop()