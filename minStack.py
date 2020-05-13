# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.data = []

#     def push(self, x: int) -> None:
#         if len(self.data) == 0:
#             self.data.append([x, x])
#         else:
#             self.data.append([x, min(x, self.data[-1][1])])

#     def pop(self) -> None:
#         self.data.pop()

#     def top(self) -> int:
#         return self.data[-1][0]

#     def getMin(self) -> int:
#         return self.data[-1][1]
#         # Your MinStack object will be instantiated and called as such:
#         # obj = MinStack()
#         # obj.push(x)
#         # obj.pop()
#         # param_3 = obj.top()
#         # param_4 = obj.getMin()


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.minData = []
        self.count = 0

    def push(self, x: int) -> None:
        self.data.append(x)
        if self.count == 0:
            self.minData.append(x)
        else:
            self.minData.append(min(x, self.minData[-1]))
        self.count += 1

    def pop(self) -> None:
        self.data.pop()
        self.minData.pop()
        self.count -= 1

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.minData[-1]
        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()

# 最小栈
s = MinStack()
s.push(-2)
s.push(0)
