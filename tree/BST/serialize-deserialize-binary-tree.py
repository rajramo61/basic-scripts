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
        return self.serializeHelper(root, '')

    def serializeHelper(self, node, string):
        if node is None:
            string += "N"
            return string

        string = str(node.val) + ',' + self.serializeHelper(node.left, string) + ',' + self.serializeHelper(node.right,
                                                                                                            string)
        return string

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        values = data.split(',')
        return self.deserializeHelper(values)

    def deserializeHelper(self, values):
        val = float('-inf')
        if values and len(values) > 0:
            val = values.pop(0)

        if val == 'N':
            return None
        node = TreeNode(val)
        node.left = self.deserializeHelper(values)
        node.right = self.deserializeHelper(values)
        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
