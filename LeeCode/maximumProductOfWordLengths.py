class Solution:
    def maxProduct(self, words: [str]) -> int:
        cacheDict = {}
        ret = 0
        for w in words:
            tempSet = set()
            for c in w:
                tempSet.add(c)
            cacheDict[w] = tempSet
        for index in range(len(words)-1):
            w1 = words[index]
            s1 = cacheDict[w1]
            for index2 in range(index+1,len(words)):
                w2 = words[index2]
                s2 = cacheDict[w2]
                flag = False
                for tempC in s2:
                    if tempC in s1:
                        flag = True
                        break
                if flag == False:
                    ret = max(ret, len(w1)*len(w2))
        return ret

r = Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
print(r)
