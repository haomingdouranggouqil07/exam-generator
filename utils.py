import os
from datetime import datetime  

def getDatePath():

    now = datetime.now()  
    
    # 格式化日期为 YYYY-MM-DD  
    formatted_date = now.strftime('%Y-%m-%d')
    return formatted_date

def getOrGeneratePathByDay(base):
    day = getDatePath()
    directory_path = "{}/{}".format(base, day)
    # 检查目录是否存在  
    if not os.path.exists(directory_path):  
        # 如果目录不存在，则创建目录  
        os.makedirs(directory_path)  
        print(f"Directory '{directory_path}' created")  

    return directory_path
    
