class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        fileDict = {}
        for tempS in paths:
            a = tempS.split(" ")
            dirP = a[0]
            for i in range(1,len(a)):
                s = a[i]
                start = s.find("(")
                end = s.find(")")
                fileName = s[:start]
                val = s[start+1:end]
                fileP = dirP+"/"+fileName

                if val in fileDict:
                    fileDict[val].append(fileP)
                else:
                    fileDict[val] = [fileP]
        ret = []
        for key in fileDict:
            if len(fileDict[key]) >= 2:
                ret.append(fileDict[key])
        return ret


print(Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
