class Solution:
    def buildArray(self, target: [int], n: int) -> [str]:
        push = "Push"
        pop = "Pop"
        result = []
        tempIndex = 0
        lenTarget = target[-1]+1
        for tempI in range(1, n+1):
            # print(result, tempI)
            if lenTarget > tempIndex:
                result.append(push)
                if tempI == target[tempIndex]:
                    tempIndex += 1
                else:
                    result.append(pop)
            else:
                break
        return result


Solution().buildArray([1, 3], 3)
