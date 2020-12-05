# 478. 在圆内随机生成点
# 给定圆的半径和圆心的 x、y 坐标，写一个在圆中产生均匀随机点的函数 randPoint 。

# 说明:

# 输入值和输出值都将是浮点数。
# 圆的半径和圆心的 x、y 坐标将作为参数传递给类的构造函数。
# 圆周上的点也认为是在圆中。
# randPoint 返回一个包含随机点的x坐标和y坐标的大小为2的数组。
import random
class Solution:

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.centerX = x_center
        self.centerY = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        # Math.random()*radius*2-radius
        tempX = random.random()*self.radius*2-self.radius
        tempY = random.random()*self.radius*2-self.radius
        if tempX*tempX+tempY*tempY <= self.radius*self.radius:
            return [self.centerX+tempX, self.centerY+tempY]
        else:
            return self.randPoint()


# Your Solution object will be instantiated and called as such:
obj = Solution(5, -10, 20)
print(obj.randPoint())
print(obj.randPoint())
print(obj.randPoint())
print(obj.randPoint())
