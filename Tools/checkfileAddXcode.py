import os
import sys

unAddFileDir = {}

        

def getAllFileAndPath(path, xcodeFileText):
    for fileName in os.listdir(path):
        filePath = os.path.join(path, fileName)
        # print(os.path.abspath(filePath))
        if os.path.isdir(filePath):
            if "Assets.xcassets" == fileName:
                continue
            elif ".framework" in fileName or ".bundle" in fileName:
                checkFile(fileName, xcodeFileText, filePath)
                continue
            else:
                getAllFileAndPath(filePath, xcodeFileText)
            
        elif os.path.isfile(filePath):
            if fileName == ".DS_Store":
                continue
            checkFile(fileName, xcodeFileText, filePath)
        else:
            # print("不是文件夹也不是文件")
            pass


def checkFile(fileName, xcodeFileText, filePath):
    if fileName not in xcodeFileText:
        # print(fileName, filePath)
        unAddFileDir[filePath] = fileName
        # unAddFileArr.append(fileName)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        xcodeFilePath = sys.argv[1]
        checkDirPath = sys.argv[2]
        if os.path.isfile(xcodeFilePath):
            xcodeFileTxt = open(xcodeFilePath).read()
            getAllFileAndPath(checkDirPath, xcodeFileTxt)
            print("result:")
            tempKeys = []
            for k in unAddFileDir:
                tempKeys.append(k)
            tempKeys.sort()
            for key in tempKeys:
                print(unAddFileDir[key], key)
        else:
            print("xcodefile 路径错误")
    else:
        print("参数错误 eg:\npython3 checkfileAddXcode.py ../../../Project/NewGeXing/NewGeXing.xcodeproj/project.pbxproj ../../../Project/NewGeXing/NewGeXing")
