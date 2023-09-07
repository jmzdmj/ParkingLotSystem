# -*- coding:utf-8 -*-
"""
作者：bug君
日期：2023年 07月 03日
标题：
作用：
思路：
"""
import pymysql


class Mysql_Object():
    def __init__(self, host, user, password, database, port=3306, charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset

    def select_sql(self, sql, size=0):
        '''
        查询sql语句
        :param sql 传入查询的sql语句，字符串
        :param size 返回结果的记录条数，如果没有输入默认输出全部条数
        :return: self.count 返回查询的记录的总数，slef.res 返回查询的结果
        '''
        self.con = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port, charset=self.charset)
        self.cur = self.con.cursor()  # 建立游标
        self.sql = sql
        # 判读是否是查询语句
        if self.sql.startswith('select'):
            self.cur.execute(self.sql)  # 获取数据库结果
            self.count = self.cur.rowcount  # 统计查询记录数
            # 通过if语句进行判断
            if size == 0:
                self.res = self.cur.fetchall()  # 输出全部结果
            elif size != 0:
                self.res = self.cur.fetchmany(size)  # 输出指定数值

            self.cur.close()
            self.con.close()  # 关闭连接
        return self.count, self.res

    def excute_sql(self, sql):
        '''
        :param sql 输入增删改的sql语句
        :return:
        '''
        self.con = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port, database=self.database,
                                   charset=self.charset, autocommit=True)
        self.cur = self.con.cursor()  # 建立游标
        self.sql = sql

        if self.sql.startswith('insert'):
            print('插入语句', self.sql)
            self.cur.execute(self.sql)  # 执行语句
            self.cur.close()  # 关闭连接
            self.con.close()
        if self.sql.startswith('delete'):
            print('删除语句', self.sql)
            self.cur.execute(self.sql)  # 执行语句
            self.cur.close()  # 关闭连接
            self.con.close()
        if self.sql.startswith('update'):
            print('更新语句', self.sql)
            self.cur.execute(self.sql)  # 执行语句
            self.cur.close()  # 关闭连接
            self.con.close()


# 调用测试
if __name__ == '__main__':
    # set_time = str(datetime.date.today())
    m = Mysql_Object('localhost', 'root', '123456', 'parkinglot_management')
    # print(m.select_sql('select * from worker'))  # 查询结果
    # value = ("4", "000", "bug", "133", "操作员", 2, "2023-07-03")
    value = ('急急急', '111', '急先锋', '新能源汽车', '1111', '临时', '', '')
    s3 = "insert into owner VALUES" + str(value)
    # m.excute_sql('update worker set name="叶宇成风" where `name`="叶"')  # 更新语句
    # m.excute_sql('delete from worker where name="李四"')  # 删除语句
    # m.excute_sql('insert into worker VALUES("2", "qwert12345", "黄", "133", "操作员", 2, "2023-07-03")')  # 插入语句
    m.excute_sql(s3)
