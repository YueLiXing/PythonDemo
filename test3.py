# 超时，可惜啊
class Solution:
    def minimumTime(self, n: int, relations: [[int]], time: [int]) -> int:
        tempArr = []
        doneC = set()
        for index in range(1, n+1):
            pre = []
            for tempL in relations:
                if tempL[1] == index:
                    pre.append(tempL[0])
            tempArr.append({
                'n': index,
                'pre': pre,  # 先决条件
                'needTime': time[index-1],  # 所需时间
                'finish': False,  # 是否完成
                'count': 0
            })
            # print(tempArr[-1])
        result = 0
        while True:

            ing = []
            index = 0
            finish = []
            for tempC in tempArr:
                index += 1
                if tempC['finish']:
                    continue
                else:
                    pre = tempC['pre']
                    canLearn = False
                    if len(pre) == 0:
                        canLearn = True
                    else:
                        c = True
                        for tempP in pre:
                            if tempArr[tempP-1]['n'] not in doneC or tempP in ing:
                                c = False
                        canLearn = c
                    if canLearn is False:
                        continue
                    if index in ing:
                        continue
                    else:
                        tempC['count'] += 1
                        ing.append(index)
                        if tempC['count'] == tempC['needTime']:
                            tempC['finish'] = True
                            finish.append(tempC)
            for temp in finish:
                # tempArr.remove(temp)
                doneC.add(temp['n'])
            # print(ing)
            result += 1
            c = False
            for tempC in tempArr:
                if tempC['finish'] is False:
                    c = True
            if c is False:
                break
        return result


# 输入：n = 3, relations = [[1,3],[2,3]], time = [3,2,5]
# 输出 8
print(Solution().minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5]))

# 5
# [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]]
# [1, 2, 3, 4, 5]
# print(Solution().minimumTime(
#     5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5]))
