# -*- coding: utf-8 -*-

import os
import sys

allCount = 0
countPng = 0

def getAllFileAndPath(path):
    global allCount,countPng
    # print("checkDir:"+path)
    for fileName in os.listdir(path):
        filePath = os.path.join(path, fileName)
        # print(os.path.abspath(filePath))
        if os.path.isdir(filePath):
            getAllFileAndPath(filePath)
        elif os.path.isfile(filePath):
            if fileName == ".DS_Store":
                continue
            # if ".m" in fileName or ".h" in fileName:
            if ".png" in fileName:
                countPng += 1
            allCount += 1
        else:
            # print("不是文件夹也不是文件")
            pass
        # print("%s isfile:%d" % (fileName, os.path.isfile(filePath)))



if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv[1])
        dirPath = sys.argv[1]
        if os.path.exists(dirPath):
            # startTime = time.time()
            getAllFileAndPath(dirPath)
            print("allcount:",allCount)
            print("png:",countPng)
            # print("执行时间 %f" % (time.time()-startTime))
        else:
            print("请输入正确的文件夹路径")
    else:
        print("请输入需要检查的文件夹路径")
        print("eg:  python3 checkDulFilename.py Images")
