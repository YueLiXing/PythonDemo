class Solution {
    struct Node {
        var s = ""
        var val = 0.0
    }
    func calcEquation(_ equations: [[String]], _ values: [Double], _ queries: [[String]]) -> [Double] {

        var result = [Double]()
        var cacheDict = [String:Node]()
        var tempEquations = [[String]]()
        var tempValues = [Double]()
        for index in 0..<equations.count {
            let tempArr = equations[index]
            let first = tempArr[0]
            let sec = tempArr[1]
            let val = values[index]
            let contain0 = cacheDict.contains(where: { (key: String, value: Node) -> Bool in
                return key == first
            })
            let contain1 = cacheDict.contains(where: { (key: String, value: Node) -> Bool in
                return key == sec
            })
            if contain0 && contain1 {
                continue
            } else if contain0 == false && contain1 == false {
                if cacheDict.count == 0 {
                    cacheDict[first] = Node(s: first, val: 1)
                    cacheDict[sec] = Node(s: first, val: 1/val)
                } else {
                    tempEquations.append(tempArr)
                    tempValues.append(val)
                }
            } else {
                if contain0 {
                    cacheDict[sec] = Node(s: first, val: 1/val)
                } else {
                    cacheDict[first] = Node(s: sec, val: val)
                }
            }
        }
        var index = tempEquations.count-1
        var flag = false
        while tempEquations.count > 0 {
            if index < 0 {
                index = tempEquations.count-1
                flag = true
            }
            let tempArr = tempEquations[index]
            let first = tempArr[0]
            let sec = tempArr[1]
            let val = tempValues[index]
            let contain0 = cacheDict.contains(where: { (key: String, value: Node) -> Bool in
                return key == first
            })
            let contain1 = cacheDict.contains(where: { (key: String, value: Node) -> Bool in
                return key == sec
            })
            if contain0 == false && contain1 == false {
                if flag {
                    cacheDict[first] = Node(s: first, val: 1)
                    cacheDict[sec] = Node(s: first, val: 1/val)
                    tempEquations.remove(at: index)
                    tempValues.remove(at: index)
                }
                index -= 1
                continue
            } else {
                if contain0 && contain1 {
                    tempEquations.remove(at: index)
                    tempValues.remove(at: index)
                    index -= 1
                    continue
                }
                if contain0 {
                    cacheDict[sec] = Node(s: first, val: 1/val)
                } else {
                    cacheDict[first] = Node(s: sec, val: val)
                }
                tempEquations.remove(at: index)
                tempValues.remove(at: index)
                index -= 1
            }
        }
        for tempArr in queries {
            let first = tempArr[0]
            let sec = tempArr[1]
            let contain0 = cacheDict.contains(where: { (key: String, value: Node) -> Bool in
                return key == first
            })
            let contain1 = cacheDict.contains(where: { (key: String, value: Node) -> Bool in
                return key == sec
            })
            if contain0 == false || contain1 == false {
                result.append(-1)
            } else {
                var firstVal = 1.0
                var tempFirst = first
                while true {
                    let node = cacheDict[tempFirst]!
                    tempFirst = node.s
                    if node.val == 1 {
                        break
                    } else {
                        firstVal *= node.val
                    }
                }
                var secVal = 1.0
                var tempSec = sec
                while true {
                    let node = cacheDict[tempSec]!
                    tempSec = node.s
                    if node.val == 1 {
                        break
                    } else {
                        secVal *= node.val
                    }
                }
                if tempFirst == tempSec {
                    result.append(firstVal/secVal)
                } else {
                    result.append(-1)
                }
            }
        }
        return result
    }
}