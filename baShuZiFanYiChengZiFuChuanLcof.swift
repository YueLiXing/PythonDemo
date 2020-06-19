class Solution {
    func translateNum(_ num: Int) -> Int {
        var tempN = num
        var cache = [Int]()
        while tempN > 0 {
            cache.insert(tempN%10, at: 0)
            tempN /= 10
        }
//        Logger.info(cache)
        var pre = 0
        var cur = 0
        var result = 1
        for index in 0..<cache.count {
            pre = cur
            cur = result
//            result = 0
            result = cur
            if index == 0 {
                continue
            }
            let t = cache[index-1]*10+cache[index]
            if 10 <= t && t <= 25 {
                result += pre
            }
        }
        return result
    }
}