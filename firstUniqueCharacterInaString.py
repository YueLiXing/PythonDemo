class Solution:
    def firstUniqChar(self, s: str) -> int:
        tempArr = []
        tempD = {}
        index = 0
        l = 0
        for c in s:
            if c in tempD:
                cIndex = tempD[c]
                tempArr[cIndex] = {
                    "k": c, "count": tempArr[cIndex]["count"]+1, "index": tempArr[cIndex]["index"]}
            else:
                tempD[c] = l
                tempArr.append({"k":c,"count":1,"index":index})
                l += 1
            index += 1
        if l > 0:
            for tD in tempArr:
                if tD["count"] == 1:
                    return tD["index"]
            return -1
        else:
            return -1
        

print(Solution().firstUniqChar("aadadaad"))

