# -*- coding: utf-8 -*-

import os
import sys

allCount = 0


def getAllFileAndPath(path):
    global allCount
    for fileName in os.listdir(path):
        filePath = os.path.join(path, fileName)

        if os.path.isdir(filePath):
            getAllFileAndPath(filePath)
        elif os.path.isfile(filePath):
            if fileName == ".DS_Store":
                continue

            if ".png" in fileName or ".jpg" in fileName or ".jpeg" in fileName:
                allCount += 1
                file = open(filePath, mode="ab+")
                file.write("a")
                file.close()
            
        else:
            # print("不是文件夹也不是文件")
            pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        dirPath = sys.argv[1]
        if os.path.exists(dirPath):
            # startTime = time.time()
            getAllFileAndPath(dirPath)
            print("修改文件数")
            print(allCount)
            print("Done")
            # print("执行时间 %f" % (time.time()-startTime))
        else:
            print("请输入正确的文件夹路径")
    else:
        print("请输入需要检查的文件夹路径")
        print("eg:  python3 changePicsMd5.py Images")
