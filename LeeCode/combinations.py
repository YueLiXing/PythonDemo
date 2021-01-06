class Solution:
    def change(self,k,arr):
        index = 0
        while k > 0:
            arr[index] = k%2
            k = k//2
            index += 1
        if index < len(arr)-1:
            for i in range(index,len(arr)):
                arr[i] = 0
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]
        ret = []
        tempArr = []
        for i in range(n):
            tempArr.append(0)
        index = 2**k-1
        self.change(index,tempArr)
        while True:
            if tempArr.count(1) == k:
                bufA = []
                for i in range(len(tempArr)):
                    if tempArr[i] == 1:
                        bufA.append(i+1)
                ret.append(bufA)
            
            if index == 2**n:
                break

            index += 1
            for i in range(len(tempArr)):
                tempArr[i] = tempArr[i]+1
                if tempArr[i] == 2:
                    tempArr[i] = 0
                else:
                    break

        return ret


print(Solution().combine(4, 2))
print(Solution().combine(2, 2))
