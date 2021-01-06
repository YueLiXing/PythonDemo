# -*- coding: utf-8 -*-
# 移动文件，检查文件结构
# 未完成

import os
import sys
import time
import re


class CheckTool:
    def __init__(self):
        super().__init__()
        self.currentDIr = os.path.curdir

    def run(self):
        readmePath = os.path.join(self.currentDIr, 'README.md')
        toolDir = os.path.join(self.currentDIr, 'Tools')
        leecodeDir = os.path.join(self.currentDIr, 'LeeCode')
        if os.path.exists(toolDir) is False:
            os.mkdir(toolDir)
        if os.path.exists(leecodeDir) is False:
            os.mkdir(leecodeDir)
        if os.path.exists(readmePath):
            with open(readmePath, 'r', encoding='utf-8') as target:
                lines = target.readlines()

                toolArr = []
                leecodeArr = []
                # 0:未开始  1:tool阶段  2:leecode阶段
                state = 0
                for tempLine in lines:
                    if '写着玩的小脚本' in tempLine:
                        state = 1
                        print('进入tool 阶段')
                        continue
                    elif '力扣网站' in tempLine:
                        print('进入leecode 阶段')
                        continue
                    if state == 0:
                        continue
                    elif state == 1:
                        print(tempLine)
                        print(re.match(r'py', tempLine))
                        break
        else:
            print('README.md 文件不见了！！！')
    pass


CheckTool().run()
# allfileName = {}
# allSkip = ""


# def getAllFileAndPath(path):
#     # print("checkDir:"+path)
#     for fileName in os.listdir(path):
#         filePath = os.path.join(path, fileName)
#         # print(os.path.abspath(filePath))
#         if os.path.isdir(filePath):
#             getAllFileAndPath(filePath)
#         elif os.path.isfile(filePath):
#             temp = allfileName.get(fileName)
#             if fileName == ".DS_Store":
#                 continue
#             if temp is None:
#                 allfileName[fileName] = [filePath]
#             else:
#                 temp.append(filePath)
#                 allfileName[fileName] = temp
#         else:
#             # print("不是文件夹也不是文件")
#             pass
#         # print("%s isfile:%d" % (fileName, os.path.isfile(filePath)))


# def checkResult():
#     global allSkip
#     flag = False
#     print("Result：")
#     for (key, value) in allfileName.items():
#         if len(value) > 1:
#             frameWorkCheck = False
#             frameWorkDir = None
#             for temp in value:
#                 if ".framework" in temp:
#                     if frameWorkDir is None:
#                         frameWorkDir = temp[0:temp.index(".framework")]
#                     elif frameWorkDir == temp[0:temp.index(".framework")]:
#                         frameWorkCheck = True
#                     else:
#                         frameWorkCheck = False
#                 else:
#                     frameWorkCheck = False
#                     break
#             if frameWorkCheck == False:
#                 flag = True
#                 print(key)
#                 for temp in value:
#                     print(temp)
#             else:
#                 allSkip += key
#                 allSkip += "\n"
#                 for temp in value:
#                     allSkip += temp
#                     allSkip += "\n"
#     if flag == False:
#         print("很高兴，没有重复的文件")
#     if len(allSkip) > 0:
#         print("\n\n\n下面是默认为不重复的内容，请自行检查，酌情处理")
#         print(allSkip)


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         print(sys.argv[1])
#         dirPath = sys.argv[1]
#         if os.path.exists(dirPath):
#             # startTime = time.time()
#             getAllFileAndPath(dirPath)
#             checkResult()
#             # print("执行时间 %f" % (time.time()-startTime))
#         else:
#             print("请输入正确的文件夹路径")
#     else:
#         print("请输入需要检查的文件夹路径")
#         print("eg:  python3 checkDulFilename.py Images")
