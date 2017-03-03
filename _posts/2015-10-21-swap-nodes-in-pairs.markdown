---
layout: post
title: Swap Nodes in Pairs
date: 2015-10-21 14:44:57.000000000 -04:00
tags: algorithm
categories:
- LinkedList
author: Jason
---
<p><strong><em>Given a linked list, swap every two adjacent nodes and return its head.</em></strong></p>


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
``` java
public class Solution {
    public ListNode swapPairs(ListNode head) {
        // Write your code here
        if (head == null) return null;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        int i = 0;
        while (head != null) {
            i ++;
            if (i % 2 == 0) {
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
