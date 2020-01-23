---
layout: post
title: 426 - Convert Binary Search Tree To Sorted Doubly Linked List
date: 2020-01-23
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place. You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

```python
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return

        dummy = head = Node(0)
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                head.right = root
                root.left = head
                head = head.right
                root = root.right

        head.right = dummy.right
        dummy.right.left = head
        return dummy.right
```
