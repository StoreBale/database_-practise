# import os
# os.environ['TDSDUMP'] = 'stdout'

# import pymysql

# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='password',
#     database='my_db',
# )

# try:
#     cursor = conn.cursor()
#     print("success")
#     cursor.close()
#     print("close")
# except Exception as e:
#     print("Error connecting to database:",e)


import mysql.connector
import pandas as pd  # 用於創建表格
import random



def connect(seed):
  # 连接到MySQL数据库
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="my_db",
    auth_plugin='mysql_native_password'
  )

  # 创建一个游标对象
  mycursor = mydb.cursor()

  # # 插入資料的 SQL 語句
  # insert_query = 'INSERT INTO exam (english, chinese) VALUES (%s, %s)'

  # # 插入每一筆資料
  # for item in seed:
  #   mycursor.execute(insert_query, item)

  # # 提交事務
  # mydb.commit()


  # 执行SQL查询
  mycursor.execute("SELECT * FROM exam")

  # 获取查询结果
  result = mycursor.fetchall()

  # 打印查询结果
  # for row in result:
  #   print(row)

  # 关闭游标和数据库连接
  mycursor.close()
  mydb.close()

  return result

# print("test")

def read_txt_to_array(file_path):
  # 步驟 1: 讀取 TXT 檔案
  with open(file_path, 'r') as file:
    # 步驟 2: 逐行讀取並拆分為二維陣列
    data = [line.strip().split(',') for line in file.readlines()]
    
  return data

def display_table(data):
  # 步驟 3: 使用 pandas 顯示表格
  df = pd.DataFrame(data)
  print(df)

def exam_st(seed):
  random.shuffle(seed)
  total = len(seed)
  sum = 0
  for question, answer in seed:
    sum += 1

    print(f"目前第{sum}/{total}題")
    user_answer = input(question + " (請輸入你的答案)：")
    
    # 檢查答案
    if user_answer.strip() == answer:
      print("正確！")
    elif user_answer.strip() == 'exit':
      break
    else:
      print(f"錯誤，正確答案是：{answer}")

  print("結束")    
    


# 使用範例
file_path = 'seed_db.txt'  # 替換成你的檔案路徑
array_data = read_txt_to_array(file_path)
# display_table(array_data)
# print(array_data)
get_seed = connect(array_data)
# df = pd.DataFrame(get_seed)
# print(df)
exam_st(get_seed)
