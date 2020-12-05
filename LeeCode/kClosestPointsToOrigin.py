# 973. 最接近原点的 K 个点  显示英文描述
# 用户通过次数 256
# 用户尝试次数 277
# 通过次数 265
# 提交次数 435
# 题目难度 Easy
# 我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点(0, 0) 最近的点。
# （这里，平面上两点之间的距离是欧几里德距离。）

# https: // leetcode-cn.com/contest/weekly-contest-119/problems/k-closest-points-to-origin/


class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        allRet = []
        for index in range(len(points)):
            temp = points[index]
            length = pow(temp[0],2)+pow(temp[1],2)
            allRet.append({
                "length":length,
                "point": temp
            })
        # print(allRet)
        array = allRet
        # 插入法取前K个小数
        minArray = array[0:K]
        minArray.sort(key=lambda obj: obj["length"])
        for index in range(K,len(array)):
            if array[index]["length"] < minArray[-1]["length"]:
                for minIndex in range(len(minArray)):
                    if array[index]["length"] < minArray[minIndex]["length"]:
                        minArray.insert(minIndex, array[index])
                        break
                minArray.pop()
        ret = []
        for index in range(len(minArray)):
            ret.append(minArray[index]["point"])
        return ret

test = Solution()

print(test.kClosest([[1, 3], [-2, 2],[4,4]], 2))
