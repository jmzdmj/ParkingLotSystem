from db import Mysql_Object
import tkinter as tk
import tkinter.messagebox as msgbox

class manage_page:
    def __init__(self, master):
        # 连接数据库
        self.sql = Mysql_Object('localhost', 'root', '123456', 'parkinglot_management')
        self.win = master
        self.win.resizable(0, 0)
        self.win.title('出场管理界面')

        # 窗口居中
        ww, wh = 400, 200
        sw, sh = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        x, y = (sw - ww) / 2, (sh - wh) / 2
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

        lb = tk.Label(self.win, text="工号: ")
        lb.pack(side="left", padx=10, anchor="nw")

        show_free = tk.Label(self.win, text=self.get_id())
        show_free.pack(side="left", padx=10, anchor="nw")
        # var_num = tk.IntVar()
        # e1 = tk.Entry(window, textvariable=var_num)
        # e1.place(side="left", padx=10, pady=10, anchor="sw")

        lb2 = tk.Label(self.win, text='输入车牌：')
        lb2.place(x=20, y=40)

        self.var_spot = tk.StringVar()
        e_spot = tk.Entry(self.win, textvariable=self.var_spot, width=10)
        e_spot.place(x=80, y=40)

        btn_sel = tk.Button(self.win, text="查询缴费状态", command=self.pay_state)
        btn_sel.place(x=200, y=40)

        lb3 = tk.Label(self.win, text="缴费状态: ")
        lb3.place(x=20, y=100)

        # 展示框
        self.order_text = tk.Text(self.win, width=10, height=1)
        self.order_text.place(x=90, y=100)
        # show_state = tk.Label(self.win, text=self.pay_state())
        # show_state.place(x=100,y=100)

        btn_cf = tk.Button(self.win, text="缴费", command=self.pay_for)
        btn_cf.place(relx=0.6, rely=0.8, relheight=0.1, relwidth=0.1)

        btn_del = tk.Button(self.win, text="通行", command=self.pass_through)

        btn_exit = tk.Button(self.win, text="退出", command=self.win.destroy)
        # 放置
        btn_exit.place(relx=0.8, rely=0.8, relheight=0.1, relwidth=0.1)
        btn_del.place(relx=0.7, rely=0.8, relheight=0.1, relwidth=0.1)

    # 获取工号
    def get_id(self):
        msg = self.get_msg()[0].strip().strip("'")
        return msg

    # 查询缴费状态
    def pay_state(self):
        # 这里查询车辆停车信息返回缴费状态
        self.order_text.delete(1.0, tk.END)
        msg = "select * from parkingspot where Cno='{}'".format(self.var_spot.get())
        msg = self.sql.select_sql(msg)[1]
        temp = '不存在费用'
        print(msg)
        if msg:
            for spot in msg:
                if spot[6] is None:
                    temp = '未缴费'
        self.order_text.insert(tk.END, temp)

    # 这里是缴费实现更改状态
    def pay_for(self):
        msg = "update parkingspot set Spay_state='已缴费' where Cno='{}'".format(self.var_spot.get())
        self.sql.excute_sql(msg)
        msgbox.showinfo(message='缴费成功')

    # 这里实现通行
    def pass_through(self):
        # 这里写入通行逻辑操作
        msgbox.showinfo(message="车辆已出场")
        self.win.quit()

    def get_msg(self):
        with open('current_user.text', 'r') as f:
            msg = f.read().strip('(').strip(')').split(',')
            # print(msg)
        return msg


if __name__ == '__main__':
    window = tk.Tk()
    manage_page(window)
    window.mainloop()
