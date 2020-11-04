/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */
class Solution {
    func mergeTrees(_ t1: TreeNode?, _ t2: TreeNode?) -> TreeNode? {
        if t1 == nil && t2 == nil {
            return nil
        }
        let root = TreeNode(0)
        _mergeTrees(root, t1, t2)
        return root
    }
    func _mergeTrees(_ root: TreeNode, _ t1: TreeNode?, _ t2: TreeNode?) {
        if t1 != nil {
            root.val = t1!.val
        }
        if t2 != nil {
            root.val += t2!.val
        }
        if t1?.left != nil || t2?.left != nil {
            root.left = TreeNode(0)
            _mergeTrees(root.left!, t1?.left, t2?.left)
        }
        if t1?.right != nil || t2?.right != nil {
            root.right = TreeNode(0)
            _mergeTrees(root.right!, t1?.right, t2?.right)
        }
    }
}