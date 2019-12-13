import collections


class Solution:
    def dailyTemperatures(self, T: [int]) -> [int]:
        target = []
        maxTemper = -1
        lenT = len(T)
        nearbyTempIndexDict = {}
        for index in range(lenT-1, -1, -1):
            tempT = T[index]
            if maxTemper < 0:
                target.append(0)
                # target.insert(0, 0)
                maxTemper = tempT
            else:
                if tempT >= maxTemper:
                    # target.insert(0, 0)
                    target.append(0)
                    maxTemper = tempT
                else:
                    tempJ = 30000
                    for tempTj in nearbyTempIndexDict:
                        j = nearbyTempIndexDict[tempTj]
                        if tempTj > tempT and j < tempJ:
                            tempJ = j
                    # target.insert(0, tempJ-index)
                    target.append(tempJ-index)
            nearbyTempIndexDict[tempT] = index
        target.reverse()
        return target
