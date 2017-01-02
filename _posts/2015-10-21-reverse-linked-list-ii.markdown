---
layout: post
title: Reverse Linked List II
date: 2015-10-21 02:46:31.000000000 -04:00
categories:
- LinkedList
author: Jason
---
<p><strong><em>Reverse a linked list from position m to n.</em></strong><br />


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
