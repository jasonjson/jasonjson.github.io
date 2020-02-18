---
layout: post
title: 116 - Populating Next Right Pointers in Each Node
date: 2015-11-09 17:36:58.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL. Initially, all next pointers are set to NULL.**

``` python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                queue.append(curr.left)
                queue.append(curr.right)
        return root
```
