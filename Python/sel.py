import os
import threading
from func import *

path = "test/"
dir = os.listdir(path)

threads = []     #定义一个线程池
t1=threading.Thread(target=吃饭)
threads.append(t1)    #把t1线程装到线程池里
t2=threading.Thread(target=看电视)
threads.append(t2)    #把t2线程装到线程池里




if __name__ == '__main__':
    dics = {}
    if(os.path.isfile("CorrectWord.txt")):
        #os.remove() function to remove the file
        os.remove("CorrectWord.txt")
    # with open('CorrectWord.txt', 'a+', encoding='utf-8') as f:
    #         tplt = "{:<8}\t{:<13}\t{:<15}\n"
    #         f.write(tplt.format('行','原单词', '改正后'))
    
    for file in dir:
        if(os.path.isfile('%s.txt'%file.split('.')[0])):
        #os.remove() function to remove the file
            os.remove('%s.txt'%file.split('.')[0])
        with open('%s.txt'%file.split('.')[0], 'a+', encoding='utf-8') as f:
            tplt = "{:<8}\t{:<13}\t{:<15}\n"
            f.write(tplt.format('行','原单词', '改正后'))
        dics = count(path + file,file.split('.')[0])
#print(dics.keys())



