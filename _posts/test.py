#!/usr/bin/python

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root or not root.left or root.right:
            return

        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        import pdb
        pdb.set_trace()
        self.connect(root.left)
        self.connect(root.right)

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right= TreeNode(3)
    import pprint
    pprint.pprint(solution.connect(root))


