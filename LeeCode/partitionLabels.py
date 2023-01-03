class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = 0
        tempSet = set()
        flag = True // 增长阶段
        result = []
        for tempC in s:
            if flag:
                oldCount = len(tempSet)
                tempSet.add(tempC)
                newCount = len(tempSet)
                if oldcount == newcount:
                    count += 1
                else:
            if tempC not in tempSet:
                if flag:
                    tempSet.add(tempC)
                    count += 1
                    len(tempSet)
                else:
                    result.append(count)
                    count = 0
                    tempSet.clear()
                pass
            else:
                count += 1
        return result

