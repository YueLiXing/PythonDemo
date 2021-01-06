class Solution {
    func commonChars(_ A: [String]) -> [String] {
        var cacheSet: Set<String>? = nil
        
        for tempS in A {
            var tempSet = Set<String>()
            
            for tempC in tempS {
                var cCount = 1
//                var key = String(tempC)
//                while tempSet.contains(key) {
//                    key = String.init(format: "%s_%d", tempC, cCount)
//                    cCount += 1
//                }
//                tempSet.insert(key)
                if tempSet.contains(String(tempC)) {
                    while true {
                        let newCS = String(tempC).appendingFormat("_%d", cCount)
                        if tempSet.contains(newCS) == false {
                            tempSet.insert(newCS)
                            break
                        } else {
                            cCount += 1
                        }
                    }
                } else {
                    tempSet.insert(String(tempC))
                }
            }
            if cacheSet != nil {
                cacheSet = cacheSet!.intersection(tempSet)
            } else {
                cacheSet = tempSet
            }
        }
        return cacheSet?.map({ (tempS) -> String in
            return String(tempS.split(separator: "_")[0])
        }) ?? []
    }
}