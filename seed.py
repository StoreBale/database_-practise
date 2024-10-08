import pandas as pd  # 用於創建表格

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

# 使用範例
file_path = 'seed_db.txt'  # 替換成你的檔案路徑
array_data = read_txt_to_array(file_path)
display_table(array_data)
