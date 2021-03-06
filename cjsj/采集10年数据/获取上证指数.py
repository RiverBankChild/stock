'''
Created on 2019年12月5日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import jqdatasdk as jq
import time
from _datetime import datetime


#超参
ksrq='2009-11-05'
jsrq='2019-12-07'
 
#jqdata认证
jq.auth('13401179853','king179853')

#定义当前日期
d=time.strftime('%Y-%m-%d',time.localtime(time.time())) 
print(d)


#建立连接
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='xg2',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()

df1=jq.get_price('000001.XSHG', start_date=ksrq, end_date=jsrq, frequency='daily', fields=['open', 'close', 'high', 'low', 'volume'], skip_paused=True, fq='pre')
df1.reset_index(inplace=True,drop=False)
list=df1.values.tolist()
#插入数据 
for j in range(len(list)):
        sql = "INSERT INTO szzs (date,open,close,high,low,volume) VALUES ( '%s', %.2f ,%.2f ,%.2f ,%.2f,%.2f  )"
        date = datetime.date(datetime.fromtimestamp(list[j][0].timestamp()))        
        data = (date,list[j][1],list[j][2],list[j][3],list[j][4],list[j][5])
        cursor.execute(sql % data)
        connect.commit()
print('上证指数历史数据获取完成')

# 关闭连接
cursor.close()
connect.close()