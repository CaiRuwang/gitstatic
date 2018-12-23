# -*- coding: UTF-8 -*-
__Author__ = "vans"
__Date__ = '2018/11/21'

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb
def connection(param):
    # 打开数据库连接
    db = MySQLdb.connect(host="58.247.46.126",port=23306, user="stdv4_test", passwd="ebs@stdv4_test", db="stdv4_test", charset='utf8' )

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()



    # 使用execute方法执行SQL语句
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchone()

    print "Database version : %s " % data

    # 关闭数据库连接
    db.close()


if  __name__ == '__main__':

    connection('')