# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    if num == 6:
        return 0
    else:
        if num > 6:
            return 1
        else:
            return -1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        ret = 0
        while low <= high:
            mid = (low+high)//2
            ret = guess(mid)
            if ret == 0:
                ret = mid
                break
            elif ret > 0:
                low = mid+1
            else:
                high = mid-1
        return ret

print(Solution().guessNumber(1000))
