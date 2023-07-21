import os
import time 
import multiprocessing
from func import *


path = "test/"
dir = os.listdir(path)






if __name__ == '__main__':
    dics = {}
    filename = []
    pool = multiprocessing.Pool(multiprocessing.cpu_count()) # 全部进程执行 multiprocessing.cpu_count()
    start_time = time.time()
    
    for file in dir:
        pool.apply_async(func=count,args=(path + file,file.split('.')[0]))
        #dics = count(path + file,file.split('.')[0])
    pool.close()
    pool.join()
    end_time = time.time()
    print("耗时: {:.4f}秒".format(end_time - start_time))
#print(dics.keys())



