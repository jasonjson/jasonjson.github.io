#!/usr/bin/python
# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        prev = [root]
        while prev:
            curr = []
            for node in prev:
                if node:
                    curr.append(node.left)
                    curr.append(node.right)
            if len(curr) % 2 != 0 or not self.symmetric_list(curr):
                return False
            prev = curr
        return True

    def symmetric_list(self, curr):
        lo, hi = 0, len(curr) - 1
        import pdb
        pdb.set_trace()
        while lo <= hi:
            if curr[lo] is None and curr[hi] is None:
                lo += 1
                hi -= 1
                continue
            elif curr[lo] is None or curr[hi] is None:
                return False
            elif curr[lo].val != curr[hi].val:
                return False
            lo += 1
            hi -= 1
        return True

if __name__ == "__main__":
    solution = Solution()
    r1 = TreeNode(1)
    r2 = TreeNode(2)
    r3 = TreeNode(2)
    r4 = TreeNode(3)
    r5 = TreeNode(4)
    r6 = TreeNode(4)
    r7 = TreeNode(3)
    r1.left = r2
    r1.right = r3
    r2.left = r4
    r2.right = r5
    r3.left = r6
    r3.right = r7
    import pprint
    pprint.pprint(solution.isSymmetric(r1))
