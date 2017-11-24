---
layout: post
title: 378 - Convert Binary Search Tree to Doubly Linked List
date: 2015-10-27 15:22:08.000000000 -04:00
tags:
- Lintcode
categories:
- Binary Search Tree
author: Jason
---
**Convert a binary search tree to doubly linked list with in-order traversal.**


``` python
class Solution:
    """
    @param: root: The root of tree
    @return: the head of doubly list node
    """
    def bstToDoublyList(self, root):
        # write your code here
        if not root:
            return

        prev = dummy = DoublyListNode(0)
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                new_node = DoublyListNode(root.val)
                prev.next = new_node
                new_node.prev = prev
                prev = new_node
                root = root.right
        dummy.next.prev = None
        return dummy.next
```
