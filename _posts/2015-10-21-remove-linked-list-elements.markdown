---
layout: post
title: Remove Linked List Elements
date: 2015-10-21 14:44:14.000000000 -04:00
categories:
- LinkedList
author: Jason
---
<p><strong><em>Remove all elements from a linked list of integers that have value val.</em></strong></p>

``` java
public class Solution {
    /**
     * @param head a ListNode
     * @param val an integer
     * @return a ListNode
     */
    public ListNode removeElements(ListNode head, int val) {
        // Write your code here
        if (head == null) return null;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode curr = dummy;
        while (curr.next != null) {
            if (curr.next.val == val) {
                curr.next = curr.next.next;
            } else {
                curr = curr.next;
            }
        }
        return dummy.next;
    }
}
```
