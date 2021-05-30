class Solution {
    func findCircleNum(_ isConnected: [[Int]]) -> Int {
        var cache = [Int:Int]()
        var linkSet = Set<Int>()
        for indexN in 0..<isConnected.count {
            let tempArr = isConnected[indexN]
            for indexM in 0..<indexN {
                let val = tempArr[indexM]
                // Logger.info("\(indexM) \(indexN) \(val)")
                if val == 1 {
                    if linkSet.contains(indexM) || linkSet.contains(indexN) {
                        if linkSet.contains(indexM) && linkSet.contains(indexN) {
                            if cache[indexM] == cache[indexN] {
                                continue
                            } else {
                                cache.filter { (key: Int, value: Int) -> Bool in
                                    return value == cache[indexN]
                                }.forEach { (key: Int, value: Int) in
                                    cache[key] = cache[indexM]
                                }
                            }
                        } else {
                            if linkSet.contains(indexM) {
                                linkSet.insert(indexN)
                                cache[indexN] = cache[indexM]
                            } else {
                                linkSet.insert(indexM)
                                cache[indexM] = cache[indexN]
                            }
                        }
                    } else {
                        linkSet.insert(indexN)
                        linkSet.insert(indexM)
                        cache[indexM] = indexM
                        cache[indexN] = indexM
                    }
                }
            }
        }
//        Logger.info(cache)
        for indexN in 0..<isConnected.count {
            if linkSet.contains(indexN) == false {
                linkSet.insert(indexN)
                cache[indexN] = indexN
            }
        }
        var result = Set<Int>()
        cache.forEach { (key: Int, value: Int) in
            result.insert(value)
        }
        return result.count
    }
}