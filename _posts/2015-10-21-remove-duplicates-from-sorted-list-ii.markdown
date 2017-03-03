---
layout: post
title: Remove Duplicates from Sorted List II
date: 2015-10-21 02:43:18.000000000 -04:00
tags: algorithm
categories:
- LinkedList
author: Jason
---
<p><strong><em>Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.</em></strong></p>


``` java
public class Solution {
    /**
     * @param ListNode head is the head of the linked list
     * @return: ListNode head of the linked list
     */
    public static ListNode deleteDuplicates(ListNode head) {
        // write your code here
        if (head == null) return null;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode curr = dummy;
        while (curr.next != null && curr.next.next != null) {
            if (curr.next.val == curr.next.next.val) {
                int prev_val = curr.next.val;
                //store the same value
                while (curr.next != null && curr.next.val == prev_val) {
                    //if the value is the same, we redirect the curr node
                    curr.next = curr.next.next;
                }
            } else {
                curr = curr.next;//do not move curr until the next two nodes are different
            }
        }
        return dummy.next;
    }
}
```
