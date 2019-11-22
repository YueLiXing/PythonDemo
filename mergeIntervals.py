class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        if len(intervals) == 0:
            return []
        ret = []
        index = 0
        l = len(intervals)
        intervals = sorted(intervals, key=lambda a: a[0], reverse=False)
        # print(intervals)
        ret.append(intervals[0])
        for index in range(1,l):
            currentRange = intervals[index]
            lastRange = ret[-1]
            if lastRange[1] < currentRange[0]:
                ret.append(currentRange)
            else:
                ret.pop()
                ret.append([min(lastRange[0], currentRange[0]), max(currentRange[1], lastRange[1])])
        return ret


print(Solution().merge([[1, 4], [2, 3]]))
# print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
