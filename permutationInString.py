class Solution:
    def getCharDict(self, s: str) -> dict:
        charDict1 = {}
        for c in s:
            if c in charDict1:
                charDict1[c] = charDict1[c]+1
            else:
                charDict1[c] = 1
        return charDict1

    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        charDict1 = self.getCharDict(s1)
        tempCharDict = self.getCharDict(s2[0:l1])
        for index2 in range(l2-l1+1):
            if index2 != 0:
                lastC = s2[index2-1]
                newC = s2[index2+l1-1]
                tempCharDict[lastC] = tempCharDict[lastC]-1
                if tempCharDict[lastC] == 0:
                    del tempCharDict[lastC]
                if newC in tempCharDict:
                    tempCharDict[newC] = tempCharDict[newC]+1
                else:
                    tempCharDict[newC] = 1
            # print(tempCharDict)
            if tempCharDict.__eq__(charDict1):
                return True
        return False
            

print(Solution().checkInclusion("adc", "dcda"))

# print(Solution().checkInclusion("hello", "ooolleoooleh"))

# resultArr= []

# def perm(s,k,m):
#     if k == m-1:
#         t = []
#         for i in range(m):
#             t.append(s[i])
#         resultArr.append(t)
#     else:
#         for i in range(k,m):
#             swap(s,k,i)
#             perm(s,k+1,m)
#             swap(s,k,i)

# def swap(s,a,b):
#     t = s[a]
#     s[a] = s[b]
#     s[b] = t

# perm(["a","b","c"],0,3)
# print(resultArr)
