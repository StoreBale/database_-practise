import psycopg2
from psycopg2 import sql


try:
    # 建立資料庫連接
    connection = psycopg2.connect(
        dbname="postgresdb",  # 資料庫名稱
        user="postgres",    # 用戶名
        password="123456",  # 密碼
        host="localhost",   # 主機
        port="5432"         # 端口
    )

    # 創建一個游標對象
    cursor = connection.cursor()
    
    # 執行一個SQL查詢
    cursor.execute("SELECT version();")
    
    # 獲取結果
    db_version = cursor.fetchone()
    print(f"PostgreSQL版本: {db_version}")

except Exception as error:
    print(f"發生錯誤：{error}")
finally:
    # 確保關閉連接
    if 'connection' in locals():
        cursor.close()
        connection.close()
        print("資料庫連接已關閉。")


