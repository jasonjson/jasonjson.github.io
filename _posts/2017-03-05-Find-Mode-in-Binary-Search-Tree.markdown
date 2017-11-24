---
layout: post
title: 501 - Find Mode in Binary Search Tree
date: 2017-03-05
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.**


```python
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, ret = [], []
        prev_val = None
        max_count = current_count = 0

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.val == prev_val:
                    current_count += 1
                else:
                    current_count = 1
                if max_count < current_count:
                    ret = []
                    ret.append(root.val)
                    max_count = current_count
                elif max_count == current_count:
                    ret.append(root.val)
                prev_val = root.val
                root = root.right
        return ret
```
