import os

# 0.获取用户要Copy 的文件夹的名字。
odlFileName = input("请输出要Cpoy的文件夹：")

# 1.创建一个文件夹。
newFileName = "C:\\Users\田海龙\\Desktop\\PyTest\\"+odlFileName+"-副本"
os.mkdir(newFileName)
# 2.获取源文件夹中所有文件的名字。
fileNames = os.listdir("C:\\Users\田海龙\\Desktop\\PyTest\\"+odlFileName)
print(fileNames)

# 3.使用多进程的方式将文件夹中的所有文件，COPY至新文件夹中。