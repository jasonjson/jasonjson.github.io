---
layout: post
title: 543 - Diameter of a Binary Tree
date: 2015-10-21 02:54:43.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.**

``` python
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ret = [0]
        self.helper(root, ret)
        return ret[0]

    def helper(self, root, ret):
        if not root:
            return 0
        left = self.helper(root.left, ret)
        right = self.helper(root.right, ret)
        ret[0] = max(ret[0], left + right)
        return max(left, right) + 1
```
