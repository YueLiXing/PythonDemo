class Solution:
    def beautifulArray(self, N):
        memo = {1: [1]}

        def f(N):
            if N not in memo:
                odds = f((N+1)//2)
                evens = f(N//2)
                memo[N] = [2*x-1 for x in odds] + [2*x for x in evens]
            print(memo)
            return memo[N]
        return f(N)


# 在[1..N] 中有(N + 1) / 2 个奇数和 N / 2 个偶数。
# 我们将其分治成两个子问题，其中一个为不超过(N + 1) / 2 的整数，
# 并映射到所有的奇数；另一个为不超过 N / 2 的整数，并映射到所有的偶数。


print(Solution().beautifulArray(5))
