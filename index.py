import csv, json, requests
import pymysql

conn = pymysql.connect(host="localhost", user="root", passwd="root", db='mz_shop', charset='utf8', port=3306)


#创建游标
cursor = conn.cursor()
cursor.execute("select uid from sys_user where is_del=1")
row_all = cursor.fetchall()  #获取所有数据，获取后游标会向下移动到末尾
#关闭游标
cursor.close()
#关闭连接
conn.close()


file = open('a.csv', 'a', newline='')
# 写入
data=[]
data.append(('uid','用户名'))
for i in  row_all:
    data.append(i)
writerCsv = csv.writer(file)
for i in data:
    writerCsv.writerow(i)
file.close()


file = open('a.csv', 'r')
readFile = csv.reader(file)
# 读取csv
for row in readFile:
    print(row)
file.close()
