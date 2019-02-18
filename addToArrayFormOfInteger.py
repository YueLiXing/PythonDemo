class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        ret = []
        index = len(A)-1
        while K > 0 or index >= 0:
            if index >= 0:
                val = A[index]+K % 10
            else:
                val = K % 10
            K = K // 10
            if val >= 10:
                K += val // 10
                val = val %10
            ret.insert(0,val)
            index -= 1
        return ret


print(Solution().addToArrayForm([9, 9, 9, 9, 9, 9, 9, 9, 9, 9],1))
print(Solution().addToArrayForm([1, 2, 0, 0], 34))
