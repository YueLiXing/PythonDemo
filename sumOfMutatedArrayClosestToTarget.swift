class Solution {
    func findBestValue(_ arr: [Int], _ target: Int) -> Int {
        let tempArr = arr.sorted()
        var index = 0
        var cacheSum = 0
        let count = tempArr.count
        for val in tempArr {
            let avg = Double(target-cacheSum)/Double(count-index)
            if avg < Double(val) {
                return Int(avg+0.49)
            }
            cacheSum += val
            index += 1
        }
        return tempArr.last!
    }
}