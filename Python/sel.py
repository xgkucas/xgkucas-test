import os
from func import *

path = "test/"
dir = os.listdir(path)



if __name__ == '__main__':
    dics = {}
    if(os.path.isfile("CorrectWord.txt")):
        #os.remove() function to remove the file
        os.remove("CorrectWord.txt")
    # with open('CorrectWord.txt', 'a+', encoding='utf-8') as f:
    #         tplt = "{:<8}\t{:<13}\t{:<15}\n"
    #         f.write(tplt.format('行','原单词', '改正后'))
    
    for file in dir:
        with open('%s.txt'%file.split('.')[0], 'a+', encoding='utf-8') as f:
            tplt = "{:<8}\t{:<13}\t{:<15}\n"
            f.write(tplt.format('行','原单词', '改正后'))
        dics = count(path + file)
#print(dics.keys())



