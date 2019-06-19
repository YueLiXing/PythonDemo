class Solution:
    def getSkyline(self, buildings: [[int]]) -> [[int]]:
        l = 0
        r = 0
        h = 0
        ret = []
        for val in buildings:
            tempL = val[0]
            tempR = val[1]
            tempH = val[2]
            if l == 0:
                l = val[0]
                r = val[1]
                h = val[2]
                ret.append([l,h])
            else:
                if tempL <= r:
                    if tempH > h:
                        ret.append([tempL, tempH])
                    else:
                        ret.append([r, tempH])
                    h = tempH
                    ret.append([r,tempH])
                    r = tempR
                else:
                    ret.append([r,0])
                    ret.append([tempL,tempH])

        return ret
            

print(Solution().getSkyline(
    [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
