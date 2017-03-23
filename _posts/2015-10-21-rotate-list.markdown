---
layout: post
title: Rotate List
date: 2015-10-21 14:35:50.000000000 -04:00
tags:
- Algorithm
categories:
- LinkedList
- LinkedList
author: Jason
---
<p><strong><em>Given a list, rotate the list to the right by k places, where k is non-negative.</em></strong></p>


``` java
public class Solution {
    /**
     * @param head: the List
     * @param k: rotate to the right k places
     * @return: the list after rotation
     */
    public ListNode rotateRight(ListNode head, int k) {
        // write your code here
        if (head == null) return null;
        int len = getSize(head);
        k %= len;
        ListNode prev = head, right = head;
        for (int i = 0; i < len - k; i++) {//we can find the nth node from the end use len directly, since we already calculate it
            prev = right;
            right = right.next;
        }
        if (right == null) { //!!important corner case
            return head;
        }
        prev.next = null;
        ListNode tail = right;
        while (tail.next != null) {
            tail = tail.next;
        }
        tail.next = head;
        return right;
    }    
    public int getSize(ListNode head) {
        int count = 0;
        while (head != null) {
            head = head.next;
            count ++;
        }
        return count;
    }
}
```
