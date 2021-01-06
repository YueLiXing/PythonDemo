class Solution:
    def isAlienSorted(self, words: [str], order: str) -> bool:
        indexDict = {}
        for i in range(len(order)):
            indexDict[order[i]] = i
        for i in range(len(words)-1):
            w0 = words[i]
            w1 = words[i+1]
            l0 = len(w0)
            l1 = len(w1)
            flag = False
            for j in range(min(l0,l1)):
                if indexDict[w0[j]] < indexDict[w1[j]]:
                    flag = True
                    break
                elif indexDict[w0[j]] > indexDict[w1[j]]:
                    return False
                    
            if flag == False and l0 > l1:
                return False
        return True


# words = ["hello", "leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
print(Solution().isAlienSorted(
    ["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
