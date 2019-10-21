# -*- coding: utf-8 -*-

import sys
import os

class HandleImage(object):
    def handleDir(self, dirPath:str):
        saveDir = dirPath+"handle"

        if os.path.exists(saveDir):
            os.rmdir(saveDir)
        os.mkdir(saveDir)

        for fileName in os.listdir(dirPath):
            filePath = os.path.join(dirPath, fileName)
            if ".png" in fileName:
                toFileName = os.path.join(saveDir, fileName)
                print(os.path.abspath(filePath), toFileName)
            
    def handleAndSave(self, imageFilePath, savePath):
        im = Image.open(imageFilePath)
        print(im)
        print(im.format, im.size, im.mode)



if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) > 1:
        dirPath = sys.argv[1]
        if os.path.exists(dirPath):
            HandleImage().handleDir(dirPath)
        else:
            print("图片目录不存在 %s" % dirPath)
    else:
        print("参数错误")
