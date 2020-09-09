import os


class Solution:
    def loopupFile(self, dirPath: str, fileType: str, fileArray: [str]):
        if os.path.isdir(dirPath) is False:
            return
        for fileName in os.listdir(dirPath):
            fullPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fullPath):
                self.loopupFile(fullPath, fileType, fileArray)
            elif os.path.isfile(fullPath):
                if fullPath.endswith(fileType):
                    fileArray.append(fullPath)
        return fileArray


# Solution().loopupFile("/Users/zhanglingyu", "m")
temp = Solution().loopupFile("/Users/zhanglingyu/Documents/Project/NewGeXing", "m", [])
print(temp)
