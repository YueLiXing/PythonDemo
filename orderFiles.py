# -*- coding: utf-8 -*-

import os
import sys


ret = []

def orderFiles(dirPath,t=0):
    for fileName in os.listdir(dirPath):
        filePath = os.path.join(dirPath, fileName)
        
        if os.path.isfile(filePath):
            # print(os.path.getmtime(filePath))
            ret.append({
                "time": os.path.getmtime(filePath),
                "file": fileName
            })
    ret.sort(key=lambda obj: obj["time"])
    # print(ret)
    for temp in ret:
        if temp["time"] > t:
            print("open "+os.path.join(dirPath,temp["file"]))
            pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv)
        # dirPath = sys.argv[1]
        
        # t = 0
        # if len(sys.argv) > 2:
        #     t = float(sys.argv[2])
        # if os.path.exists(dirPath):
        #     # startTime = time.time()
        #     orderFiles(dirPath,t)
        #     # print("执行时间 %f" % (time.time()-startTime))
        # else:
        #     print("请输入正确的文件夹路径")
        #     dirPath = sys.argv[1]

        dirPath = "/Users/zhanglingyu/Library/Containers/com.tencent.qq/Data/Library/Caches/Images"
        t = 0
        if len(sys.argv) > 1:
            t = float(sys.argv[1])
        if os.path.exists(dirPath):
            # startTime = time.time()
            orderFiles(dirPath, t)
            # print("执行时间 %f" % (time.time()-startTime))
        else:
            print("请输入正确的文件夹路径")
    else:
        print("请输入需要检查的文件夹路径")
