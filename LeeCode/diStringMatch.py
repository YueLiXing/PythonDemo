class Solution:
    def diStringMatch(self, S: str) -> [int]:
        n = len(S)
        target = []
        cache = [i for i in range(n+1)]
        for c in S:
            if c is 'I':
                target.append(cache.pop(0))
            else:
                target.append(cache.pop())
        target.append(cache.pop())
        return target


print(Solution().diStringMatch("IDID"))
