---
layout: post
title: 572 - Subtree of Another Tree
date: 2020-01-16
tags:
- Lintcode
categories:
- Binary Search Tree
author: Jason
---
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

``` python
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        elif not s:
            return False

        return self.isSametree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSametree(self, s1, s2):
        if not s1 or not s2:
            return s1 == s2
        return s1.val == s2.val and self.isSametree(s1.left, s2.left) and self.isSametree(s1.right, s2.right)
```
