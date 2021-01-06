class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        ret = []
        index = 0
        intervals.append(newInterval)
        l = len(intervals)
        intervals = sorted(intervals, key=lambda a: a[0], reverse=False)
        print(intervals)
        ret.append(intervals[0])
        for index in range(1, l):
            currentRange = intervals[index]
            lastRange = ret[-1]
            if lastRange[1] < currentRange[0]:
                ret.append(currentRange)
            else:
                ret.pop()
                ret.append([min(lastRange[0], currentRange[0]),
                            max(currentRange[1], lastRange[1])])
        return ret

    # def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
    #     if len(intervals) == 0:
    #         return [newInterval]
    #     ret = []
    #     start = newInterval[0]
    #     stop = newInterval[1]
    #     status = 0 # 0 未处理，1正在处理，2处理完成

    #     l = len(intervals)
    #     for index in range(len(intervals)):
    #         tempRange = intervals[index]
    #         tempB = tempRange[0]
    #         tempE = tempRange[1]
    #         if tempB > stop:
    #             if status != 2:
    #                 ret.append([start, stop])
    #                 status = 2
    #             ret.append(tempRange)
    #         elif tempE < start:
    #             ret.append(tempRange)
    #             if index+1 == l or status == 1:
    #                 ret.append([start, stop])
    #                 status = 2
    #         elif tempB <= start <= stop <= tempE and status != 2:
    #             status = 2
    #             ret.append(tempRange)
    #         else:
    #             if status == 0:
    #                 if start <= tempB <= stop:
    #                     status = 1
    #                     if tempE > stop:
    #                         ret.append([start, tempE])
    #                         status = 2
    #                     elif index+1 == l:
    #                         status = 2
    #                         ret.append([start, stop])
    #                 elif start <= tempE <= stop:
    #                     status = 1
    #                     start = min(tempB,start)
    #                     stop = max(tempE,stop)
    #                     if index+1 == l:
    #                         ret.append([start, stop])
    #             elif status == 1:
                    
    #                 if tempB > stop:
    #                     ret.append([start, tempE])
    #                     ret.append(tempRange)
    #                     status = 2
    #                 else:
    #                     if tempE > stop:
    #                         ret.append([start, tempE])
    #                         status = 2
    #                     elif index+1 == len(intervals):
    #                         ret.append([start,stop])
    #                         status = 2
    #     return ret


# print(Solution().insert([[1, 3], [6, 9]], [2, 5])) # [[1, 5], [6, 9]]

# [[1,2],[3,10],[12,16]]
# print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
# print(Solution().insert([[1, 5]], [2, 3]))
print(Solution().insert([], [1, 7]))
# print(Solution().insert([[1, 5], [9, 12]], [0, 4]))
# print(Solution().insert([[1, 3], [6, 9]], [2, 5]))
