---
layout: post
title: 298 - Binary Tree Longest Consecutive Sequence
date: 2015-10-29 10:37:39.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, find the length of the longest consecutive sequence path. The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).**

``` python
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        ret = [0]

        def helper(node):
            if not node:
                return 0
            local_max = 1
            left = helper(node.left)
            right = helper(node.right)
            if node.left and node.left.val == node.val + 1:
                local_max = max(local_max, left + 1)
            if node.right and node.right.val == node.val + 1:
                local_max = max(local_max, right + 1)
            ret[0] = max(ret[0], local_max)
            return local_max

        helper(root)
        return ret[0]

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        ret = 0
        while stack:
            node, count = stack.pop()
            if node.left:
                stack.append([node.left, count + 1 if node.left.val == node.val + 1 else 1])
            if node.right:
                stack.append([node.right, count + 1 if node.right.val == node.val + 1 else 1])
            ret = max(ret, count)
        return ret
```
