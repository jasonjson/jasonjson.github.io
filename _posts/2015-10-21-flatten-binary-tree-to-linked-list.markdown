---
layout: post
title: 114 - Flatten Binary Tree to Linked List
date: 2015-10-21 14:43:36.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, flatten it to a linked list in-place.**

``` python
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        stack = [root]
        prev = None
        while stack:
            curr = stack.pop()
            if prev:
                prev.right = curr
                prev.left = None
            prev = curr
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
```

``` python
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        self.helper(root)

    def helper(self, node):
        if not node:
            return

        left = self.helper(node.left)
        right = self.helper(node.right)
        node.left = None
        node.right = left
        curr = node
        while curr.right:
            curr = curr.right
        curr.right = right
        return node
```
