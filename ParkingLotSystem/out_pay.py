import tkinter as tk
from tkinter import *
from db import Mysql_Object
import tkinter.messagebox as msgbox


class Out_pay:
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


        # 添加标签显示当前停车记录的ID
        current_parking_id=str(self.show_id())
        id_label = tk.Label(self.win, text="ID：" + current_parking_id)
        id_label.pack(pady=10)

        # 添加text文本框显示当前待支付订单信息
        order_text = tk.Text(self.win, width=30, height=5)
        order_text.pack(pady=10)

        # 在text文本框中显示当前待支付订单信息
        current_parking_order = self.payment()
        # 假设当前停车订单的信息为一个字典
        # current_parking_order = {
        #     "车辆信息": "车辆1",
        #     "停车时长": "2小时",
        #     "停车费用": "10元"
        # }
        # 清空text文本框中的内容
        order_text.delete("1.0", tk.END)
        for key, value in current_parking_order.items():
            order_text.insert(tk.END, key + ": " + value + "\n")

        pay_button = tk.Button(self.win, text="支付", command=self.pay)
        pay_button.pack(pady=10)

    # 添加支付按钮
    def pay(self):
        # 在这里实现支付逻辑，可以将支付成功的信息显示在text文本框中\
        borad = self.get_borad()
        msg = "update parkingspot set Spay_state='已缴费' where Cno='{}'".format(borad)
        self.sql.excute_sql(msg)
        msgbox.showinfo(message="支付成功")
        self.win.quit()

    def show_id(self):
        # 这里查询当前用户id并返回
        msg = self.get_msg()[0].strip().strip("'")
        return msg

    def get_msg(self):
        with open('current_user.text', 'r') as f:
            msg = f.read().strip('(').strip(')').split(',')
        return msg

    def get_borad(self):
        msg = self.get_msg()[2].strip().strip("'")
        return msg

    def get_type(self):
        msg = self.get_msg()[3].strip().strip("'")
        return msg

    def payment(self):
        """这里查询停车信息并返回一个字典
        current_parking_order = {
            "车辆信息": "车辆1",
            "停车时长": "2小时",
            "停车费用": "10元"
        }
        """
        borad= self.get_borad()
        msg1 = "select SUM(Suse_time) from parkingspot where Cno='{}' and Spay_state is null".format(borad)
        all_time = int(self.sql.select_sql(msg1)[1][0][0])


        msg2 = "select standard from charge_standard where Ctype='{}'".format(self.get_type())
        standard = self.sql.select_sql(msg2)[1][0][0]
        # print(self.get_type())
        # print(standard)

        current_parking_order = {
            "车辆信息": borad,
            "停车时长": f"{all_time}分钟",
            "收费标准": f"{standard}元|分钟",
            "停车费用": f"{all_time*standard:.2f}元"
        }
        return current_parking_order




if __name__ == "__main__":
    window = Tk()
    window.title("缴费界面")
    Out_pay(window)
    window.mainloop()
