#!/usr/bin/python
# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        stack = []
        prev = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if prev and root.val <= prev:
                    return False
                prev = root.val
                root = root.right
        return True

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(0)
    root.left = None
    root.right = TreeNode(-1)
    import pprint
    pprint.pprint(solution.isValidBST(root))
