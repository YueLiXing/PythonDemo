class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num // 2 + 1
        while left <= right:
            mid = (left+right)//2
            temp = mid*mid
            # print(temp, num, left, mid, right)
            if temp == num:
                return True
            elif temp > num:
                right = mid-1
            else:
                left = mid+1
        return False


print(Solution().isPerfectSquare(1))

print(Solution().isPerfectSquare(14))

print(Solution().isPerfectSquare(16))
