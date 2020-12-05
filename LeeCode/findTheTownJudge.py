class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        cache = set(range(1,N+1))
        for tempArr in trust:
            t = tempArr[0]
            if t in cache:
                cache.remove(t)
        if len(cache) != 1:
            return -1
        judge = cache.pop()
        cache.clear()
        for i in range(1,N+1):
            if i != judge:
                cache.add(i)
        for tempArr in trust:
            a = tempArr[0]
            t = tempArr[1]
            if t == judge and a in cache:
                cache.remove(a)
        if len(cache) == 0:
            return judge
        else:
            return -1
        

Solution().findJudge(N=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])
