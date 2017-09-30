#!/usr/bin/python

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
        def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """


        self.helper(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1)
    def helper(self, postorder, post_start, post_end, inorder, in_start, in_end):
        if post_start > post_end or in_start > in_end:
            return
        root = TreeNode(postorder[post_end])
        index = inorder.index(root.val)
        root.left = self.helper(postorder, post_start, index - in_start + post_start - 1, inorder, in_start, index - 1)
        root.right = self.helper(postorder, index - in_start + post_start, post_end - 1, inorder, index + 1, in_end)
        return root
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.buildTree([-1],[-1]).val)
