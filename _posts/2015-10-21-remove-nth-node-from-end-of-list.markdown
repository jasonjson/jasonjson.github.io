---
layout: post
title: 19 - Remove Nth Node From End of List
date: 2015-10-21 02:44:57.000000000 -04:00
tags:
- Leetcode
categories:
- LinkedList
author: Jason
---
**Given a linked list, remove the nth node from the end of list and return its head.**


``` java
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) return null;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode curr = dummy, slow = dummy;
        for (int i = 0; i < n; i++) {
            curr = curr.next;
        }
        while (curr.next != null) {
            slow = slow.next;
            curr = curr.next;
        }
        slow.next = slow.next.next;
        return dummy.next;
    }
}
```

``` python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return

        dummy = ListNode(0)
        dummy.next = head

        slow, fast = dummy, dummy
        for i in xrange(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
```
