class Solution:
    # 递归解决
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        flag = K % 2
        if flag == 1:
            return self.kthGrammar(N - 1, (K - 1) / 2 + 1)
        else:
            return 1 if self.kthGrammar(N - 1, K // 2) == 0 else 0

    # 当然也可以用迭代解决


# print("kthGrammar:", Solution().kthGrammar(5, 9))  # 1
# print("kthGrammar:", Solution().kthGrammar(5, 8))  # 1

# print("kthGrammar:", Solution().kthGrammar(5, 1))  # 0
# print("kthGrammar:", Solution().kthGrammar(5, 2))  # 1

# print("kthGrammar:", Solution().kthGrammar(30, 3))  # 0
# print("kthGrammar:", Solution().kthGrammar(30, 4))  # 1

# for tempK in [1, 2, 3, 4, 5, 6]:
#     print()
#     print(Solution().kthGrammar(n + 1, tempK + 1))
#     print(Solution().kthGrammar(n - 1 + 1, tempK // 2 + tempK % 2 + 1))
