# import os
# os.environ['TDSDUMP'] = 'stdout'

import pymssql

conn = pymssql.connect(
    server='Mysql@localhost:3306',
    user='root',
    password='password',
    database='my_db',
    as_dict=True
)

try:
    cursor = conn.cursor()
    print("success")
    cursor.close()
    print("close")
except Exception as e:
    print("Error connecting to database:",e)

    
# print("test")