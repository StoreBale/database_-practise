import psycopg2
from psycopg2 import sql

def connect_to_postgres():
    connection = None  # 初始化 connection 變數
    try:
        # 連接資料庫
        connection = psycopg2.connect(
            user="postgres-db",                    # 預設用戶名
            password="123456",        # 在 Docker 運行時設置的密碼
            host="localhost",                   # 容器運行於本地主機
            port="5432",                        # PostgreSQL 預設端口
            database="postgres-db"                 # 預設資料庫名稱
        )

        # 創建游標
        cursor = connection.cursor()
        print("PostgreSQL 連接成功")

        # 執行一個簡單的查詢
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"PostgreSQL 版本: {db_version}")

        # 返回資料庫中的表
        cursor.execute("""SELECT table_name FROM information_schema.tables
                          WHERE table_schema = 'public';""")
        tables = cursor.fetchall()
        print(f"Public schema 中的表: {tables}")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"連接出錯: {error}")
    finally:
        # 關閉游標與連接
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL 連接已關閉")

# 呼叫函數來執行連接
connect_to_postgres()
