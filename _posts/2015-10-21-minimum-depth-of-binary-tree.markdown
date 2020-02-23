---
layout: post
title: 111 - Minimum Depth of Binary Tree
date: 2015-10-21 03:01:12.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.**

``` python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0:
            return right + 1
        elif right == 0:
            return left + 1
        else:
            return min(left, right) + 1
```
