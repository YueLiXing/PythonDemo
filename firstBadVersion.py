# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        if high == 1:
            return 1
        while low <= high:
            mid = (low+high)//2

            if isBadVersion(mid) == True:
                if mid > 1:
                    if mid == n:
                        return n
                    if isBadVersion(mid-1) == False:
                        return mid
                    else:
                        high = mid-1
                else:
                    return mid
            else:
                low = mid+1
