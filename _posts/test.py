#!/usr/bin/python

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        right_tree = self.flatten(root.right)
        left_tree = self.flatten(root.left)
        root.right = left_tree
        curr = root
        while curr.right:
            curr = curr.right
        curr.right = right_tree

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    import pprint
    pprint.pprint(solution.flatten(root))
    print root, root.left, root.right


