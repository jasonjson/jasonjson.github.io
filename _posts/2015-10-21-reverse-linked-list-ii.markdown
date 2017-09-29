---
layout: post
title: Reverse Linked List II
date: 2015-10-21 02:46:31.000000000 -04:00
tags:
- Algorithm
categories:
- LinkedList
author: Jason
---
**Reverse a linked list from position m to n.**


``` java
public class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        int index = 1;
        ListNode prev = dummy;
        while (index < m) {
            index ++;
            prev = prev.next;
        }
        ListNode last = prev.next, curr = last.next;
        while (index < n) {
            index ++;
            last.next = curr.next;
            curr.next = prev.next;
            prev.next = curr;
            curr = last.next;
        }
        return dummy.next;
    }
}
```

``` python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return

        index = 1
        dummy, dummy.next = ListNode(0), head
        prev = dummy
        while index < m:
            index += 1
            prev = prev.next
        last, curr = prev.next, prev.next.next
        while index < n:
            index += 1
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = last.next
        return dummy.next
```
