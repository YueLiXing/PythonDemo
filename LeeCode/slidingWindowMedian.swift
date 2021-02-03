class Solution {
    func medianSlidingWindow(_ nums: [Int], _ k: Int) -> [Double] {
        var result = [Double]()
        var cacheArr = [Int]()
        var sortCacheArr = [Int]()
        var count = 0
        for tempN in nums {
            if count < k {
                count += 1
                cacheArr.append(tempN)
                self.insertNum(tempN, &sortCacheArr)
            } else {
                let first = cacheArr.removeFirst()
                sortCacheArr.remove(at: sortCacheArr.firstIndex(of: first)!)
                cacheArr.append(tempN)
                self.insertNum(tempN, &sortCacheArr)
            }
            if count == k {
                if k%2 == 0 {
                    result.append(Double(sortCacheArr[k/2-1]+sortCacheArr[k/2])*0.5)
                } else {
                    result.append(Double(sortCacheArr[k/2])*1.0)
                }
            }
        }
        return result
    }
    func insertNum(_ tempNum: Int, _ sortArr: inout [Int]) {
        if sortArr.count == 0 {
            sortArr.append(tempNum)
            return
        }
        if sortArr[0] >= tempNum {
            sortArr.insert(tempNum, at: 0)
        } else if sortArr[sortArr.count-1] <= tempNum {
            sortArr.append(tempNum)
        } else {
            var left = 0
            var right = sortArr.count-1
            while left < right {
                let mid = (left+right+1)/2
                if sortArr[mid] >= tempNum {
                    if sortArr[mid-1] <= tempNum {
                        sortArr.insert(tempNum, at: mid)
                        break
                    }
                    right = mid
                } else {
                    if sortArr[mid+1] >= tempNum {
                        sortArr.insert(tempNum, at: mid+1)
                        break
                    } else {
                        left = mid+1
                    }
                    
                }
            }
        }
    }
}