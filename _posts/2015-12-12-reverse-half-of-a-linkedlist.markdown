---
layout: post
title: Reverse half of a Linkedlist
date: 2015-12-12 11:38:04.000000000 -05:00
tags:
- Algorithm
categories:
- LinkedList
author: Jason
---
<p><strong><em>Reverse the latter half of a linkedlist.</em></strong></p>


``` java
class Solution {
    public static void main(String[] args) {
        ListNode l1 = new ListNode(1);
        ListNode l2 = new ListNode(2);
        ListNode l3 = new ListNode(3);
        ListNode l4 = new ListNode(4);
        ListNode l5 = new ListNode(5);
        l1.next = l2; l2.next = l3; l3.next = l4; l4.next = l5;
        ListNode l6 = reverseHalf(l1);
        while (l6 != null) {
            System.out.println(l6.val);
            l6 = l6.next;
        }

    }
    public static ListNode reverseHalf(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode fast = head, slow = head, prev = slow;
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        prev.next = reverse(slow);
        return head;
    }
    public static ListNode reverse(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode rev = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = rev;
            rev = head;
            head = next;
        }
        return rev;
    }
}
```
