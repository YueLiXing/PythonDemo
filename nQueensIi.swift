class Solution {
    typealias Point = (x:Int, y:Int)
    func totalNQueens(_ n: Int) -> Int {
        var result = [[Point]]()
        var temp = [Point]()
        var x = 0, y = 0
        while true {
            if y == 0 && x == n {
                break
            }
            if self.varNQueens(temp, x: x, y: y, n: n) {
                temp.append((x, y))
                if y == n-1 {
                    result.append(temp)
                    let _ = temp.popLast()
                    x += 1
                } else {
                    y += 1
                    x = 0
                }
            } else {
                if x < n-1 {
                    x += 1
                } else {
                    while let last = temp.popLast() {
                        y = last.y
                        x = last.x+1
                        if x < n {
                            break
                        }
                    }
                }
            }
        }
        return result.count
    }
    
    func varNQueens(_ arr:[Point], x: Int, y: Int, n: Int) -> Bool {
        guard 0 <= x && x < n && 0 <= y && y < n else {
            return false
        }
        for tempP in arr {
            if tempP.x == x || tempP.y == y || tempP.x-tempP.y == x-y || tempP.x+tempP.y == x+y {
                return false
            }
        }
        return true
    }
}