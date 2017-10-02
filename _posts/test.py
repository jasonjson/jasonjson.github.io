#!/usr/bin/python

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        ret = []
        self.helper(root, [], ret)
        import pprint
        pprint.pprint(ret)
        return sum([int(n) for n in ret])

    def helper(self, root, curr, ret):
        curr += [str(root.val)]
        if not root.left and not root.right:
            ret.append("".join(curr))
            return
        if root.left:
            self.helper(root.left, curr, ret)
            curr.pop()
        if root.right:
            self.helper(root.right, curr, ret)
            curr.pop()
if __name__ == "__main__":
    solution = Solution()

    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    import pprint
    pprint.pprint(solution.sumNumbers(root))
