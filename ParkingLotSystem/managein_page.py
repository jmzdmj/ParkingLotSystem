
from db import Mysql_Object
import tkinter as tk
import random as rd
import tkinter.messagebox as msgbox

class manage_page:
    def __init__(self, master):
        # 连接数据库
        self.sql = Mysql_Object('localhost', 'root', '123456', 'parkinglot_management')
        self.win = master
        self.win.resizable(0, 0)
        self.win.title('入场管理界面')

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

        lb = tk.Label(self.win, text="工号: ")
        lb.pack(side="left", padx=10, anchor="nw")

        show_free = tk.Label(self.win, text=self.get_id())
        show_free.pack(side='left', padx=10, anchor='nw')
        # var_num = tk.IntVar()
        # e1 = tk.Entry(window, textvariable=var_num)
        # e1.pack(side="left", padx=10, pady=10, anchor="sw")

        lb2 = tk.Label(self.win, text='输入车牌：')
        lb2.pack(side='left', padx=10, anchor='nw')

        self.var_spot = tk.StringVar()
        e_spot = tk.Entry(self.win, textvariable=self.var_spot, width=5)
        e_spot.pack(side='left', padx=15, anchor='nw')

        btn_cf = tk.Button(self.win, text="查看预约", command=self.search_reserve)
        btn_cf.pack(side="left", padx=10, anchor="nw")

        lb3 = tk.Label(self.win, text='选择车位：')
        lb3.pack(side='left', padx=10, anchor='nw')

        self.chosen_no = tk.IntVar()
        e_spot = tk.Entry(self.win, textvariable=self.chosen_no, width=5)
        e_spot.pack(side='left', padx=10, anchor='nw')

        btn_sel = tk.Button(self.win, text="查询空闲车位", command=self.select_spot)
        btn_sel.pack(side="left", padx=10, anchor="nw")

        btn_cfs = tk.Button(self.win, text='确认车位', command=self.cf_spot)
        btn_cfs.pack(side="left", padx=10, anchor="nw")

        btn_del = tk.Button(self.win, text="通行", command=self.let_goin)

        btn_exit = tk.Button(self.win, text="退出", command=self.win.destroy)
        # 放置
        btn_exit.pack(side="right", padx=10, pady=10, anchor="se")
        btn_del.pack(side="right", pady=10, anchor="se")

    #获取工号
    def get_id(self):
        msg = self.get_msg()[0].strip().strip("'")
        return msg

    # 查看空闲车位信息
    def select_spot(self):
        self.t1.delete(1.0, tk.END)
        self.t1.insert(1.0, "车位号\t\t车辆标签\t\t车位类型\t\t占用状态\n")
        msg = self.sql.select_sql("select * from parkingspot where Slabel='临时' and Sstate='未占用'")[1]
        # print(msg)
        for spot in msg:
            self.t1.insert('end', "{}\t\t{}\t\t{}\t\t{}\n".format(spot[0], spot[1], spot[2], spot[3]))

    #这里返回查询的预约记录
    def search_reserve(self):
        # print(self.var_spot)
        msg = "select * from parkingspot where Cno='{}'".format(self.var_spot.get())
        msg = self.sql.select_sql(msg)
        self.t1.delete(1.0, tk.END)
        self.t1.insert(1.0, "车位号\t\t车辆标签\t\t车位类型\t\t占用状态\t\t车牌号\t\t预约时间\t\t预约状态\n")
        for msg in msg[1]:
            self.t1.insert('end', "{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\n".format(msg[0], msg[1], msg[2], msg[3], msg[4], msg[5], msg[7]))

    # 确认车位
    def cf_spot(self):
        msg = "update parkingspot set Sstate='占用', Cno='{}', Suse_time='{}' where Sno='{}'".format(self.var_spot.get(), self.get_randusetiem(), self.chosen_no.get())
        self.sql.excute_sql(msg)
        msgbox.showinfo(message="确认成功")
        self.select_spot()

    # 获得随机使用时间
    def get_randusetiem(self):
        return rd.randint(10, 300)

    #这里实现通行
    def let_goin(self):
       #这里写入通行逻辑操作
       msgbox.showinfo(message="车辆已入场")


    def get_msg(self):
        with open('current_user.text', 'r') as f:
            msg = f.read().strip('(').strip(')').split(',')
            # print(msg)
        return msg


if __name__ == '__main__':
    window = tk.Tk()
    manage_page(window)
    window.mainloop()
