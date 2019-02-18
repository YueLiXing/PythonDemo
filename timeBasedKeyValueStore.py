class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeArr = []
        self.timeDict = {}

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        if timestamp not in self.timeArr:
            self.timeDict[timestamp] = {}
            index = 0
            if len(self.timeArr) == 0:
                self.timeArr.append(timestamp)
            else:
                index = self.getTimestamp(timestamp)+1
                if index < len(self.timeArr):
                    self.timeArr.insert(index,timestamp)
                else:
                    self.timeArr.append(timestamp)
        tempD = self.timeDict.get(timestamp)
        tempD[key] = value
            

    def getTimestamp(self, timestamp: 'int') -> 'int':
        if len(self.timeArr) == 0:
            return -1
        if self.timeArr[0] > timestamp:
            return -1
        if self.timeArr[len(self.timeArr)-1] < timestamp:
            return len(self.timeArr)-1
        low = 0
        high = len(self.timeArr)-1
        while low <= high:
            mid = (low+high)//2
            if self.timeArr[mid] == timestamp:
                return mid
            elif self.timeArr[mid] < timestamp:
                if mid+1 < len(self.timeArr) and self.timeArr[mid+1] > timestamp:
                    return mid
                else:  
                    low = mid+1
            else:
                high = mid-1
        return low
    def get(self, key: 'str', timestamp: 'int') -> 'str':
        index = self.getTimestamp(timestamp)

        while index >= 0:
            tempD = self.timeDict[self.timeArr[index]]
            if key in tempD:
                return tempD[key]
            index -= 1
        return ""

        # Your TimeMap object will be instantiated and called as such:
        # obj = TimeMap()
        # obj.set(key,value,timestamp)
        # param_2 = obj.get(key,timestamp)


# ["TimeMap", "set", "set", "get", "get", "get", "get", "get"]
# [[], ["love", "high", 10], ["love", "low", 20], ["love", 5],
#     ["love", 10], ["love", 15], ["love", 20], ["love", 25]]

obj = TimeMap()
obj.set("love", "high", 10)
obj.set("love", "low", 20)
print(obj.get("love", 5)) # 
print(obj.get("love", 10)) # high
print(obj.get("love", 15)) # high
print(obj.get("love", 20)) # low
print(obj.get("love", 25)) # low

