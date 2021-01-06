import functools


class Solution:
    def largestNumber(self, nums: [int]) -> str:
        def cmpStr(s1, s2) -> bool:
            # print("cmp", s1+s2, s2+s1)
            return int(s1+s2) - int(s2+s1)

        tempArr = []
        for tempN in nums:
            tempArr.append(str(tempN))

        tempArr.sort(key=functools.cmp_to_key(cmpStr), reverse=True)

        ret = "".join(tempArr)
        if int(ret) == 0:
            return "0"
        return ret


# print(Solution().largestNumber([3, 30, 34, 5, 9]))  # 9 5
print(Solution().largestNumber([30, 10, 20, 1]))  # 3020110


"""
swift

class Solution {
    func largestNumber(_ nums: [Int]) -> String {
        var temp = nums.map { (n) -> String in
            return String(n)
        }.sorted { (s0, s1) -> Bool in
            return s0+s1 > s1+s0
        }.joined(separator: "")
        if Int(temp) == 0 {
            return "0"
        } else {
            return temp
        }
    }
}

"""