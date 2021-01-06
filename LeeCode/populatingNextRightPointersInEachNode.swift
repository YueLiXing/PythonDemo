/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var left: Node?
 *     public var right: Node?
 *	   public var next: Node?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *         self.next = nil
 *     }
 * }
 */

class Solution {
    func connect(_ root: Node?) -> Node? {
        var tempArr:[[Node]] = []
        self.travel(root, tempArr: &tempArr, level: 1)
        return root
    }
    func travel(_ root: Node?, tempArr: inout [[Node]], level: Int) {
        guard root != nil else {
            return
        }
        if tempArr.count < level {
            tempArr.append([])
        }
        root!.next = nil
        tempArr[level-1].last?.next = root
        tempArr[level-1].append(root!)
        travel(root?.left, tempArr: &tempArr, level: level+1)
        travel(root?.right, tempArr: &tempArr, level: level+1)
    }
}