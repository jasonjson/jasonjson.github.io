---
layout: post
title: 430 - Flatten A Multilevel Doubly Linked List
date: 2020-01-07
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
**You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below. Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.**

```python
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        dummy = Node(0, None, None, None)
        dummy.next = head
        while head:
            if head.child:
                child_head = self.flatten(head.child)
                head.child = None
                child_tail = self.get_tail(child_head)
                head_next = head.next
                head.next = child_head
                child_head.prev = head
                child_tail.next = head_next
                if head_next:
                    head_next.prev = child_tail
                head = head_next
            else:
                head = head.next

        return dummy.next
    def get_tail(self, node):
        while node.next:
            node = node.next
        return node
```
