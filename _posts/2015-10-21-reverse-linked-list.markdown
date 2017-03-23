---
layout: post
title: Reverse Linked List
date: 2015-10-21 02:46:08.000000000 -04:00
tags:
- Algorithm
categories:
- LinkedList
author: Jason
---
<p><strong><em>Reverse a singly linked list.</em></strong></p>


``` java
public class Solution {
    /**
     * @param head: The head of linked list.
     * @return: The new head of reversed linked list.
     */
    public ListNode reverse(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode rev = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = rev;
            rev = head;
            head = next;
        }
        return rev;
    }
    //recursiton
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode rev = reverseList(head.next);
        //head.next is the last element in rev, we connect it to the first element, and clear the first element.
        head.next.next = head;
        head.next = null;
        return rev;
    }
}
```
