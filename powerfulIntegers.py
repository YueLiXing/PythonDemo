class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        ret = []
        i = 0
        j = 0
        while True:
            temp = x**i+y**j
            # print(i,j,temp)
            if temp <= bound:
                if temp not in ret:
                    ret.append(temp)
                if x <= 1 and y <= 1:
                    break
                elif y <= 1:
                    i += 1
                    j = 0
                else:
                    j += 1
            else:
                if x**i+1 > bound or x <= 1:
                    break
                else:
                    i += 1
                    j = 0
        return ret
        

print(Solution().powerfulIntegers(1, 1, 2))
# print(Solution().powerfulIntegers(2, 3, 10))
