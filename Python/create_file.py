import os

path = r'C:\Users\xuguokai\Desktop\kernel'
path_list = next(os.walk(path))[1]
print(path_list)

#新增文件夹
def creat_dir():
    for i in path_list[1:]:
        new_path = "./result/"+ i
        if not os.path.exists(new_path):
            os.makedirs(new_path)

#删除文件夹
def rm_dir():
    for i in path_list[1:]:
        new_path = "./result/"+ i
        if os.path.exists(new_path):
            #删除该文件夹里面的东西
            if os.path.getsize(new_path):
                for file in os.listdir(new_path)[0:]:
                    os.remove(new_path+'/'+file)
        os.rmdir(new_path)

rm_dir()


    