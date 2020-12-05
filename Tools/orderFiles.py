# -*- coding: utf-8 -*-

import os
import sys
import time


ret = []

def orderFiles(dirPath,startTime, endTime):
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
        if endTime >= temp["time"] >= startTime:
            print("open "+os.path.join(dirPath,temp["file"]))
            pass


if __name__ == "__main__":
    # dirPath = sys.argv[1]

    dirPath = "/Users/zhanglingyu/Library/Containers/com.tencent.qq/Data/Library/Caches/Images"
    startTime = 0
    
    startTime = float(input("请输入时间参数\n"))
    endTime = time.time()
    if len(sys.argv) > 2:
        endTime = float(sys.argv[2])
    if os.path.exists(dirPath):
        orderFiles(dirPath, startTime, endTime)
        # print("执行时间 %f" % (time.time()-startTime))
