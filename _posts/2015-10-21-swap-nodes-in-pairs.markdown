---
layout: post
title: Swap Nodes in Pairs
date: 2015-10-21 14:44:57.000000000 -04:00
tags:
- Algorithm
categories:
- LinkedList
author: Jason
---
**Given a linked list, swap every two adjacent nodes and return its head.**


``` java
public class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        while (prev.next != null && prev.next.next != null) {
            ListNode last = prev.next;
            ListNode curr = last.next;
            last.next = curr.next;
            curr.next = prev.next;
            prev.next = curr;
            prev = last;
        }
        return dummy.next;
    }
}
```

``` java
public class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode n1 = head, n2 = head.next;
        n1.next = n2.next;
        n2.next = n1;
        n1.next = swapPairs(n1.next);
        return n2;
    }
}
```

``` python
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            first.next = second.next
            second.next = prev.next
            prev.next = second
            prev = first
        return dummy.next
```
