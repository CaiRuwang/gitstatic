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

    # SQL 插入语句
    sql = 'INSERT INTO  work_code_static(project_name,userName,commitNums,addLines,subLines,fristCommit,lastCommit,model_name)values(%s,%s,%s,%s,%s,%s,%s,%s)'


    try:
        # 执行sql语句
        cursor.executemany(sql,param)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        print e
        # Rollback in case there is any error
        db.rollback()




if  __name__ == '__main__':
    dbParams=[]
    dbParams.append(('lbdq', u'1', u'yangfeng <abaneo@qq.com>', u'156', u'167402', u'9091', u'August 01, 2017 18:27', u'January 22, 2018 14:29', 'ebs-frame'))
    dbParams.append(('lbdq', 'yang33feng <abaneo@qq.com>', '156', '167402', '9091', 'aaa', 'ddd','ebs-frame'))
    connection(dbParams)