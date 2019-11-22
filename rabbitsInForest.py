class Solution:
    def numRabbits(self, answers: [int]) -> int:
        cacheDict = {}
        for tempAns in answers:
            t = tempAns+1
            key = str(t)
            if key not in cacheDict:
                cacheDict[key] = 1
            else:
                if cacheDict.get(key, 0)+1 > t:
                    pre = 0
                    while True:
                        newKey = str(pre)+"_"+str(t)

                        tempRet = cacheDict.get(newKey, 0)+1
                        if tempRet <= t:
                            cacheDict[newKey] = tempRet
                            break
                        pre += 1
                else:
                    cacheDict[key] = cacheDict.get(key, 0)+1
            # print(cacheDict, result)
        result = 0
        for key in cacheDict:
            result += int(key.split("_")[-1])
        return result


# print(Solution().numRabbits([1, 0, 1, 0, 0]))
print(Solution().numRabbits([0, 0, 1, 1, 1]))
