---
layout: post
title: 124 - Binary Tree Maximum Path Sum
date: 2015-10-21 02:52:23.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.**


``` python
class Solution(object):

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ret = [float("-inf")]
        self.helper(root, ret)
        return ret[0]

    def helper(self, root, ret):
        if not root:
            return 0
        left_sum = max(0, self.helper(root.left, ret))
        right_sum = max(0, self.helper(root.right, ret))
        ret[0] = max(ret[0], left_sum + right_sum + root.val)
        return max(left_sum, right_sum) + root.val
```
