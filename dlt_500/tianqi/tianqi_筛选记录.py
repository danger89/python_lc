import os

file = "./data/yc22095_数据2022-08-18.txt"
with open(file, 'r') as f:
    content = f.readlines()

filepath = './right_data_095.txt'
try:
    os.remove(filepath)
except:
    pass
fileInput = open(filepath, "a")

for i in content:
    if i.find("当前访问") >= 0 or i.find("===") >= 0 or (
            i.find("04") >= 0 and i.find("13") >= 0 and i.find("14") >= 0 and i.find("18") >= 0 and i.find(
            "20") >= 0 and i.find("28") >= 0):
        fileInput.write(f"{i.strip()}\n")