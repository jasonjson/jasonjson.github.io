---
layout: post
title: 92 - Reverse Linked List II
date: 2015-10-21 02:46:31.000000000 -04:00
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
**Reverse a linked list from position m to n.**

``` python
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head
        for _ in range(m - 1):
            prev = prev.next
            curr = curr.next

        for _ in range(n - m):
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp

        return dummy.next
```
