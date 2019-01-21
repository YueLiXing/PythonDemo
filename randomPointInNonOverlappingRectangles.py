# 497. 非重叠矩形中的随机点
# 给定一个非重叠轴对齐矩形的列表 rects，写一个函数 pick 随机均匀地选取矩形覆盖的空间中的整数点。
# 提示：
# 整数点是具有整数坐标的点。
# 矩形周边上的点包含在矩形覆盖的空间中。
# 第 i 个矩形 rects[i] = [x1，y1，x2，y2]，其中[x1，y1] 是左下角的整数坐标，[x2，y2] 是右上角的整数坐标。
# 每个矩形的长度和宽度不超过 2000。
# 1 <= rects.length <= 100
# pick 以整数坐标数组[p_x, p_y] 的形式返回一个点。
# pick 最多被调用10000次。
import random

class Solution:

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.sumArea = 0
        self.areaSteps = []
        self.rects = rects
        for index in range(len(rects)):
            tempRect = rects[index]
            pointX = tempRect[0]
            pointY = tempRect[1]
            pointXr = tempRect[2]
            pointYr = tempRect[3]
            area = (pointXr-pointX+1)*(pointYr-pointY+1)
            # print(area,pointXr-pointX,pointYr-pointY)
            self.sumArea += area
            self.areaSteps.append(self.sumArea)
        
    def pick(self):
        """
        :rtype: List[int]
        """
        temp = random.randint(0,self.sumArea)
        tempRect = None
        if temp <= self.areaSteps[0]:
            tempRect = self.rects[0]
        else:
            for index in range(0,len(self.areaSteps)-1):
                currentValue = self.areaSteps[index]
                nextValue = self.areaSteps[index+1]
                if currentValue < temp and temp <= nextValue:
                    tempRect = self.rects[index+1]
                    break
        pointX = tempRect[0]
        pointY = tempRect[1]
        pointXr = tempRect[2]
        pointYr = tempRect[3]
        return [random.randint(pointX, pointXr), random.randint(pointY, pointYr)]

test = Solution([[82918473, -57180867, 82918476, -57180863], [83793579, 18088559, 83793580, 18088560],[66574245, 26243152, 66574246, 26243153], [72983930, 11921716, 72983934, 11921720]])
print(test.pick())
print(test.pick())
print(test.pick())
print(test.pick())
print(test.pick())
print(test.pick())
print(test.pick())
print(test.pick())
print(test.pick())
print(test.pick())
print(test.pick())
print(test.pick())
