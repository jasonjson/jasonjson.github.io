---
layout: post
title: 445 - Add Two Numbers II
date: 2020-01-18
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2

        def stack_value(head):
            stack = []
            while head:
                stack.append(head.val)
                head = head.next
            return stack

        s1, s2 = stack_value(l1), stack_value(l2)
        carry = 0
        head = None
        while s1 or s2 or carry:
            if s1:
                carry += s1.pop()
            if s2:
                carry += s2.pop()
            new_node = ListNode(carry % 10)
            carry //= 10
            new_node.next = head
            head = new_node
        return head
```
