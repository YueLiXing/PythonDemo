class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        ret = []
        flag = False
        for tempArr in queries:
            val = tempArr[0]
            index = tempArr[1]

            if flag == False:
                A[index] = A[index]+val
                buf = 0
                for temp in A:
                    if temp % 2 == 0:
                        buf += temp
                ret.append(buf)
                flag = True
            else:
                buf = ret[-1]
                if A[index]%2 == 0:
                    buf -= A[index]

                if (A[index]+val)%2 == 0:
                    buf += A[index]+val

                ret.append(buf)
                A[index] = A[index]+val
        return ret


print(Solution().sumEvenAfterQueries([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]]))
# [8,6,2,4]
