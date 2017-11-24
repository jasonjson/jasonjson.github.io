---
layout: post
title: 11 - Search Range in Binary Search Tree
date: 2015-10-21 02:58:42.000000000 -04:00
tags:
- Lintcode
categories:
- Binary Search Tree
author: Jason
---
**Given two values k1 and k2 (where k1 <= k2) and a root pointer to a Binary Search Tree. Find all the keys of tree in range k1 to k2. i.e. print all x such that k1 <= x <= k2 and x is a key of given BST. Return all the keys in ascending order.**


``` python
class Solution:
    """
    @param: root: param root: The root of the binary search tree
    @param: k1: An integer
    @param: k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here

        stack, ret = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if k1 <= root.val <= k2:
                    ret.append(root.val)
                root = root.right
        return ret
```
