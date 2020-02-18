---
layout: post
title: 117 - Populating Next Right Pointers in Each Node II
date: 2015-11-09 18:52:59.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Follow up for problem "Populating Next Right Pointers in Each Node". What if the given tree could be any binary tree? Would your previous solution still work?**

``` python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = dummy = Node(0)
        node = root
        while node:
            curr.next = node.left
            if curr.next:
                curr = curr.next
            curr.next = node.right
            if curr.next:
                curr = curr.next
            node = node.next
            if not node:
                node = dummy.next
                curr = dummy
        return root
```
