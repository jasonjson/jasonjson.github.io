---
layout: post
title: Remove Nth Node From End of List
date: 2015-10-21 02:44:57.000000000 -04:00
categories:
- LinkedList
author: Jason
---
<p><strong><em>Given a linked list, remove the nth node from the end of list and return its head.</em></strong></p>


``` java
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) return null;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode curr = dummy, slow = dummy;
        for (int i = 0; i <= n; i++) {
            curr = curr.next;
        }
        while (curr != null) {
            slow = slow.next;
            curr = curr.next;
        }
        slow.next = slow.next.next;
        return dummy.next;
    }
}
```
