# import os
# os.environ['TDSDUMP'] = 'stdout'

import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    database='my_db',
)

try:
    cursor = conn.cursor()
    print("success")
    cursor.close()
    print("close")
except Exception as e:
    print("Error connecting to database:",e)


# import mysql.connector

# # 连接到MySQL数据库
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="password",
#   database="my_db",
#   auth_plugin='mysql_native_password'
# )

# # 创建一个游标对象
# mycursor = mydb.cursor()

# # 执行SQL查询
# mycursor.execute("SELECT * FROM users")

# # 获取查询结果
# result = mycursor.fetchall()

# # 打印查询结果
# for row in result:
#   print(row)

# # 关闭游标和数据库连接
# mycursor.close()
# mydb.close()
# print("test")