import collections


class Solution:
    def formatStr(self, s: str):
        countDict = collections.defaultdict(int)
        for c in s:
            countDict[c] += 1
        result = ""
        for k in sorted(countDict.keys()):
            v = countDict[k]
            result += k+str(v)+'|'
        return result

    def groupAnagrams(self, strs: [str]) -> [[str]]:
        cacheDict = collections.defaultdict(list)
        for s in strs:
            key = self.formatStr(s)
            tempArray = cacheDict[key]
            tempArray.append(s)
        # print(cacheDict)
        result = []
        for k, v in cacheDict.items():
            result.append(v)
        return result


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
