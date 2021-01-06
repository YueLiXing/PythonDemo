# -*- coding: utf-8 -*-
# 检查文件夹下所有有 XMLocalizedString 的代码行

import os
import sys
import time

class Tools:
    # def __init__(self, x):
    #     self.val = x
    #     self.left = None
    #     self.right = None

    def getAllXMLocalizedString(self, filePath) -> [str]:
        """
        docstring
        """
        allfileName = []
        def fileHandle(filePath, allLine: [str]):
            with open(filePath, mode='r') as file:
                allLines = file.readlines()
                for tempLine in allLines:
                    if 'XMLocalizedString' in tempLine:
                        tempLine = tempLine.strip() # 去掉前后多余的空格和换行
                        allLine.append(tempLine)
                        
        self.getAllFileAndPath(filePath, fileHandle, allfileName)
        return allfileName

    def getAllFileAndPath(self, path, fileHandle, result):
        # print("checkDir:"+path)
        allNeedToDealDirs = [path]
        while len(allNeedToDealDirs) > 0:
            currentDir = allNeedToDealDirs.pop()
            for fileName in os.listdir(currentDir):        
                filePath = os.path.join(path, fileName)
                
                if os.path.isdir(filePath):
                    allNeedToDealDirs.append(filePath)
                elif os.path.isfile(filePath):
                    # temp = allfileName.get(fileName)
                    if fileName == ".DS_Store":
                        continue
                    if fileName.endswith('.m'):
                        fileHandle(filePath, result)



result = Tools().getAllXMLocalizedString('/Users/yuelixing/Documents/workspace/mishop-ios/MiShop/MiShop/Native/Order/Detail')
for temp in result:
    print(temp)