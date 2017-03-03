---
layout: post
title: Remove Duplicates from Sorted List
date: 2015-10-21 02:42:57.000000000 -04:00
tags: algorithm
categories:
- LinkedList
author: Jason
---
<p><strong><em>Given a sorted linked list, delete all duplicates such that each element appear only once.</em></strong></p>


``` java
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        //if (head == null) return null; bug1 no need this, if head is null, we just return it.
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        ListNode curr = head;
        ListNode prev = null;
        while (curr != null) {
            if (!map.containsKey(curr.val)) {
                map.put(curr.val, 1);
                prev = curr;
            } else {
                prev.next = curr.next;
            }
            curr = curr.next;
        }
        return head;
    }
    
    public ListNode deleteDuplicates(ListNode head) {
        ListNode curr = head;
        while (curr != null && curr.next != null) {
            if (curr.next.val == curr.val) {
                curr.next = curr.next.next;
            } else {
                curr = curr.next;
            }
        }
        return head;
    }
}
```
