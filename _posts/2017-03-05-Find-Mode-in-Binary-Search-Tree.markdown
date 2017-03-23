---
layout: post
title: Find Mode in Binary Search Tree
date: 2017-03-05
tags:
- Algorithm
categories:
- Binary Search Tree
author: Jason
---
<p><strong><em>Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.</em></strong></p>

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        max_count = 0
        stack = []
        result = []
        prev_val = None
        current_count = 0

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop(-1)
                #'if prev' is wrong since prev_val can be 0 which gives false
                if prev_val is not None and root.val == prev_val:
                    current_count += 1
                else:
                    current_count = 1
                if max_count < current_count:
                    result = []
                    result.append(root.val)
                    max_count = current_count
                elif max_count == current_count:
                    result.append(root.val)
                prev_val = root.val
                root = root.right
        return result
```
