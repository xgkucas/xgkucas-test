import time 
import multiprocessing
from func import *



if __name__ == '__main__':
    #dics = {}
    pool = multiprocessing.Pool(multiprocessing.cpu_count()) # 全部进程执行 multiprocessing.cpu_count()
    start_time = time.time()

    #确定文件路径  './' 当前目录下
    filename = find_C_H("./")
    for i in filename:
        print(i)
    
    for file in filename:
        pool.apply_async(func=count,args=(file[0],file[1]))

    # for file in dir:
    #     pool.apply_async(func=count,args=(path + file,file.split('.')[0]))
        #dics = count(path + file,file.split('.')[0])
    pool.close()
    pool.join()
    end_time = time.time()
    print("耗时: {:.4f}秒".format(end_time - start_time))




