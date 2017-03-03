---
layout: post
title: Odd Even Linked List
date: 2016-01-18 12:00:49.000000000 -05:00
tags: algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes. You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.</em></strong></p>


``` java
public class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) return head;
        
        int index = 0;
        ListNode dummy1 = new ListNode(0), dummy2 = new ListNode(0);
        ListNode curr1 = dummy1, curr2 = dummy2;
        while (head != null) {
            index++;
            if (index % 2 != 0) {
                curr1.next = head;
                curr1 = curr1.next;
            } else {
                curr2.next = head;
                curr2 = curr2.next;
            }
            head = head.next;
        }
        curr2.next = null;
        curr1.next = dummy2.next;
        return dummy1.next;
    }
}
```
``` java
public class Solution {
    public static ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) return head;
        int index = 1;
        ListNode prev = head, curr = prev.next;
        while (curr.next != null) {
            index++;
            if (index % 2 == 0) {
                ListNode front = curr.next;
                curr.next = front.next;
                front.next = prev.next;
                prev.next = front;
                prev = front;
            } else {
                curr = curr.next;
            }
        }
        return head;
    }
}
```
