# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    

class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        if len(A) == 0 or len(B) == 0:
            return []
        ret = []
        indexA = 0
        indexB = 0
        while len(A) > indexA and len(B) > indexB:
            a = A[indexA]
            b = B[indexB]
            if a.start > b.end:
                indexB += 1
            elif b.start > a.end:
                indexA += 1
            else:
                ret.append(Interval(max(a.start,b.start),min(a.end,b.end)))
                if a.end > b.end:
                    indexB += 1
                else:
                    indexA += 1

        return ret


tempA = []
for temp in [[0, 2], [5, 10], [13, 23], [24, 25]]:
    tempA.append(Interval(temp[0], temp[1]))
tempB = []
for temp in [[1, 5], [8, 12], [15, 24], [25, 26]]:
    tempB.append(Interval(temp[0], temp[1]))
tempA = Solution().intervalIntersection(tempA,tempB)
for t in tempA:
    print(t.start,t.end) 


