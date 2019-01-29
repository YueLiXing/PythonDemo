# 978. 最长湍流子数组 
# 当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：

# 若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
# 或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
# 也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。
# 返回 A 的最大湍流子数组的长度

class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        ans = 1
        anchor = 0
        cmp = lambda a,b: 1 if a > b else -1 if a < b else 0
        for i in range(1, N):
            
            c = cmp(A[i-1], A[i])
            if i == N-1 or c * cmp(A[i], A[i+1]) != -1:
                if c != 0:
                    ans = max(ans, i - anchor + 1)
                anchor = i
        return ans


# print(Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
# print(Solution().maxTurbulenceSize([2,0,2,4,2,5,0,1,2,3]))
print(Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))  # 5

