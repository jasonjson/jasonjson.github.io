---
layout: post
title: Two Lists Sum
date: 2015-10-21 02:44:31.000000000 -04:00
tags:
- Algorithm
categories:
- LinkedList
author: Jason
---
<p><strong><em>You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1’s digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.</p>

  Example</p>
  Given two lists, 3->1->5->null and 5->9->2->null, return 8->0->8->null</em></strong></p>

``` java
class Solution {
    public static ListNode listSum(ListNode head1, ListNode head2) {
        if (head1 == null && head2 == null) return null;
        ListNode head3 = new ListNode(0);
        ListNode curr = head3;
        //bug: forget to store the head, and use curr to create a list
        int carry = 0;
        while (head1 != null || head2 !=null || carry != 0) {
            if (head1 != null) {
                carry += head1.val;
                head1 = head1.next;
            }
            if (head2 != null) {
                carry += head2.val;
                head2 = head2.next;
            }
            curr.next = new ListNode(carry % 10);
            curr = curr.next;
            carry = carry / 10;
        }
        //there is no need to clear curr.next since, we always create a new node and give it to curr
        return head3.next;
    }
};
```
