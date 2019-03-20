class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeDict = {}

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        if key in self.timeDict:
            tempArr = self.timeDict[key]
            l = len(tempArr)
            if tempArr[0][0] > timestamp:
                tempArr.insert(0, (timestamp, value))
            elif tempArr[l-1][0] < timestamp:
                tempArr.append((timestamp, value))
            else:
                low = 0
                high = l-1
                while low <= high:
                    mid = (low+high)//2
                    if tempArr[mid][0] == timestamp:
                        tempArr[mid] = (timestamp, value)
                        break
                    elif tempArr[mid][0] < timestamp:
                        low = mid+1
                    else:
                        high = mid
                    if low == high:
                        if tempArr[low][0] > timestamp:
                            tempArr.insert(low, (timestamp, value))
                        else:
                            tempArr.insert(low+1, (timestamp, value))
                        break
        else:
            self.timeDict[key] = [(timestamp,value)]

    
    def get(self, key: 'str', timestamp: 'int') -> 'str':
        if key in self.timeDict:
            tempArr = self.timeDict[key]
            l = len(tempArr)
            if tempArr[0][0] > timestamp:
                return ""
            elif tempArr[l-1][0] <= timestamp:
                return tempArr[l-1][1]
            else:
                low = 0
                high = l-1
                while low <= high:
                    mid = (low+high)//2
                    if tempArr[mid][0] == timestamp:
                        return tempArr[mid][1]
                    elif tempArr[mid][0] < timestamp:
                        if tempArr[mid+1][0] > timestamp:
                            return tempArr[mid][1]
                        else:
                            low = mid+1
                    else:
                        high = mid
                    if low == high:
                        return tempArr[low-1][1]
                        # print("low: ",low)
                        # break
        else:
            return ""
        

        # Your TimeMap object will be instantiated and called as such:
        # obj = TimeMap()
        # obj.set(key,value,timestamp)
        # param_2 = obj.get(key,timestamp)
    def showVal(self):
        print("showVal ",self.timeDict)


# ["TimeMap", "set", "set", "get", "get", "get", "get", "get"]
# [[], ["love", "high", 10], ["love", "low", 20], ["love", 5],
#     ["love", 10], ["love", 15], ["love", 20], ["love", 25]]

obj = TimeMap()
# obj.set("love", "high", 10)
# obj.set("love", "low", 20)
# obj.set("love", "low10", 10)
# obj.set("love", "low14", 14)
# obj.set("love", "low12", 12)
# obj.set("love", "low13", 13)
# obj.showVal()
# print("---")
# print(obj.get("love", 5))
# print(obj.get("love", 16))
# print(obj.get("love", 5)) # 
# print(obj.get("love", 10)) # high
# print(obj.get("love", 15)) # high
# print(obj.get("love", 20)) # low
# print(obj.get("love", 25)) # low
# obj.showVal()

# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], [], [], [],
    # ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
obj.set("foo", "bar", 1)
print(obj.get("foo", 1))
print(obj.get("foo", 3))
obj.set("foo", "bar2", 4)
print(obj.get("foo", 4))
print(obj.get("foo", 5))
obj.showVal()


