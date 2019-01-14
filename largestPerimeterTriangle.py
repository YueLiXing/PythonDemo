# 976. 三角形的最大周长  显示英文描述
# 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
# 如果不能形成任何面积不为零的三角形，返回 0。

# https: // leetcode-cn.com/contest/weekly-contest-119/problems/largest-perimeter-triangle/


class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 三角形，任意两边之和大于第三边，任意两边之差小于第三边
        A.sort(reverse=True)
        print(A)
        return 0

test = Solution()

print(test.largestPerimeter([3, 2, 3, 4]))
print(test.largestPerimeter([3,6,2,3]))
