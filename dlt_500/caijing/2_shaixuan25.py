import os
file = "./yc/yc22098_数据2022-08-25.txt"
with open(file, 'r') as f:
    content = f.readlines()

filepath = './shaixuan/25shaixuan_data_098.txt'
try:
    os.remove(filepath)
except:
    pass
fileInput = open(filepath, "a")
for i in content:
    #if i.find("当前访问") >= 0 or i.find("===") >= 0
    # if (i.find("25码") >= 0 or i.find("20码") >= 0) or i.find("===") >= 0:
    if i.find("25码") >= 0:
        fileInput.write(f"{i.replace('：', ' ').strip()}\n")