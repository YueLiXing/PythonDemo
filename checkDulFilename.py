# -*- coding: utf-8 -*-
# 检查文件夹下拥有重复文件名的文件

import os
import sys
import time

allfileName = {}

def getAllFileAndPath(path):
    # print("checkDir:"+path)
    for fileName in os.listdir(path):        
        filePath = os.path.join(path, fileName)
        # print(os.path.abspath(filePath))
        if os.path.isdir(filePath):
            getAllFileAndPath(filePath)
        elif os.path.isfile(filePath):
            temp = allfileName.get(fileName)
            if fileName == ".DS_Store":
                continue
            if temp is None:
                allfileName[fileName] = [filePath]
            else:
                temp.append(filePath)
                allfileName[fileName] = temp
        else:
            # print("不是文件夹也不是文件")
            pass
        # print("%s isfile:%d" % (fileName, os.path.isfile(filePath)))
  

def checkResult():
    flag = False
    print("Result：")
    for (key,value) in allfileName.items():
        if len(value)>1:
            print(key)
            flag = True
            for temp in value:
                print("%s" % (temp))
    if flag == False:
        print("很高兴，没有重复的文件")


if __name__ == "__main__":
    if len(sys.argv)>1:
        print(sys.argv[1])
        dirPath = sys.argv[1]
        if os.path.exists(dirPath):
            # startTime = time.time()
            getAllFileAndPath(dirPath)
            checkResult()
            # print("执行时间 %f" % (time.time()-startTime))
        else:
            print("请输入正确的文件夹路径")
        
    else:
        print("请输入需要检查的文件夹路径")
        print("eg:  python3 checkDulFilename.py Images")
