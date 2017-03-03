---
layout: post
title: Add Two Numbers
date: 2015-10-21 01:42:02.000000000 -04:00
tags: algorithm
categories:
- LinkedList
author: Jason
---
<p><strong><em>You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.</em></strong></p>


``` java
    /**
     * @param l1: the first list
     * @param l2: the second list
     * @return: the sum list of l1 and l2 
     */
    public ListNode addLists(ListNode l1, ListNode l2) {
        // write your code here
        ListNode head = new ListNode(0);
        ListNode current = head;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0){
            if(l1 != null) {
                carry += l1.val;
                l1 = l1.next;
            }
            if(l2 != null){
                carry += l2.val;
                l2 = l2.next;
            }
            current.next = new ListNode(carry % 10);
            current = current.next;
            carry /= 10;
        }
        return head.next;
    }
}
```
