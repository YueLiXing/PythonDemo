# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        cacheNode = [root]
        result = []
        while len(cacheNode) > 0:
            nextCacheNode = []
            flag = False
            for temp in cacheNode:
                if temp is NULL:
                    nextCacheNode.append(NULL)
                    nextCacheNode.append(NULL)
                else:
                    nextCacheNode.append(temp.left)
                    nextCacheNode.append(temp.right)
                    if flag is False:
                        if temp.left is not NULL or temp.right is not NULL:
                            flag = True
            if flag:
                cacheNode = nextCacheNode
        return result
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))