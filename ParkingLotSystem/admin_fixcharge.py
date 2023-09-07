from db import Mysql_Object
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox

class admin_fixcharge:
    def __init__(self, master):
        # 连接数据库
        self.sql = Mysql_Object('localhost', 'root', '123456', 'parkinglot_management')
        self.win = master
        self.win.resizable(0, 0)
        self.win.title('管理收费标准界面')

        # 窗口居中
        ww, wh = 400, 200
        sw, sh = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        x, y = (sw - ww) / 2, (sh - wh) / 2
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

        lb = tk.Label(self.win, text="管理员id: ")
        lb.pack(side="left", padx=10, anchor="nw")

        show_free = tk.Label(self.win, text=self.show_id())
        show_free.pack(side="left", padx=10, anchor="nw")
        # var_num = tk.IntVar()
        # e1 = tk.Entry(window, textvariable=var_num)
        # e1.place(side="left", padx=10, pady=10, anchor="sw")

        lb = tk.Label(self.win, text="当前收费标准：")
        lb.place(relx=0.1,rely=0.2)

        # 创建多行文本框
        self.charge = tk.Text(self.win, width=20, height=5)
        self.charge.place(relx=0.3, rely=0.2)

        # 查询收费标准
        btn_sel = tk.Button(self.win, text="查询缴费标准", command=self.pay_standard)
        btn_sel.place(relx=0.7,rely=0.2)


        lb2 = tk.Label(self.win, text='输入更改的类型：')
        lb2.place(relx=0.1,rely=0.6)

        self.var_type = tk.StringVar()
        e_spot = ttk.Combobox(self.win, width=12, textvariable=self.var_type)
        e_spot['value'] = (
            '',
            '新能源汽车',
            '传统型油车'
        )

        e_spot.place(relx=0.35,rely=0.6)

        lb2 = tk.Label(self.win, text='输入更改的值：')
        lb2.place(relx=0.1, rely=0.75)

        self.var_value = tk.DoubleVar()
        e_spot = tk.Entry(self.win, textvariable=self.var_value, width=10)
        e_spot.place(x=140, y=150)

        btn_del = tk.Button(self.win, text="更改", command=self.set_charge)
        btn_exit = tk.Button(self.win, text="退出", command=self.win.destroy)
        # 放置
        btn_exit.place(relx=0.8, rely=0.8, relheight=0.1, relwidth=0.1)
        btn_del.place(relx=0.7, rely=0.8, relheight=0.1, relwidth=0.1)

    # 获取工号
    def show_id(self):
        # 这里查询当前用户id并返回
        with open('current_user.text', 'r') as f:
            msg = f.read().strip('(').strip(')').split(',')
            # print(msg[0])
        return msg[0].strip("'")

    # 查询缴费标准
    def pay_standard(self):
        # 这里查询缴费标准
        self.charge.delete(1.0, tk.END)
        msg = "select * from charge_standard"
        charge = self.sql.select_sql(msg)[1]
        # print(charge)
        for stanard in charge:
            self.charge.insert(tk.END, stanard)
            self.charge.insert(tk.END, '\n')


    # 这里实现更改缴费标准
    def set_charge(self):
        # 这里写入更改缴费
        msg = "update charge_standard set standard='{}' where Ctype='{}'".format(self.var_value.get(), self.var_type.get())
        self.sql.excute_sql(msg)
        msgbox.showinfo(message='更改成功')
        self.pay_standard()


    def get_msg(self):
        with open('current_user.text', 'r') as f:
            msg = f.read().strip('(').strip(')').split(',')
        return msg


if __name__ == '__main__':
    window = tk.Tk()
    admin_fixcharge(window)
    window.mainloop()
