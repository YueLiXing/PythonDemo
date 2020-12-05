class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        eqalArr = []
        unEqalArr = []
        for tempS in equations:
            a = tempS[:1]
            b = tempS[-1:]
            if tempS[1:2] == "=":
                for tempArr in unEqalArr:
                    if a in tempArr and b in tempArr:
                        return False
                flag = False
                for tempArr in eqalArr:
                    if a in tempArr and b not in tempArr:
                        tempArr.append(b)
                        flag = True
                    elif a not in tempArr and b in tempArr:
                        tempArr.append(a)
                        flag = True
                if flag == False:
                    eqalArr.append([a,b])
                print(eqalArr,unEqalArr)
            else:
                for tempArr in eqalArr:
                    if a in tempArr and b in tempArr:
                        return False
                unEqalArr.append([a,b])
        return True


print(Solution().equationsPossible(["a==b", "b!=c", "c==a"]))
