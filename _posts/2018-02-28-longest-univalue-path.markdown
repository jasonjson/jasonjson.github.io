---
layout: post
title: 687 - Longest Univalue Path
date: 2018-02-28
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.**


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        ret = [0]
        self.helper(root, ret)
        return ret[0]

    def helper(self, root, ret):
        if not root:
            return 0

        left_length = self.helper(root.left, ret)
        right_length = self.helper(root.right, ret)
        if root.left and root.val == root.left.val:
            left_length += 1
        else:
            left_length = 0
        if root.right and root.val == root.right.val:
            right_length += 1
        else:
            right_length = 0
        ret[0] = max(ret[0], left_length + right_length)
        return max(left_length, right_length)
```
