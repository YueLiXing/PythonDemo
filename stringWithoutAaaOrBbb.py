class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        countA = 0
        countB = 0
        ret = ""
        while A > 0 or B > 0:
            if countA == 2:
                ret += "b"
                countA = 0
                countB = 1
                B -= 1
                continue
            if countB == 2:
                ret += "a"
                countB = 0
                countA = 1
                A -= 1
                continue
            if B >= A:
                ret += "b"
                countB += 1
                B -= 1
            else:
                ret += "a"
                countA += 1
                A -= 1
            # print(ret)
        return ret

print(Solution().strWithout3a3b(3,4))

# a = "asd"
# a.join("a")
# print(a)
