class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        ret = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i+1]-timeSeries[i] <= duration:
                ret += timeSeries[i+1]-timeSeries[i]
            else:
                ret += duration
        if len(timeSeries) > 0:
            ret += duration
        return ret
