---
layout: post
title: 129 - Sum Root to Leaf Numbers
date: 2015-11-06 22:04:46.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number. An example is the root-to-leaf path 1->2->3 which represents the number 123. Find the total sum of all root-to-leaf numbers.**


``` python
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        ret = []
        self.helper(root, "", ret)
        return sum(int(n) for n in ret)

    def helper(self, root, path, ret):
        if not root:
            return
        if not root.left and not root.right:
            ret.append(path + str(root.val))
            return
        self.helper(root.left, path + str(root.val), ret)
        self.helper(root.right, path + str(root.val), ret)
```
