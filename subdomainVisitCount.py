class Solution:
    def subdomainVisits(self, cpdomains: [str]) -> [str]:
        self.cacheDict = {}
        for tempDomain in cpdomains:
            tempA = tempDomain.split(" ")
            count = int(tempA[0])
            domain = tempA[1]
            tempA = domain.split(".")
            # if len(tempA) > 1:
            for index in range(len(tempA)):
                domain0 = ".".join(tempA[index:])
                self.cacheDict[domain0] = self.cacheDict.get(domain0, 0)+count
        ret = []
        for key in self.cacheDict:
            count = self.cacheDict[key]
            ret.append("%d %s" % (count, key))
            
        return ret


print(Solution().subdomainVisits(["9001 discuss.leetcode.com"]))
# print(Solution().subdomainVisits(["9001 com"]))
