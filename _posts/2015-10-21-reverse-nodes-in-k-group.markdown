---
layout: post
title: 25 - Reverse Nodes in k-Group
date: 2015-10-21 14:42:44.000000000 -04:00
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
**Given a linked list, reverse the nodes of a linked list k at a time and return its modified list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.**


``` java
public class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k <= 1) return head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        int i = 0;
        while (head != null) {
            i ++;
            if (i % k == 0) {
                prev = reverse(prev, head.next);
                head = prev.next;
            } else {
                head = head.next;
            }
        }
        return dummy.next;
    }
    public ListNode reverse(ListNode prev, ListNode next) {
        ListNode last = prev.next;
        ListNode curr = last.next;
        while (curr != next) {
            last.next = curr.next;
            curr.next = prev.next;
            prev.next = curr;
            curr = last.next;
        }
        return last;
    }
}
```

``` python
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or k <= 1:
            return head

        prev = dummy = ListNode(0)
        dummy.next = head
        i = 0
        while head:
            i += 1
            if i % k == 0:
                prev = self.reverse(prev, head.next)
                head = prev.next
            else:
                head = head.next
        return dummy.next

    def reverse(self, prev, end):
        last = prev.next
        curr = last.next
        while curr != end:
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = last.next
        return last
```
